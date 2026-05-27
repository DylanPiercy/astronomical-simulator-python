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
    parent_body: CelestialBody,
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
        position=vector(
            parent_body.position.x + distance,
            parent_body.position.y,
            parent_body.position.z,
        ),
        velocity=vector(
            parent_body.velocity.x,
            parent_body.velocity.y + velocity,
            parent_body.velocity.z,
        ),
        colour=colour,
        make_trail=True,
        parent_body=parent_body,
    )


def create_moon(
    name: str,
    mass: float,
    radius: float,
    parent_body: CelestialBody,
    distance: float,
    velocity: float,
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
            parent_body.position.x,
            parent_body.position.y,
            parent_body.position.z + distance,
        ),
        velocity=vector(
            parent_body.velocity.x + velocity,
            parent_body.velocity.y,
            parent_body.velocity.z,
        ),
        colour=colour,
        make_trail=True,
        parent_body=parent_body,
    )
