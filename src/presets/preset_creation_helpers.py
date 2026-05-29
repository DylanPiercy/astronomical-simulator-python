"""
Helper function to create celestial bodies for presets.
"""

from vpython import vector

from models.celestial_body import CelestialBody, CelestialBodyType


def create_star(
    id: str,
    name: str,
    mass: float,
    radius: float,
    position: vector,
    velocity: vector,
    colour: vector,
) -> CelestialBody:
    return CelestialBody(
        id=id,
        type=CelestialBodyType.STAR,
        name=name,
        mass=mass,
        radius=radius,
        position=position,
        velocity=velocity,
        colour=colour,
        make_trail=True,
    )


def create_orbiting_body_from_state_vector(
    id: str,
    type: CelestialBodyType,
    name: str,
    mass: float,
    radius: float,
    parent_body: CelestialBody,
    relative_position: vector,
    relative_velocity: vector,
    colour: vector,
) -> CelestialBody:
    """
    Creates an orbiting body from a real relative state vector.
    """
    return CelestialBody(
        id=id,
        type=type,
        name=name,
        mass=mass,
        radius=radius,
        position=parent_body.position + relative_position,
        velocity=parent_body.velocity + relative_velocity,
        colour=colour,
        make_trail=True,
        parent_body=parent_body,
    )
