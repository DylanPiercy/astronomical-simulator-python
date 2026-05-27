"""
This file contains preset CelestialBody objects for the local solar system.
"""

from vpython import color, vector

from config.local_system_data import (
    EARTH,
    EARTH_MASS,
    EARTH_RADIUS,
    JUPITER,
    JUPITER_MASS,
    JUPITER_RADIUS,
    MARS,
    MARS_MASS,
    MARS_RADIUS,
    MERCURY,
    MERCURY_MASS,
    MERCURY_RADIUS,
    MOON,
    MOON_MASS,
    MOON_RADIUS,
    NEPTUNE,
    NEPTUNE_MASS,
    NEPTUNE_RADIUS,
    PLUTO,
    PLUTO_MASS,
    PLUTO_RADIUS,
    SATURN,
    SATURN_MASS,
    SATURN_RADIUS,
    SUN,
    SUN_AVERAGE_VELOCITY,
    SUN_MASS,
    SUN_RADIUS,
    URANUS,
    URANUS_MASS,
    URANUS_RADIUS,
    VENUS,
    VENUS_MASS,
    VENUS_RADIUS,
)
from config.local_system_state_vectors import (
    EARTH_RELATIVE_POSITION,
    EARTH_RELATIVE_VELOCITY,
    JUPITER_RELATIVE_POSITION,
    JUPITER_RELATIVE_VELOCITY,
    MARS_RELATIVE_POSITION,
    MARS_RELATIVE_VELOCITY,
    MERCURY_RELATIVE_POSITION,
    MERCURY_RELATIVE_VELOCITY,
    MOON_RELATIVE_POSITION,
    MOON_RELATIVE_VELOCITY,
    NEPTUNE_RELATIVE_POSITION,
    NEPTUNE_RELATIVE_VELOCITY,
    PLUTO_RELATIVE_POSITION,
    PLUTO_RELATIVE_VELOCITY,
    SATURN_RELATIVE_POSITION,
    SATURN_RELATIVE_VELOCITY,
    STATE_VECTORS_GENERATED,
    URANUS_RELATIVE_POSITION,
    URANUS_RELATIVE_VELOCITY,
    VENUS_RELATIVE_POSITION,
    VENUS_RELATIVE_VELOCITY,
)
from models.celestial_body import CelestialBodyType
from models.solar_system import SolarSystem
from presets.preset_creation_helpers import (
    create_orbiting_body_from_state_vector,
    create_star,
)


def create_local_system() -> SolarSystem:
    """
    Creates the preset celestial bodies for the local solar system.
    """
    if not STATE_VECTORS_GENERATED:
        raise RuntimeError(
            "JPL state vectors have not been generated. "
            "Run: python src/tools/fetch_jpl_local_system_vectors.py"
        )

    sun = create_star(
        name=SUN,
        mass=SUN_MASS,
        radius=SUN_RADIUS,
        position=vector(0, 0, 0),
        velocity=vector(0, SUN_AVERAGE_VELOCITY, 0),
        colour=color.yellow,
    )

    mercury = create_orbiting_body_from_state_vector(
        type=CelestialBodyType.PLANET,
        name=MERCURY,
        mass=MERCURY_MASS,
        radius=MERCURY_RADIUS,
        parent_body=sun,
        relative_position=vector(*MERCURY_RELATIVE_POSITION),
        relative_velocity=vector(*MERCURY_RELATIVE_VELOCITY),
        colour=color.gray(0.5),
    )

    venus = create_orbiting_body_from_state_vector(
        type=CelestialBodyType.PLANET,
        name=VENUS,
        mass=VENUS_MASS,
        radius=VENUS_RADIUS,
        parent_body=sun,
        relative_position=vector(*VENUS_RELATIVE_POSITION),
        relative_velocity=vector(*VENUS_RELATIVE_VELOCITY),
        colour=color.orange,
    )

    earth = create_orbiting_body_from_state_vector(
        type=CelestialBodyType.PLANET,
        name=EARTH,
        mass=EARTH_MASS,
        radius=EARTH_RADIUS,
        parent_body=sun,
        relative_position=vector(*EARTH_RELATIVE_POSITION),
        relative_velocity=vector(*EARTH_RELATIVE_VELOCITY),
        colour=color.blue,
    )

    moon = create_orbiting_body_from_state_vector(
        type=CelestialBodyType.MOON,
        name=MOON,
        mass=MOON_MASS,
        radius=MOON_RADIUS,
        parent_body=earth,
        relative_position=vector(*MOON_RELATIVE_POSITION),
        relative_velocity=vector(*MOON_RELATIVE_VELOCITY),
        colour=color.white,
    )

    mars = create_orbiting_body_from_state_vector(
        type=CelestialBodyType.PLANET,
        name=MARS,
        mass=MARS_MASS,
        radius=MARS_RADIUS,
        parent_body=sun,
        relative_position=vector(*MARS_RELATIVE_POSITION),
        relative_velocity=vector(*MARS_RELATIVE_VELOCITY),
        colour=color.red,
    )

    jupiter = create_orbiting_body_from_state_vector(
        type=CelestialBodyType.PLANET,
        name=JUPITER,
        mass=JUPITER_MASS,
        radius=JUPITER_RADIUS,
        parent_body=sun,
        relative_position=vector(*JUPITER_RELATIVE_POSITION),
        relative_velocity=vector(*JUPITER_RELATIVE_VELOCITY),
        colour=color.orange,
    )

    saturn = create_orbiting_body_from_state_vector(
        type=CelestialBodyType.PLANET,
        name=SATURN,
        mass=SATURN_MASS,
        radius=SATURN_RADIUS,
        parent_body=sun,
        relative_position=vector(*SATURN_RELATIVE_POSITION),
        relative_velocity=vector(*SATURN_RELATIVE_VELOCITY),
        colour=color.yellow,
    )

    uranus = create_orbiting_body_from_state_vector(
        type=CelestialBodyType.PLANET,
        name=URANUS,
        mass=URANUS_MASS,
        radius=URANUS_RADIUS,
        parent_body=sun,
        relative_position=vector(*URANUS_RELATIVE_POSITION),
        relative_velocity=vector(*URANUS_RELATIVE_VELOCITY),
        colour=color.cyan,
    )

    neptune = create_orbiting_body_from_state_vector(
        type=CelestialBodyType.PLANET,
        name=NEPTUNE,
        mass=NEPTUNE_MASS,
        radius=NEPTUNE_RADIUS,
        parent_body=sun,
        relative_position=vector(*NEPTUNE_RELATIVE_POSITION),
        relative_velocity=vector(*NEPTUNE_RELATIVE_VELOCITY),
        colour=color.blue,
    )

    pluto = create_orbiting_body_from_state_vector(
        type=CelestialBodyType.DWARF_PLANET,
        name=PLUTO,
        mass=PLUTO_MASS,
        radius=PLUTO_RADIUS,
        parent_body=sun,
        relative_position=vector(*PLUTO_RELATIVE_POSITION),
        relative_velocity=vector(*PLUTO_RELATIVE_VELOCITY),
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
