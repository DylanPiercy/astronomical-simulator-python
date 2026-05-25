"""
This file contains preset CelestialBody objects for the local solar system.
"""

from vpython import color, vector

from config.solar_system_data import (
    EARTH,
    EARTH_AVERAGE_DISTANCE,
    EARTH_AVERAGE_VELOCITY,
    EARTH_MASS,
    EARTH_RADIUS,
    JUPITER,
    JUPITER_AVERAGE_DISTANCE,
    JUPITER_AVERAGE_VELOCITY,
    JUPITER_MASS,
    JUPITER_RADIUS,
    MARS,
    MARS_AVERAGE_DISTANCE,
    MARS_AVERAGE_VELOCITY,
    MARS_MASS,
    MARS_RADIUS,
    MERCURY,
    MERCURY_AVERAGE_DISTANCE,
    MERCURY_AVERAGE_VELOCITY,
    MERCURY_MASS,
    MERCURY_RADIUS,
    MOON,
    MOON_AVERAGE_DISTANCE,
    MOON_AVERAGE_VELOCITY,
    MOON_MASS,
    MOON_RADIUS,
    NEPTUNE,
    NEPTUNE_AVERAGE_DISTANCE,
    NEPTUNE_AVERAGE_VELOCITY,
    NEPTUNE_MASS,
    NEPTUNE_RADIUS,
    PLUTO,
    PLUTO_AVERAGE_DISTANCE,
    PLUTO_AVERAGE_VELOCITY,
    PLUTO_MASS,
    PLUTO_RADIUS,
    SATURN,
    SATURN_AVERAGE_DISTANCE,
    SATURN_AVERAGE_VELOCITY,
    SATURN_MASS,
    SATURN_RADIUS,
    SUN,
    SUN_AVERAGE_VELOCITY,
    SUN_MASS,
    SUN_RADIUS,
    URANUS,
    URANUS_AVERAGE_DISTANCE,
    URANUS_AVERAGE_VELOCITY,
    URANUS_MASS,
    URANUS_RADIUS,
    VENUS,
    VENUS_AVERAGE_DISTANCE,
    VENUS_AVERAGE_VELOCITY,
    VENUS_MASS,
    VENUS_RADIUS,
)
from models.celestial_body import CelestialBody, CelestialBodyType
from models.solar_system import SolarSystem


def create_local_system() -> SolarSystem:
    """
    Creates the preset celestial bodies for the local solar system.
    """

    sun = CelestialBody(
        type=CelestialBodyType.STAR,
        name=SUN,
        mass=SUN_MASS,
        radius=SUN_RADIUS,
        position=vector(0, 0, 0),
        velocity=vector(0, SUN_AVERAGE_VELOCITY, 0),
        colour=color.yellow,
        make_trail=False,
    )

    mercury = _create_planet(
        name=MERCURY,
        mass=MERCURY_MASS,
        radius=MERCURY_RADIUS,
        distance=MERCURY_AVERAGE_DISTANCE,
        velocity=MERCURY_AVERAGE_VELOCITY,
        colour=color.gray(0.5),
    )

    venus = _create_planet(
        name=VENUS,
        mass=VENUS_MASS,
        radius=VENUS_RADIUS,
        distance=VENUS_AVERAGE_DISTANCE,
        velocity=VENUS_AVERAGE_VELOCITY,
        colour=color.orange,
    )

    earth = _create_planet(
        name=EARTH,
        mass=EARTH_MASS,
        radius=EARTH_RADIUS,
        distance=EARTH_AVERAGE_DISTANCE,
        velocity=EARTH_AVERAGE_VELOCITY,
        colour=color.blue,
    )

    moon = _create_moon(
        name=MOON,
        mass=MOON_MASS,
        radius=MOON_RADIUS,
        parent_distance=EARTH_AVERAGE_DISTANCE,
        parent_velocity=EARTH_AVERAGE_VELOCITY,
        moon_distance=MOON_AVERAGE_DISTANCE,
        moon_velocity=MOON_AVERAGE_VELOCITY,
        colour=color.white,
    )

    mars = _create_planet(
        name=MARS,
        mass=MARS_MASS,
        radius=MARS_RADIUS,
        distance=MARS_AVERAGE_DISTANCE,
        velocity=MARS_AVERAGE_VELOCITY,
        colour=color.red,
    )

    jupiter = _create_planet(
        name=JUPITER,
        mass=JUPITER_MASS,
        radius=JUPITER_RADIUS,
        distance=JUPITER_AVERAGE_DISTANCE,
        velocity=JUPITER_AVERAGE_VELOCITY,
        colour=color.orange,
    )

    saturn = _create_planet(
        name=SATURN,
        mass=SATURN_MASS,
        radius=SATURN_RADIUS,
        distance=SATURN_AVERAGE_DISTANCE,
        velocity=SATURN_AVERAGE_VELOCITY,
        colour=color.yellow,
    )

    uranus = _create_planet(
        name=URANUS,
        mass=URANUS_MASS,
        radius=URANUS_RADIUS,
        distance=URANUS_AVERAGE_DISTANCE,
        velocity=URANUS_AVERAGE_VELOCITY,
        colour=color.cyan,
    )

    neptune = _create_planet(
        name=NEPTUNE,
        mass=NEPTUNE_MASS,
        radius=NEPTUNE_RADIUS,
        distance=NEPTUNE_AVERAGE_DISTANCE,
        velocity=NEPTUNE_AVERAGE_VELOCITY,
        colour=color.blue,
    )

    pluto = _create_planet(
        name=PLUTO,
        mass=PLUTO_MASS,
        radius=PLUTO_RADIUS,
        distance=PLUTO_AVERAGE_DISTANCE,
        velocity=PLUTO_AVERAGE_VELOCITY,
        colour=color.gray(0.7),
    )

    return SolarSystem(
        name="Local Solar System",
        bodies=[
            sun,
            mercury,
            venus,
            earth,
            moon,
            mars,
            jupiter,
            saturn,
            uranus,
            neptune,
            pluto,
        ],
    )


def _create_planet(
    name: str,
    mass: float,
    radius: float,
    distance: float,
    velocity: float,
    colour,
) -> CelestialBody:
    """
    Creates a planet orbiting the Sun in the X/Y plane.
    """
    return CelestialBody(
        type=CelestialBodyType.PLANET,
        name=name,
        mass=mass,
        radius=radius,
        position=vector(distance, 0, 0),
        velocity=vector(0, velocity, 0),
        colour=colour,
        make_trail=True,
    )

def _create_moon(
    name: str,
    mass: float,
    radius: float,
    parent_distance: float,
    parent_velocity: float,
    moon_distance: float,
    moon_velocity: float,
    colour,
) -> CelestialBody:
    """
    Creates a moon orbiting a parent body in the X/Z plane.
    """
    return CelestialBody(
        type=CelestialBodyType.MOON,
        name=name,
        mass=mass,
        radius=radius,
        position=vector(
            parent_distance,
            0,
            moon_distance,
        ),
        velocity=vector(
            moon_velocity,
            parent_velocity,
            0,
        ),
        colour=colour,
        make_trail=True,
    )
