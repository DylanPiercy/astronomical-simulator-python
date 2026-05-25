"""
This file contains preset CelestialBody objects for the Alpha Centauri system.
"""

from vpython import color, vector

from config.alpha_centauri_data import (
    ALPHA_CENTAURI_A,
    ALPHA_CENTAURI_A_AVERAGE_DISTANCE,
    ALPHA_CENTAURI_A_AVERAGE_VELOCITY,
    ALPHA_CENTAURI_A_MASS,
    ALPHA_CENTAURI_A_RADIUS,
    ALPHA_CENTAURI_B,
    ALPHA_CENTAURI_B_AVERAGE_DISTANCE,
    ALPHA_CENTAURI_B_AVERAGE_VELOCITY,
    ALPHA_CENTAURI_B_MASS,
    ALPHA_CENTAURI_B_RADIUS,
    PROXIMA_CENTAURI,
    PROXIMA_CENTAURI_AVERAGE_DISTANCE,
    PROXIMA_CENTAURI_AVERAGE_VELOCITY,
    PROXIMA_CENTAURI_B,
    PROXIMA_CENTAURI_B_AVERAGE_DISTANCE,
    PROXIMA_CENTAURI_B_AVERAGE_VELOCITY,
    PROXIMA_CENTAURI_B_MASS,
    PROXIMA_CENTAURI_B_RADIUS,
    PROXIMA_CENTAURI_C,
    PROXIMA_CENTAURI_C_AVERAGE_DISTANCE,
    PROXIMA_CENTAURI_C_AVERAGE_VELOCITY,
    PROXIMA_CENTAURI_C_MASS,
    PROXIMA_CENTAURI_C_RADIUS,
    PROXIMA_CENTAURI_D,
    PROXIMA_CENTAURI_D_AVERAGE_DISTANCE,
    PROXIMA_CENTAURI_D_AVERAGE_VELOCITY,
    PROXIMA_CENTAURI_D_MASS,
    PROXIMA_CENTAURI_D_RADIUS,
    PROXIMA_CENTAURI_MASS,
    PROXIMA_CENTAURI_RADIUS,
)
from models.celestial_body import CelestialBody, CelestialBodyType
from models.solar_system import SolarSystem
from presets.preset_creation_helpers import create_star


def create_alpha_centauri_system() -> SolarSystem:
    """
    Creates the preset celestial bodies for the Alpha Centauri system.
    """

    alpha_centauri_a = create_star(
        name=ALPHA_CENTAURI_A,
        mass=ALPHA_CENTAURI_A_MASS,
        radius=ALPHA_CENTAURI_A_RADIUS,
        position=vector(-ALPHA_CENTAURI_A_AVERAGE_DISTANCE, 0, 0),
        velocity=vector(0, -ALPHA_CENTAURI_A_AVERAGE_VELOCITY, 0),
        colour=color.yellow,
    )

    alpha_centauri_b = create_star(
        name=ALPHA_CENTAURI_B,
        mass=ALPHA_CENTAURI_B_MASS,
        radius=ALPHA_CENTAURI_B_RADIUS,
        position=vector(ALPHA_CENTAURI_B_AVERAGE_DISTANCE, 0, 0),
        velocity=vector(0, ALPHA_CENTAURI_B_AVERAGE_VELOCITY, 0),
        colour=color.orange,
    )

    proxima_centauri = create_star(
        name=PROXIMA_CENTAURI,
        mass=PROXIMA_CENTAURI_MASS,
        radius=PROXIMA_CENTAURI_RADIUS,
        position=vector(PROXIMA_CENTAURI_AVERAGE_DISTANCE, 0, 0),
        velocity=vector(0, PROXIMA_CENTAURI_AVERAGE_VELOCITY, 0),
        colour=color.red,
    )

    proxima_d = _create_proxima_planet(
        name=PROXIMA_CENTAURI_D,
        mass=PROXIMA_CENTAURI_D_MASS,
        radius=PROXIMA_CENTAURI_D_RADIUS,
        distance=PROXIMA_CENTAURI_D_AVERAGE_DISTANCE,
        velocity=PROXIMA_CENTAURI_D_AVERAGE_VELOCITY,
        colour=color.gray(0.6),
    )

    proxima_b = _create_proxima_planet(
        name=PROXIMA_CENTAURI_B,
        mass=PROXIMA_CENTAURI_B_MASS,
        radius=PROXIMA_CENTAURI_B_RADIUS,
        distance=PROXIMA_CENTAURI_B_AVERAGE_DISTANCE,
        velocity=PROXIMA_CENTAURI_B_AVERAGE_VELOCITY,
        colour=color.blue,
    )

    proxima_c = _create_proxima_planet(
        name=PROXIMA_CENTAURI_C,
        mass=PROXIMA_CENTAURI_C_MASS,
        radius=PROXIMA_CENTAURI_C_RADIUS,
        distance=PROXIMA_CENTAURI_C_AVERAGE_DISTANCE,
        velocity=PROXIMA_CENTAURI_C_AVERAGE_VELOCITY,
        colour=color.cyan,
    )

    return SolarSystem(
        name="Alpha Centauri System",
        bodies=[
            alpha_centauri_a,
            alpha_centauri_b,
            proxima_centauri,
            proxima_d,
            proxima_b,
            proxima_c,
        ],
    )


def _create_proxima_planet(
    name: str,
    mass: float,
    radius: float,
    distance: float,
    velocity: float,
    colour,
) -> CelestialBody:
    """
    Creates a planet orbiting Proxima Centauri in the X/Z plane.
    """
    return CelestialBody(
        type=CelestialBodyType.PLANET,
        name=name,
        mass=mass,
        radius=radius,
        position=vector(
            PROXIMA_CENTAURI_AVERAGE_DISTANCE,
            0,
            distance,
        ),
        velocity=vector(
            velocity,
            PROXIMA_CENTAURI_AVERAGE_VELOCITY,
            0,
        ),
        colour=colour,
        make_trail=True,
    )
