"""
Helper function to create celestial bodies for presets.
"""

from math import cos, radians, sin

from vpython import vector

from models.celestial_body import CelestialBody, CelestialBodyType


def create_star(
    name: str,
    mass: float,
    radius: float,
    position: vector,
    velocity: vector,
    colour: vector,
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
    colour: vector,
    inclination_degrees: float,
    phase_degrees: float,
) -> CelestialBody:
    """
    Creates a planet orbiting a parent body.
    """
    return _create_orbiting_body(
        type=CelestialBodyType.PLANET,
        name=name,
        mass=mass,
        radius=radius,
        parent_body=parent_body,
        distance=distance,
        velocity=velocity,
        colour=colour,
        inclination_degrees=inclination_degrees,
        phase_degrees=phase_degrees,
    )


def create_moon(
    name: str,
    mass: float,
    radius: float,
    parent_body: CelestialBody,
    distance: float,
    velocity: float,
    colour: vector,
    inclination_degrees: float,
    phase_degrees: float,
) -> CelestialBody:
    """
    Creates a moon orbiting a parent body.
    """
    return _create_orbiting_body(
        type=CelestialBodyType.MOON,
        name=name,
        mass=mass,
        radius=radius,
        parent_body=parent_body,
        distance=distance,
        velocity=velocity,
        colour=colour,
        inclination_degrees=inclination_degrees,
        phase_degrees=phase_degrees,
    )


def _create_orbiting_body(
    type: CelestialBodyType,
    name: str,
    mass: float,
    radius: float,
    parent_body: CelestialBody,
    distance: float,
    velocity: float,
    colour: vector,
    inclination_degrees: float,
    phase_degrees: float,
) -> CelestialBody:
    """
    Creates a body using simple circular orbital elements.

    Position is placed relative to the parent.
    Velocity is tangent to the orbit and inherits the parent's velocity.
    """
    radial_direction = _calculate_radial_direction(
        inclination_degrees=inclination_degrees,
        phase_degrees=phase_degrees,
    )

    tangential_direction = _calculate_tangential_direction(
        inclination_degrees=inclination_degrees,
        phase_degrees=phase_degrees,
    )

    return CelestialBody(
        type=type,
        name=name,
        mass=mass,
        radius=radius,
        position=parent_body.position + radial_direction * distance,
        velocity=parent_body.velocity + tangential_direction * velocity,
        colour=colour,
        make_trail=True,
        parent_body=parent_body,
    )


def _calculate_radial_direction(
    inclination_degrees: float,
    phase_degrees: float,
) -> vector:
    """
    Calculates the orbital radial direction from inclination and phase.
    """
    inclination = radians(inclination_degrees)
    phase = radians(phase_degrees)

    return vector(
        cos(phase),
        sin(phase) * cos(inclination),
        sin(phase) * sin(inclination),
    )


def _calculate_tangential_direction(
    inclination_degrees: float,
    phase_degrees: float,
) -> vector:
    """
    Calculates the orbital tangential direction from inclination and phase.
    """
    inclination = radians(inclination_degrees)
    phase = radians(phase_degrees)

    return vector(
        -sin(phase),
        cos(phase) * cos(inclination),
        cos(phase) * sin(inclination),
    )
