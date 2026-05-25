"""
Scene setup for the astronomical simulator.
"""

from vpython import color, scene, vector

from config.constants import DISTANCE_SCALE
from config.solar_system_data import (
    EARTH,
    EARTH_AVERAGE_ORBITAL_DISTANCE,
    EARTH_MASS,
    EARTH_RADIUS,
    SUN,
    SUN_MASS,
    SUN_RADIUS,
)
from models.celestial_body import CelestialBody


def setup_scene() -> list[CelestialBody]:
    """
    Sets up the initial VPython scene and creates the starting celestial bodies.
    """
    scene.title = "Astronomical Simulator"
    scene.width = 2400
    scene.height = 1200
    scene.background = color.black

    sun = CelestialBody(
        name=SUN,
        mass=SUN_MASS,
        radius=SUN_RADIUS,
        position=vector(0, 0, 0),
        velocity=vector(0, 0, 0),
        colour=color.yellow,
        make_trail=False,
    )

    earth = CelestialBody(
        name=EARTH,
        mass=EARTH_MASS,
        radius=EARTH_RADIUS,
        position=vector(EARTH_AVERAGE_ORBITAL_DISTANCE * DISTANCE_SCALE, 0, 0),
        velocity=vector(0, 29_780, 0),
        colour=color.blue,
        make_trail=True,
    )

    return [sun, earth]