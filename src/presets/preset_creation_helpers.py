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
    inclination_degrees: float = 0,
    phase_degrees: float = 0,
    longitude_of_ascending_node_degrees: float = 0,
) -> CelestialBody:
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
        longitude_of_ascending_node_degrees=longitude_of_ascending_node_degrees,
    )


def create_moon(
    name: str,
    mass: float,
    radius: float,
    parent_body: CelestialBody,
    distance: float,
    velocity: float,
    colour: vector,
    inclination_degrees: float = 0,
    phase_degrees: float = 0,
    longitude_of_ascending_node_degrees: float = 0,
) -> CelestialBody:
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
        longitude_of_ascending_node_degrees=longitude_of_ascending_node_degrees,
    )


def create_orbiting_body_from_state_vector(
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
    longitude_of_ascending_node_degrees: float,
) -> CelestialBody:
    radial_direction = _calculate_radial_direction(
        inclination_degrees=inclination_degrees,
        phase_degrees=phase_degrees,
        longitude_of_ascending_node_degrees=longitude_of_ascending_node_degrees,
    )

    tangential_direction = _calculate_tangential_direction(
        inclination_degrees=inclination_degrees,
        phase_degrees=phase_degrees,
        longitude_of_ascending_node_degrees=longitude_of_ascending_node_degrees,
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
    longitude_of_ascending_node_degrees: float,
) -> vector:
    inclination = radians(inclination_degrees)
    phase = radians(phase_degrees)
    longitude_of_ascending_node = radians(longitude_of_ascending_node_degrees)

    return _rotate_orbital_plane_vector(
        vector(cos(phase), sin(phase), 0),
        inclination,
        longitude_of_ascending_node,
    )


def _calculate_tangential_direction(
    inclination_degrees: float,
    phase_degrees: float,
    longitude_of_ascending_node_degrees: float,
) -> vector:
    inclination = radians(inclination_degrees)
    phase = radians(phase_degrees)
    longitude_of_ascending_node = radians(longitude_of_ascending_node_degrees)

    return _rotate_orbital_plane_vector(
        vector(-sin(phase), cos(phase), 0),
        inclination,
        longitude_of_ascending_node,
    )


def _rotate_orbital_plane_vector(
    base_vector: vector,
    inclination: float,
    longitude_of_ascending_node: float,
) -> vector:
    x = base_vector.x
    y = base_vector.y
    z = base_vector.z

    inclined_vector = vector(
        x,
        y * cos(inclination) - z * sin(inclination),
        y * sin(inclination) + z * cos(inclination),
    )

    return vector(
        inclined_vector.x * cos(longitude_of_ascending_node)
        - inclined_vector.y * sin(longitude_of_ascending_node),
        inclined_vector.x * sin(longitude_of_ascending_node)
        + inclined_vector.y * cos(longitude_of_ascending_node),
        inclined_vector.z,
    )
