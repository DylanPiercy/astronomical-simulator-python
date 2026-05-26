"""
Celestial body model used to represent stars, planets, moons, and other astronomical objects.
"""

from enum import Enum
from typing import Optional

from vpython import sphere, vector

from config.constants import (
    ARTISTIC_MOON_DISTANCE_SCALE,
    DISTANCE_SCALE,
    STAR_RADIUS_SCALE,
    PLANET_RADIUS_SCALE,
    MOON_RADIUS_SCALE,
    MIN_PLANET_RADIUS_SCALE,
    MIN_MOON_RADIUS_SCALE,
    PLANET_TRAIL_MAX_LENGTH,
    MOON_TRAIL_MAX_LENGTH,
    PLANET_TRAIL_MAX_WIDTH,
    MOON_TRAIL_MAX_WIDTH,
    STAR_TRAIL_MAX_LENGTH,
    STAR_TRAIL_MAX_WIDTH,
)


class CelestialBodyType(Enum):
    STAR = "Star"
    PLANET = "Planet"
    MOON = "Moon"


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

        if self.type == CelestialBodyType.STAR:
            visual_radius = radius * STAR_RADIUS_SCALE
            trail_length = STAR_TRAIL_MAX_LENGTH if self.make_trail else 0
            trail_width = STAR_TRAIL_MAX_WIDTH if self.make_trail else 0
        elif self.type == CelestialBodyType.PLANET:
            visual_radius = max(radius * PLANET_RADIUS_SCALE, MIN_PLANET_RADIUS_SCALE)
            trail_length = PLANET_TRAIL_MAX_LENGTH if self.make_trail else 0
            trail_width = PLANET_TRAIL_MAX_WIDTH if self.make_trail else 0
        elif self.type == CelestialBodyType.MOON:
            visual_radius = max(radius * MOON_RADIUS_SCALE, MIN_MOON_RADIUS_SCALE)
            trail_length = MOON_TRAIL_MAX_LENGTH if self.make_trail else 0
            trail_width = MOON_TRAIL_MAX_WIDTH if self.make_trail else 0
        else:
            raise ValueError(f"Invalid celestial body type: {self.type}")

        self.visual = sphere(
            pos=self._get_visual_position(),
            radius=visual_radius,
            color=self.colour,
            make_trail=self.make_trail,
            retain=trail_length,
            trail_radius=trail_width,
        )

    def update_visual_position(self) -> None:
        """
        Updates the VPython sphere position to match the body's physical position.
        """
        self.visual.pos = self._get_visual_position()

    def _get_visual_position(self) -> vector:
        """
        Returns the scaled visual position for the body.
        """
        if self.type == CelestialBodyType.MOON and self.parent_body is not None:
            moon_offset_from_parent = self.position - self.parent_body.position
            return (
                self.parent_body.visual.pos
                + moon_offset_from_parent * ARTISTIC_MOON_DISTANCE_SCALE
            )

        return self.position * DISTANCE_SCALE
