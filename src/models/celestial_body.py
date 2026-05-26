"""
Celestial body model used to represent stars, planets, moons, and other astronomical objects.
"""

from enum import Enum
from typing import Optional

from vpython import sphere, vector

from config.constants import (
    ARTISTIC_MOON_DISTANCE_SCALE,
    ARTISTIC_RADIUS_SCALE,
    DISTANCE_SCALE,
    MOON_TRAIL_MAX_LENGTH,
    MOON_TRAIL_MAX_WIDTH,
    PLANET_TRAIL_MAX_LENGTH,
    PLANET_TRAIL_MAX_WIDTH,
    RADIUS_SCALE,
    STAR_TRAIL_MAX_LENGTH,
    STAR_TRAIL_MAX_WIDTH,
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

        trail_length, trail_width = self._get_trail_settings()

        self.visual = sphere(
            pos=self._get_visual_position(),
            radius=self._get_visual_radius(),
            color=self.colour,
            make_trail=self.trails_enabled,
            retain=trail_length,
            trail_radius=trail_width,
        )

    def update_visual_position(self) -> None:
        """
        Updates the VPython sphere position to match the body's physical position.
        """
        self.visual.pos = self._get_visual_position()

    def set_visual_scaling_mode(self, visual_scaling_mode: VisualScalingMode) -> None:
        """
        Updates the body's visual scaling mode.
        """
        self.visual_scaling_mode = visual_scaling_mode
        self.visual.radius = self._get_visual_radius()
        self.visual.pos = self._get_visual_position()

    def set_trails_enabled(self, trails_enabled: bool) -> None:
        self.trails_enabled = trails_enabled and self.make_trail
        self.visual.make_trail = self.trails_enabled
        self.visual.clear_trail()

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
