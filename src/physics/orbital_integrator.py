"""
Orbital integration logic for updating celestial body motion.
"""

from vpython import vector

from physics.physics_engine import PhysicsEngine


class OrbitalIntegrator:
    """
    Updates celestial body motion using Leapfrog integration.
    """

    def __init__(self, physics_engine: PhysicsEngine):
        self.physics_engine = physics_engine

    def update_bodies(self, bodies, time_step: float) -> None:
        """
        Updates all bodies using Leapfrog integration.

        Steps:
        1. Calculate current accelerations.
        2. Update velocities by half a timestep.
        3. Update positions by a full timestep.
        4. Recalculate accelerations.
        5. Update velocities by another half timestep.
        """
        half_time_step = time_step / 2

        current_accelerations = self._calculate_all_accelerations(bodies)

        for body in bodies:
            self.physics_engine.update_body_velocity(
                body,
                current_accelerations[body],
                half_time_step,
            )

        for body in bodies:
            self.physics_engine.update_body_position(body, time_step)

        updated_accelerations = self._calculate_all_accelerations(bodies)

        for body in bodies:
            self.physics_engine.update_body_velocity(
                body,
                updated_accelerations[body],
                half_time_step,
            )

    def _calculate_all_accelerations(self, bodies) -> dict:
        """
        Calculates total acceleration for every body.
        """
        return {
            body: self._calculate_total_acceleration(body, bodies) for body in bodies
        }

    def _calculate_total_acceleration(self, body, bodies):
        """
        Calculates the total acceleration applied to a body by all other bodies.
        """
        total_acceleration = vector(0, 0, 0)

        for other_body in bodies:
            if other_body == body:
                continue

            total_acceleration += (
                self.physics_engine.calculate_gravitational_acceleration(
                    body,
                    other_body,
                )
            )

        return total_acceleration
