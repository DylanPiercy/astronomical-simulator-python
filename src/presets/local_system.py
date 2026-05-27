"""
This file contains preset CelestialBody objects for the local solar system.
"""

from vpython import color, vector

from config.local_system_data import *
from models.solar_system import SolarSystem
from presets.preset_creation_helpers import create_moon, create_planet, create_star


def create_local_system() -> SolarSystem:
    """
    Creates the preset celestial bodies for the local solar system.
    """

    sun = create_star(
        name=SUN,
        mass=SUN_MASS,
        radius=SUN_RADIUS,
        position=vector(0, 0, 0),
        velocity=vector(0, SUN_AVERAGE_VELOCITY, 0),
        colour=color.yellow,
    )

    mercury = create_planet(
        name=MERCURY,
        mass=MERCURY_MASS,
        radius=MERCURY_RADIUS,
        parent_body=sun,
        distance=MERCURY_AVERAGE_DISTANCE,
        velocity=MERCURY_AVERAGE_VELOCITY,
        colour=color.gray(0.5),
        inclination_degrees=MERCURY_ORBITAL_INCLINATION,
        phase_degrees=MERCURY_ORBITAL_PHASE,
    )

    venus = create_planet(
        name=VENUS,
        mass=VENUS_MASS,
        radius=VENUS_RADIUS,
        parent_body=sun,
        distance=VENUS_AVERAGE_DISTANCE,
        velocity=VENUS_AVERAGE_VELOCITY,
        colour=color.orange,
        inclination_degrees=VENUS_ORBITAL_INCLINATION,
        phase_degrees=VENUS_ORBITAL_PHASE,
    )

    earth = create_planet(
        name=EARTH,
        mass=EARTH_MASS,
        radius=EARTH_RADIUS,
        parent_body=sun,
        distance=EARTH_AVERAGE_DISTANCE,
        velocity=EARTH_AVERAGE_VELOCITY,
        colour=color.blue,
        inclination_degrees=EARTH_ORBITAL_INCLINATION,
        phase_degrees=EARTH_ORBITAL_PHASE,
    )

    moon = create_moon(
        name=MOON,
        mass=MOON_MASS,
        radius=MOON_RADIUS,
        parent_body=earth,
        distance=MOON_AVERAGE_DISTANCE,
        velocity=MOON_AVERAGE_VELOCITY,
        colour=color.white,
        inclination_degrees=MOON_ORBITAL_INCLINATION,
        phase_degrees=MOON_ORBITAL_PHASE,
    )

    mars = create_planet(
        name=MARS,
        mass=MARS_MASS,
        radius=MARS_RADIUS,
        parent_body=sun,
        distance=MARS_AVERAGE_DISTANCE,
        velocity=MARS_AVERAGE_VELOCITY,
        colour=color.red,
        inclination_degrees=MARS_ORBITAL_INCLINATION,
        phase_degrees=MARS_ORBITAL_PHASE,
    )

    jupiter = create_planet(
        name=JUPITER,
        mass=JUPITER_MASS,
        radius=JUPITER_RADIUS,
        parent_body=sun,
        distance=JUPITER_AVERAGE_DISTANCE,
        velocity=JUPITER_AVERAGE_VELOCITY,
        colour=color.orange,
        inclination_degrees=JUPITER_ORBITAL_INCLINATION,
        phase_degrees=JUPITER_ORBITAL_PHASE,
    )

    saturn = create_planet(
        name=SATURN,
        mass=SATURN_MASS,
        radius=SATURN_RADIUS,
        parent_body=sun,
        distance=SATURN_AVERAGE_DISTANCE,
        velocity=SATURN_AVERAGE_VELOCITY,
        colour=color.yellow,
        inclination_degrees=SATURN_ORBITAL_INCLINATION,
        phase_degrees=SATURN_ORBITAL_PHASE,
    )

    uranus = create_planet(
        name=URANUS,
        mass=URANUS_MASS,
        radius=URANUS_RADIUS,
        parent_body=sun,
        distance=URANUS_AVERAGE_DISTANCE,
        velocity=URANUS_AVERAGE_VELOCITY,
        colour=color.cyan,
        inclination_degrees=URANUS_ORBITAL_INCLINATION,
        phase_degrees=URANUS_ORBITAL_PHASE,
    )

    neptune = create_planet(
        name=NEPTUNE,
        mass=NEPTUNE_MASS,
        radius=NEPTUNE_RADIUS,
        parent_body=sun,
        distance=NEPTUNE_AVERAGE_DISTANCE,
        velocity=NEPTUNE_AVERAGE_VELOCITY,
        colour=color.blue,
        inclination_degrees=NEPTUNE_ORBITAL_INCLINATION,
        phase_degrees=NEPTUNE_ORBITAL_PHASE,
    )

    pluto = create_planet(
        name=PLUTO,
        mass=PLUTO_MASS,
        radius=PLUTO_RADIUS,
        parent_body=sun,
        distance=PLUTO_AVERAGE_DISTANCE,
        velocity=PLUTO_AVERAGE_VELOCITY,
        colour=color.gray(0.7),
        inclination_degrees=PLUTO_ORBITAL_INCLINATION,
        phase_degrees=PLUTO_ORBITAL_PHASE,
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
