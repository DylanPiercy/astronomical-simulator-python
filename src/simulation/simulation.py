"""
Simulation runner for the astronomical simulator.
"""

from vpython import rate

from config.constants import DEFAULT_UPDATE_RATE, TIME_STEP
from physics.physics_engine import PhysicsEngine


class Simulation:
    """
    Runs the gravitational simulation loop.
    """

    def __init__(self, bodies):
        self.bodies = bodies
        self.physics_engine = PhysicsEngine()
        self.is_paused = False
        self.update_rate = DEFAULT_UPDATE_RATE

    def run(self) -> None:
        """
        Starts the simulation loop.
        """
        while True:
            rate(self.update_rate)

            if not self.is_paused:
                self._update_bodies()

    def toggle_pause(self) -> None:
        self.is_paused = not self.is_paused

    def set_update_rate(self, update_rate: int) -> None:
        self.update_rate = update_rate

    def _update_bodies(self) -> None:
        """
        Updates all bodies using the gravitational effect of every other body.
        """
        accelerations = {}

        for body in self.bodies:
            total_acceleration = self._calculate_total_acceleration(body)
            accelerations[body] = total_acceleration

        for body in self.bodies:
            self.physics_engine.update_body_velocity(
                body,
                accelerations[body],
                TIME_STEP,
            )

        for body in self.bodies:
            self.physics_engine.update_body_position(body, TIME_STEP)

    def _calculate_total_acceleration(self, body):
        """
        Calculates the total acceleration applied to a body by all other bodies.
        """
        total_acceleration = None

        for other_body in self.bodies:
            if other_body == body:
                continue

            acceleration = self.physics_engine.calculate_gravitational_acceleration(
                body,
                other_body,
            )

            if total_acceleration is None:
                total_acceleration = acceleration
            else:
                total_acceleration += acceleration

        return total_acceleration
