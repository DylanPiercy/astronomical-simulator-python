"""
Celestial body model used to represent stars, planets, moons, and other astronomical objects.
"""

from enum import Enum
from math import pi
from typing import Optional

from vpython import sphere, vector

from config.constants import (
    ARTISTIC_MOON_DISTANCE_SCALE,
    ARTISTIC_RADIUS_SCALE,
    DEFAULT_TRAIL_MARKER_RADIUS_SCALE,
    DISTANCE_SCALE,
    MAX_DYNAMIC_TRAIL_MARKER_COUNT,
    MIN_DYNAMIC_TRAIL_MARKER_COUNT,
    MOON_TRAIL_MARKER_RADIUS,
    PLANET_TRAIL_MARKER_RADIUS,
    RADIUS_SCALE,
    SECONDS_IN_DAY,
    STAR_TRAIL_MARKER_RADIUS,
    TRAIL_GAP_POINTS,
    TRAIL_ORBIT_FRACTION,
    TRAIL_POINTS_PER_SIMULATED_DAY,
)


class CelestialBodyType(Enum):
    STAR = "Star"
    PLANET = "Planet"
    MOON = "Moon"


class VisualScalingMode(Enum):
    REALISTIC = "Realistic"
    ARTISTIC = "Artistic"


class CelestialBody:
    """
    Represents a physical body in the simulation.

    Position, velocity, mass, and radius use real SI units.
    The visual sphere is scaled separately for display.
    """

    def __init__(
        self,
        type: CelestialBodyType,
        name: str,
        mass: float,
        radius: float,
        position: vector,
        velocity: vector,
        colour: vector,
        make_trail: bool,
        parent_body: Optional["CelestialBody"] = None,
        visual_scaling_mode: VisualScalingMode = VisualScalingMode.ARTISTIC,
    ):
        self.type = type
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.colour = colour
        self.make_trail = make_trail
        self.parent_body = parent_body
        self.visual_scaling_mode = visual_scaling_mode

        self.trails_enabled = make_trail
        self.simulated_seconds_since_last_trail_point = 0
        self.previous_visual_position = None

        self.trail_marker_count, self.base_trail_marker_radius = (
            self._get_trail_settings()
        )
        self.trail_marker_radius_scale = DEFAULT_TRAIL_MARKER_RADIUS_SCALE
        self.trail_recent_positions = []
        self.trail_markers = self._create_trail_markers()
        self.trail_marker_has_position = [False for _ in self.trail_markers]
        self.next_trail_marker_index = 0

        self.visual = sphere(
            pos=self._get_visual_position(),
            radius=self._get_visual_radius(),
            color=self.colour,
            make_trail=False,
        )

        self.previous_visual_position = self._copy_position(self.visual.pos)

    def update_visual_position(self, time_step: float = 0) -> None:
        """
        Updates the VPython sphere position to match the body's physical position.
        """
        old_visual_position = self._copy_position(self.visual.pos)

        self.visual.pos = self._get_visual_position()

        new_visual_position = self._copy_position(self.visual.pos)

        self._update_trail(
            time_step=time_step,
            old_visual_position=old_visual_position,
            new_visual_position=new_visual_position,
        )

        self.previous_visual_position = new_visual_position

    def set_visual_scaling_mode(self, visual_scaling_mode: VisualScalingMode) -> None:
        """
        Updates the body's visual scaling mode.
        """
        self.visual_scaling_mode = visual_scaling_mode
        self.visual.radius = self._get_visual_radius()
        self.visual.pos = self._get_visual_position()
        self.previous_visual_position = self._copy_position(self.visual.pos)
        self._clear_trail()

    def set_trails_enabled(self, trails_enabled: bool) -> None:
        """
        Shows or hides this body's trail markers without stopping trail recording.
        """
        self.trails_enabled = trails_enabled and self.make_trail

        for index, marker in enumerate(self.trail_markers):
            marker.visible = (
                self.trails_enabled and self.trail_marker_has_position[index]
            )

    def set_trail_marker_radius_scale(self, trail_marker_radius_scale: float) -> None:
        """
        Updates the radius scale for trail markers.
        """
        self.trail_marker_radius_scale = trail_marker_radius_scale

        for marker in self.trail_markers:
            marker.radius = self._get_scaled_trail_marker_radius()

    def _get_visual_radius(self) -> float:
        if self.visual_scaling_mode == VisualScalingMode.REALISTIC:
            return self.radius * RADIUS_SCALE

        return self.radius * ARTISTIC_RADIUS_SCALE

    def _get_visual_position(self) -> vector:
        """
        Returns the scaled visual position for the body.
        """
        if self.type == CelestialBodyType.MOON and self.parent_body is not None:
            moon_offset_from_parent = self.position - self.parent_body.position
            moon_distance_scale = self._get_moon_distance_scale()

            return (
                self.parent_body.visual.pos
                + moon_offset_from_parent * moon_distance_scale
            )

        return self.position * DISTANCE_SCALE

    def _get_moon_distance_scale(self) -> float:
        if self.visual_scaling_mode == VisualScalingMode.REALISTIC:
            return DISTANCE_SCALE

        return ARTISTIC_MOON_DISTANCE_SCALE

    def _get_trail_settings(self) -> tuple[int, float]:
        """
        Returns trail marker count and marker radius for this body.
        """
        if not self.make_trail:
            return 0, 0

        return (
            self._calculate_dynamic_trail_marker_count(),
            self._get_base_trail_marker_radius(),
        )

    def _get_base_trail_marker_radius(self) -> float:
        if self.type == CelestialBodyType.STAR:
            return STAR_TRAIL_MARKER_RADIUS

        if self.type == CelestialBodyType.PLANET:
            return PLANET_TRAIL_MARKER_RADIUS

        if self.type == CelestialBodyType.MOON:
            return MOON_TRAIL_MARKER_RADIUS

        raise ValueError(f"Invalid celestial body type: {self.type}")

    def _calculate_dynamic_trail_marker_count(self) -> int:
        """
        Calculates trail marker count from estimated orbit size.

        The target is a configurable fraction of the body's orbit around its parent.
        Bodies without a parent fall back to the minimum marker count.
        """
        if self.parent_body is None:
            return MIN_DYNAMIC_TRAIL_MARKER_COUNT

        orbital_radius = (self.position - self.parent_body.position).mag
        relative_speed = (self.velocity - self.parent_body.velocity).mag

        if orbital_radius <= 0 or relative_speed <= 0:
            return MIN_DYNAMIC_TRAIL_MARKER_COUNT

        orbital_period_seconds = 2 * pi * orbital_radius / relative_speed
        trail_duration_days = (
            orbital_period_seconds / SECONDS_IN_DAY * TRAIL_ORBIT_FRACTION
        )
        marker_count = round(trail_duration_days * TRAIL_POINTS_PER_SIMULATED_DAY)

        return self._clamp_marker_count(marker_count)

    def _clamp_marker_count(self, marker_count: int) -> int:
        """
        Keeps dynamic trail marker counts within safe performance bounds.
        """
        return max(
            MIN_DYNAMIC_TRAIL_MARKER_COUNT,
            min(MAX_DYNAMIC_TRAIL_MARKER_COUNT, marker_count),
        )

    def _create_trail_markers(self) -> list:
        """
        Creates reusable hidden trail marker spheres.
        """
        if not self.make_trail:
            return []

        return [
            sphere(
                pos=vector(0, 0, 0),
                radius=self._get_scaled_trail_marker_radius(),
                color=self.colour,
                visible=False,
                make_trail=False,
            )
            for _ in range(self.trail_marker_count)
        ]

    def _get_scaled_trail_marker_radius(self) -> float:
        return self.base_trail_marker_radius * self.trail_marker_radius_scale

    def _update_trail(
        self,
        time_step: float,
        old_visual_position: vector,
        new_visual_position: vector,
    ) -> None:
        """
        Updates trail markers based on simulated time.

        Trail sample positions are interpolated between the previous and current
        visual position so marker spacing remains consistent at different speeds.
        """
        if not self.make_trail or not self.trail_markers or time_step <= 0:
            return

        trail_point_interval = SECONDS_IN_DAY / TRAIL_POINTS_PER_SIMULATED_DAY
        self.simulated_seconds_since_last_trail_point += time_step

        while self.simulated_seconds_since_last_trail_point >= trail_point_interval:
            overshoot_seconds = (
                self.simulated_seconds_since_last_trail_point - trail_point_interval
            )
            interpolation_ratio = 1 - (overshoot_seconds / time_step)

            interpolated_position = self._interpolate_position(
                old_visual_position,
                new_visual_position,
                interpolation_ratio,
            )

            self._add_trail_sample(interpolated_position)

            self.simulated_seconds_since_last_trail_point -= trail_point_interval

    def _add_trail_sample(self, trail_position: vector) -> None:
        """
        Adds a sampled position to the trail, respecting the gap behind the body.
        """
        self.trail_recent_positions.append(trail_position)

        if len(self.trail_recent_positions) <= TRAIL_GAP_POINTS:
            return

        visible_trail_position = self.trail_recent_positions.pop(0)
        trail_marker = self.trail_markers[self.next_trail_marker_index]

        trail_marker.pos = visible_trail_position
        trail_marker.radius = self._get_scaled_trail_marker_radius()
        self.trail_marker_has_position[self.next_trail_marker_index] = True
        trail_marker.visible = self.trails_enabled

        self.next_trail_marker_index = (self.next_trail_marker_index + 1) % len(
            self.trail_markers
        )

    def _interpolate_position(
        self,
        start_position: vector,
        end_position: vector,
        interpolation_ratio: float,
    ) -> vector:
        """
        Interpolates between two visual positions.
        """
        clamped_ratio = max(0, min(1, interpolation_ratio))

        return start_position + (end_position - start_position) * clamped_ratio

    def _clear_trail(self) -> None:
        """
        Resets stored trail state and hides all trail markers.
        """
        self.simulated_seconds_since_last_trail_point = 0
        self.trail_recent_positions.clear()
        self.next_trail_marker_index = 0
        self.trail_marker_has_position = [False for _ in self.trail_markers]
        self._hide_trail_markers()

    def _hide_trail_markers(self) -> None:
        for marker in self.trail_markers:
            marker.visible = False

    def _copy_position(self, position: vector) -> vector:
        """
        Returns a detached copy of a VPython vector position.
        """
        return vector(position.x, position.y, position.z)
