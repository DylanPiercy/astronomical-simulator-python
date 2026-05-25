"""
Physics engine for calculating gravitational motion.
"""

from vpython import vector

from config.constants import GRAVITATIONAL_CONSTANT


class PhysicsEngine:
    """
    Handles Newtonian gravity calculations between celestial bodies.
    """

    @staticmethod
    def calculate_gravitational_acceleration(body, other_body) -> vector:
        """
        Calculates the acceleration applied to one body by another body.
        """
        displacement = other_body.position - body.position
        distance = displacement.mag

        if distance == 0:
            return vector(0, 0, 0)

        direction = displacement.norm()
        acceleration_magnitude = GRAVITATIONAL_CONSTANT * other_body.mass / distance**2

        return direction * acceleration_magnitude

    @staticmethod
    def update_body_velocity(body, acceleration: vector, time_step: float) -> None:
        """
        Updates a body's velocity using acceleration and time step.
        """
        body.velocity += acceleration * time_step

    @staticmethod
    def update_body_position(body, time_step: float) -> None:
        """
        Updates a body's position using velocity and time step.
        """
        body.position += body.velocity * time_step
        body.update_visual_position()
