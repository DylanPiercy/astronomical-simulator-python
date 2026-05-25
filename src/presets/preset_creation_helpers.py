"""
Helper function to create celestial bodies for presets.
"""

from vpython import vector

from models.celestial_body import CelestialBody, CelestialBodyType


def create_star(
    name: str,
    mass: float,
    radius: float,
    position: vector,
    velocity: vector,
    colour,
) -> CelestialBody:
    return CelestialBody(
        type=CelestialBodyType.STAR,
        name=name,
        mass=mass,
        radius=radius,
        position=position,
        velocity=velocity,
        colour=colour,
        make_trail=True,
    )


def create_planet(
    name: str,
    mass: float,
    radius: float,
    distance: float,
    velocity: float,
    colour,
) -> CelestialBody:
    """
    Creates a planet orbiting a parent body in the X/Y plane.
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


def create_moon(
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
