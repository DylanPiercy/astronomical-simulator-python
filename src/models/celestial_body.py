"""
Celestial body model used to represent stars, planets, moons, and other astronomical objects.
"""
from enum import Enum
from vpython import sphere, vector

from config.constants import (
    DISTANCE_SCALE,
    STAR_RADIUS_SCALE,
    PLANET_RADIUS_SCALE,
    MOON_RADIUS_SCALE,
    MIN_PLANET_RADIUS_SCALE,
    MIN_MOON_RADIUS_SCALE,
    PLANET_TRAIL_RETAIN,
    MOON_TRAIL_RETAIN,
)


class CelestialBodyType(Enum):
    STAR = "star"
    PLANET = "planet"
    MOON = "moon"


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
    ):
        self.type = type
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity

        if self.type == CelestialBodyType.STAR:
            visual_radius = radius * STAR_RADIUS_SCALE
            self.make_trail = False
            trail_retain = 0
        elif self.type == CelestialBodyType.PLANET:
            visual_radius = max(radius * PLANET_RADIUS_SCALE, MIN_PLANET_RADIUS_SCALE)
            self.make_trail = make_trail
            trail_retain = PLANET_TRAIL_RETAIN if make_trail else 0
        elif self.type == CelestialBodyType.MOON:
            visual_radius = max(radius * MOON_RADIUS_SCALE, MIN_MOON_RADIUS_SCALE)
            self.make_trail = make_trail
            trail_retain = MOON_TRAIL_RETAIN if make_trail else 0
        else:
            raise ValueError(f"Invalid celestial body type: {self.type}")
        
        self.visual = sphere(
            pos=self.position * DISTANCE_SCALE,
            radius=visual_radius,
            color=colour,
            make_trail=make_trail,
            retain=trail_retain,
        )

    def update_visual_position(self) -> None:
        """
        Updates the VPython sphere position to match the body's physical position.
        """
        self.visual.pos = self.position * DISTANCE_SCALE
