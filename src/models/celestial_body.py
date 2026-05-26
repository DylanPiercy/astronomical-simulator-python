"""
Celestial body model used to represent stars, planets, moons, and other astronomical objects.
"""

from enum import Enum
from typing import Any, Optional

from vpython import curve, sphere, vector

from config.constants import (
    ARTISTIC_MOON_DISTANCE_SCALE,
    ARTISTIC_RADIUS_SCALE,
    DISTANCE_SCALE,
    MOON_TRAIL_MAX_LENGTH,
    MOON_TRAIL_MAX_WIDTH,
    PLANET_TRAIL_MAX_LENGTH,
    PLANET_TRAIL_MAX_WIDTH,
    RADIUS_SCALE,
    SECONDS_IN_DAY,
    STAR_TRAIL_MAX_LENGTH,
    STAR_TRAIL_MAX_WIDTH,
    TRAIL_GAP_POINTS,
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
        self.trail_max_length, self.trail_width = self._get_trail_settings()
        self.trail_recent_positions = []
        self.trail_positions = []
        self.trail: Any = self._create_trail()

        self.visual = sphere(
            pos=self._get_visual_position(),
            radius=self._get_visual_radius(),
            color=self.colour,
            make_trail=False,
        )

    def update_visual_position(self, time_step: float = 0) -> None:
        """
        Updates the VPython sphere position to match the body's physical position.
        """
        self.visual.pos = self._get_visual_position()
        self._update_trail(time_step)

    def set_visual_scaling_mode(self, visual_scaling_mode: VisualScalingMode) -> None:
        """
        Updates the body's visual scaling mode.
        """
        self.visual_scaling_mode = visual_scaling_mode
        self.visual.radius = self._get_visual_radius()
        self.visual.pos = self._get_visual_position()
        self._clear_trail()

    def set_trails_enabled(self, trails_enabled: bool) -> None:
        """
        Enables or disables this body's custom trail.
        """
        self.trails_enabled = trails_enabled and self.make_trail

        if not self.trails_enabled:
            self._clear_trail()

    def _get_visual_radius(self) -> float:
        """
        Returns the scaled visual radius for the current scaling mode.
        """
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
        """
        Returns the moon distance scale for the current visual scaling mode.
        """
        if self.visual_scaling_mode == VisualScalingMode.REALISTIC:
            return DISTANCE_SCALE

        return ARTISTIC_MOON_DISTANCE_SCALE

    def _get_trail_settings(self) -> tuple[int, float]:
        """
        Returns trail length and width for this body.
        """
        if not self.make_trail:
            return 0, 0

        if self.type == CelestialBodyType.STAR:
            return STAR_TRAIL_MAX_LENGTH, STAR_TRAIL_MAX_WIDTH

        if self.type == CelestialBodyType.PLANET:
            return PLANET_TRAIL_MAX_LENGTH, PLANET_TRAIL_MAX_WIDTH

        if self.type == CelestialBodyType.MOON:
            return MOON_TRAIL_MAX_LENGTH, MOON_TRAIL_MAX_WIDTH

        raise ValueError(f"Invalid celestial body type: {self.type}")

    def _create_trail(self):
        """
        Creates the custom trail curve.
        """
        if not self.make_trail:
            return None

        return curve(
            color=self.colour,
            radius=self.trail_width,
        )

    def _update_trail(self, time_step: float) -> None:
        """
        Adds trail points based on simulated time, leaving a gap behind the body.
        """
        if not self.trails_enabled or self.trail is None:
            return

        trail_point_interval = SECONDS_IN_DAY / TRAIL_POINTS_PER_SIMULATED_DAY
        self.simulated_seconds_since_last_trail_point += time_step

        if self.simulated_seconds_since_last_trail_point < trail_point_interval:
            return

        self.simulated_seconds_since_last_trail_point -= trail_point_interval
        self.trail_recent_positions.append(self._copy_position(self.visual.pos))

        if len(self.trail_recent_positions) <= TRAIL_GAP_POINTS:
            return

        trail_position = self.trail_recent_positions.pop(0)
        self.trail_positions.append(trail_position)
        self.trail.append(pos=trail_position)

        if len(self.trail_positions) > self.trail_max_length:
            self.trail_positions.pop(0)
            self._rebuild_trail()

    def _rebuild_trail(self) -> None:
        """
        Rebuilds the trail after old points are removed.
        """
        if self.trail is None:
            return

        self.trail.clear()

        for trail_position in self.trail_positions:
            self.trail.append(pos=trail_position)

    def _clear_trail(self) -> None:
        """
        Clears stored and rendered trail positions.
        """
        self.simulated_seconds_since_last_trail_point = 0
        self.trail_recent_positions.clear()
        self.trail_positions.clear()

        if self.trail is not None:
            self.trail.clear()

    def _copy_position(self, position: vector) -> vector:
        """
        Returns a detached copy of a VPython vector position.
        """
        return vector(position.x, position.y, position.z)
