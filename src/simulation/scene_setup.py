"""
Scene setup for the astronomical simulator.
"""

from vpython import color, scene, vector

from config.solar_system_data import (
    EARTH,
    EARTH_AVERAGE_DISTANCE,
    EARTH_AVERAGE_VELOCITY,
    EARTH_MASS,
    EARTH_RADIUS,
    MOON,
    MOON_AVERAGE_DISTANCE,
    MOON_AVERAGE_VELOCITY,
    MOON_MASS,
    MOON_RADIUS,
    SUN,
    SUN_AVERAGE_VELOCITY,
    SUN_MASS,
    SUN_RADIUS,
)
from models.celestial_body import CelestialBody, CelestialBodyType


def setup_scene() -> list[CelestialBody]:
    """
    Sets up the initial VPython scene and creates the starting celestial bodies.
    """
    scene.title = "Astronomical Simulator"
    scene.width = 2400
    scene.height = 1200
    scene.background = color.black
    scene.resizable = True

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

    earth = CelestialBody(
        type=CelestialBodyType.PLANET,
        name=EARTH,
        mass=EARTH_MASS,
        radius=EARTH_RADIUS,
        position=vector(EARTH_AVERAGE_DISTANCE, 0, 0),
        velocity=vector(0, EARTH_AVERAGE_VELOCITY, 0),
        colour=color.blue,
        make_trail=True,
    )

    moon = CelestialBody(
        type=CelestialBodyType.MOON,
        name=MOON,
        mass=MOON_MASS,
        radius=MOON_RADIUS,
        position=vector(
            EARTH_AVERAGE_DISTANCE,
            0,
            MOON_AVERAGE_DISTANCE,
        ),
        velocity=vector(
            MOON_AVERAGE_VELOCITY,
            EARTH_AVERAGE_VELOCITY,
            0,
        ),
        colour=color.white,
        make_trail=True,
    )

    return [sun, earth, moon]
