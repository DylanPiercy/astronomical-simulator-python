"""
This file contains preset CelestialBody objects for the local solar system.
"""

from vpython import color, vector

from config.local_system_data import *
from config.local_system_state_vectors import *
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
        id="sun",
        name=SUN,
        mass=SUN_MASS,
        radius=SUN_RADIUS,
        position=vector(*SUN_RELATIVE_POSITION),
        velocity=vector(*SUN_RELATIVE_VELOCITY)
        + vector(0, LOCAL_SYSTEM_GALACTIC_VELOCITY, 0),
        colour=color.yellow,
    )

    mercury = create_orbiting_body_from_state_vector(
        id="mercury",
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
        id="venus",
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
        id="earth",
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
        id="earth_moon",
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
        id="mars",
        type=CelestialBodyType.PLANET,
        name=MARS,
        mass=MARS_MASS,
        radius=MARS_RADIUS,
        parent_body=sun,
        relative_position=vector(*MARS_RELATIVE_POSITION),
        relative_velocity=vector(*MARS_RELATIVE_VELOCITY),
        colour=color.red,
    )

    phobos = create_orbiting_body_from_state_vector(
        id="mars_phobos",
        type=CelestialBodyType.MOON,
        name=PHOBOS,
        mass=PHOBOS_MASS,
        radius=PHOBOS_RADIUS,
        parent_body=mars,
        relative_position=vector(*PHOBOS_RELATIVE_POSITION),
        relative_velocity=vector(*PHOBOS_RELATIVE_VELOCITY),
        colour=color.gray(0.6),
    )

    deimos = create_orbiting_body_from_state_vector(
        id="mars_deimos",
        type=CelestialBodyType.MOON,
        name=DEIMOS,
        mass=DEIMOS_MASS,
        radius=DEIMOS_RADIUS,
        parent_body=mars,
        relative_position=vector(*DEIMOS_RELATIVE_POSITION),
        relative_velocity=vector(*DEIMOS_RELATIVE_VELOCITY),
        colour=color.gray(0.7),
    )

    jupiter = create_orbiting_body_from_state_vector(
        id="jupiter",
        type=CelestialBodyType.PLANET,
        name=JUPITER,
        mass=JUPITER_MASS,
        radius=JUPITER_RADIUS,
        parent_body=sun,
        relative_position=vector(*JUPITER_RELATIVE_POSITION),
        relative_velocity=vector(*JUPITER_RELATIVE_VELOCITY),
        colour=color.orange,
    )

    io = create_orbiting_body_from_state_vector(
        id="jupiter_io",
        type=CelestialBodyType.MOON,
        name=IO,
        mass=IO_MASS,
        radius=IO_RADIUS,
        parent_body=jupiter,
        relative_position=vector(*IO_RELATIVE_POSITION),
        relative_velocity=vector(*IO_RELATIVE_VELOCITY),
        colour=color.orange,
    )

    europa = create_orbiting_body_from_state_vector(
        id="jupiter_europa",
        type=CelestialBodyType.MOON,
        name=EUROPA,
        mass=EUROPA_MASS,
        radius=EUROPA_RADIUS,
        parent_body=jupiter,
        relative_position=vector(*EUROPA_RELATIVE_POSITION),
        relative_velocity=vector(*EUROPA_RELATIVE_VELOCITY),
        colour=color.white,
    )

    ganymede = create_orbiting_body_from_state_vector(
        id="jupiter_ganymede",
        type=CelestialBodyType.MOON,
        name=GANYMEDE,
        mass=GANYMEDE_MASS,
        radius=GANYMEDE_RADIUS,
        parent_body=jupiter,
        relative_position=vector(*GANYMEDE_RELATIVE_POSITION),
        relative_velocity=vector(*GANYMEDE_RELATIVE_VELOCITY),
        colour=color.gray(0.7),
    )

    callisto = create_orbiting_body_from_state_vector(
        id="jupiter_callisto",
        type=CelestialBodyType.MOON,
        name=CALLISTO,
        mass=CALLISTO_MASS,
        radius=CALLISTO_RADIUS,
        parent_body=jupiter,
        relative_position=vector(*CALLISTO_RELATIVE_POSITION),
        relative_velocity=vector(*CALLISTO_RELATIVE_VELOCITY),
        colour=color.gray(0.5),
    )

    saturn = create_orbiting_body_from_state_vector(
        id="saturn",
        type=CelestialBodyType.PLANET,
        name=SATURN,
        mass=SATURN_MASS,
        radius=SATURN_RADIUS,
        parent_body=sun,
        relative_position=vector(*SATURN_RELATIVE_POSITION),
        relative_velocity=vector(*SATURN_RELATIVE_VELOCITY),
        colour=color.yellow,
    )

    mimas = create_orbiting_body_from_state_vector(
        id="saturn_mimas",
        type=CelestialBodyType.MOON,
        name=MIMAS,
        mass=MIMAS_MASS,
        radius=MIMAS_RADIUS,
        parent_body=saturn,
        relative_position=vector(*MIMAS_RELATIVE_POSITION),
        relative_velocity=vector(*MIMAS_RELATIVE_VELOCITY),
        colour=color.gray(0.6),
    )

    enceladus = create_orbiting_body_from_state_vector(
        id="saturn_enceladus",
        type=CelestialBodyType.MOON,
        name=ENCELADUS,
        mass=ENCELADUS_MASS,
        radius=ENCELADUS_RADIUS,
        parent_body=saturn,
        relative_position=vector(*ENCELADUS_RELATIVE_POSITION),
        relative_velocity=vector(*ENCELADUS_RELATIVE_VELOCITY),
        colour=color.white,
    )

    tethys = create_orbiting_body_from_state_vector(
        id="saturn_tethys",
        type=CelestialBodyType.MOON,
        name=TETHYS,
        mass=TETHYS_MASS,
        radius=TETHYS_RADIUS,
        parent_body=saturn,
        relative_position=vector(*TETHYS_RELATIVE_POSITION),
        relative_velocity=vector(*TETHYS_RELATIVE_VELOCITY),
        colour=color.gray(0.8),
    )

    dione = create_orbiting_body_from_state_vector(
        id="saturn_dione",
        type=CelestialBodyType.MOON,
        name=DIONE,
        mass=DIONE_MASS,
        radius=DIONE_RADIUS,
        parent_body=saturn,
        relative_position=vector(*DIONE_RELATIVE_POSITION),
        relative_velocity=vector(*DIONE_RELATIVE_VELOCITY),
        colour=color.gray(0.75),
    )

    rhea = create_orbiting_body_from_state_vector(
        id="saturn_rhea",
        type=CelestialBodyType.MOON,
        name=RHEA,
        mass=RHEA_MASS,
        radius=RHEA_RADIUS,
        parent_body=saturn,
        relative_position=vector(*RHEA_RELATIVE_POSITION),
        relative_velocity=vector(*RHEA_RELATIVE_VELOCITY),
        colour=color.gray(0.7),
    )

    titan = create_orbiting_body_from_state_vector(
        id="saturn_titan",
        type=CelestialBodyType.MOON,
        name=TITAN,
        mass=TITAN_MASS,
        radius=TITAN_RADIUS,
        parent_body=saturn,
        relative_position=vector(*TITAN_RELATIVE_POSITION),
        relative_velocity=vector(*TITAN_RELATIVE_VELOCITY),
        colour=color.orange,
    )

    iapetus = create_orbiting_body_from_state_vector(
        id="saturn_iapetus",
        type=CelestialBodyType.MOON,
        name=IAPETUS,
        mass=IAPETUS_MASS,
        radius=IAPETUS_RADIUS,
        parent_body=saturn,
        relative_position=vector(*IAPETUS_RELATIVE_POSITION),
        relative_velocity=vector(*IAPETUS_RELATIVE_VELOCITY),
        colour=color.gray(0.5),
    )

    uranus = create_orbiting_body_from_state_vector(
        id="uranus",
        type=CelestialBodyType.PLANET,
        name=URANUS,
        mass=URANUS_MASS,
        radius=URANUS_RADIUS,
        parent_body=sun,
        relative_position=vector(*URANUS_RELATIVE_POSITION),
        relative_velocity=vector(*URANUS_RELATIVE_VELOCITY),
        colour=color.cyan,
    )

    ariel = create_orbiting_body_from_state_vector(
        id="uranus_ariel",
        type=CelestialBodyType.MOON,
        name=ARIEL,
        mass=ARIEL_MASS,
        radius=ARIEL_RADIUS,
        parent_body=uranus,
        relative_position=vector(*ARIEL_RELATIVE_POSITION),
        relative_velocity=vector(*ARIEL_RELATIVE_VELOCITY),
        colour=color.gray(0.7),
    )

    umbriel = create_orbiting_body_from_state_vector(
        id="uranus_umbriel",
        type=CelestialBodyType.MOON,
        name=UMBRIEL,
        mass=UMBRIEL_MASS,
        radius=UMBRIEL_RADIUS,
        parent_body=uranus,
        relative_position=vector(*UMBRIEL_RELATIVE_POSITION),
        relative_velocity=vector(*UMBRIEL_RELATIVE_VELOCITY),
        colour=color.gray(0.5),
    )

    titania = create_orbiting_body_from_state_vector(
        id="uranus_titania",
        type=CelestialBodyType.MOON,
        name=TITANIA,
        mass=TITANIA_MASS,
        radius=TITANIA_RADIUS,
        parent_body=uranus,
        relative_position=vector(*TITANIA_RELATIVE_POSITION),
        relative_velocity=vector(*TITANIA_RELATIVE_VELOCITY),
        colour=color.gray(0.8),
    )

    oberon = create_orbiting_body_from_state_vector(
        id="uranus_oberon",
        type=CelestialBodyType.MOON,
        name=OBERON,
        mass=OBERON_MASS,
        radius=OBERON_RADIUS,
        parent_body=uranus,
        relative_position=vector(*OBERON_RELATIVE_POSITION),
        relative_velocity=vector(*OBERON_RELATIVE_VELOCITY),
        colour=color.gray(0.6),
    )

    miranda = create_orbiting_body_from_state_vector(
        id="uranus_miranda",
        type=CelestialBodyType.MOON,
        name=MIRANDA,
        mass=MIRANDA_MASS,
        radius=MIRANDA_RADIUS,
        parent_body=uranus,
        relative_position=vector(*MIRANDA_RELATIVE_POSITION),
        relative_velocity=vector(*MIRANDA_RELATIVE_VELOCITY),
        colour=color.gray(0.9),
    )

    neptune = create_orbiting_body_from_state_vector(
        id="neptune",
        type=CelestialBodyType.PLANET,
        name=NEPTUNE,
        mass=NEPTUNE_MASS,
        radius=NEPTUNE_RADIUS,
        parent_body=sun,
        relative_position=vector(*NEPTUNE_RELATIVE_POSITION),
        relative_velocity=vector(*NEPTUNE_RELATIVE_VELOCITY),
        colour=color.blue,
    )

    triton = create_orbiting_body_from_state_vector(
        id="neptune_triton",
        type=CelestialBodyType.MOON,
        name=TRITON,
        mass=TRITON_MASS,
        radius=TRITON_RADIUS,
        parent_body=neptune,
        relative_position=vector(*TRITON_RELATIVE_POSITION),
        relative_velocity=vector(*TRITON_RELATIVE_VELOCITY),
        colour=color.gray(0.8),
    )

    pluto = create_orbiting_body_from_state_vector(
        id="pluto",
        type=CelestialBodyType.DWARF_PLANET,
        name=PLUTO,
        mass=PLUTO_MASS,
        radius=PLUTO_RADIUS,
        parent_body=sun,
        relative_position=vector(*PLUTO_RELATIVE_POSITION),
        relative_velocity=vector(*PLUTO_RELATIVE_VELOCITY),
        colour=color.gray(0.7),
    )

    charon = create_orbiting_body_from_state_vector(
        id="pluto_charon",
        type=CelestialBodyType.MOON,
        name=CHARON,
        mass=CHARON_MASS,
        radius=CHARON_RADIUS,
        parent_body=pluto,
        relative_position=vector(*CHARON_RELATIVE_POSITION),
        relative_velocity=vector(*CHARON_RELATIVE_VELOCITY),
        colour=color.gray(0.6),
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
            phobos,
            deimos,
            jupiter,
            io,
            europa,
            ganymede,
            callisto,
            saturn,
            mimas,
            enceladus,
            tethys,
            dione,
            rhea,
            titan,
            iapetus,
            uranus,
            ariel,
            umbriel,
            titania,
            oberon,
            miranda,
            neptune,
            triton,
            pluto,
            charon,
        ],
    )
