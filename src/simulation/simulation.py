"""
Simulation runner for the astronomical simulator.
"""

from vpython import rate

from config.constants import (
    DEFAULT_DAYS_PER_SECOND,
    RENDER_RATE,
    SECONDS_IN_DAY,
)
from physics.physics_engine import PhysicsEngine


class Simulation:
    """
    Runs the gravitational simulation loop.
    """

    def __init__(self, bodies):
        self.bodies = bodies
        self.physics_engine = PhysicsEngine()
        self.is_paused = False
        self.days_per_second = DEFAULT_DAYS_PER_SECOND

    def run(self) -> None:
        """
        Starts the simulation loop.
        """
        while True:
            rate(RENDER_RATE)

            if not self.is_paused:
                self._update_bodies()

    def toggle_pause(self) -> None:
        self.is_paused = not self.is_paused

    def set_days_per_second(
        self,
        days_per_second: int,
    ) -> None:
        self.days_per_second = days_per_second

    def _get_time_step(self) -> float:
        return SECONDS_IN_DAY * self.days_per_second / RENDER_RATE

    def _update_bodies(self) -> None:
        """
        Updates all bodies using the gravitational effect of every other body.
        """
        time_step = self._get_time_step()
        accelerations = {}

        for body in self.bodies:
            total_acceleration = self._calculate_total_acceleration(body)
            accelerations[body] = total_acceleration

        for body in self.bodies:
            self.physics_engine.update_body_velocity(
                body,
                accelerations[body],
                time_step,
            )

        for body in self.bodies:
            self.physics_engine.update_body_position(body, time_step)

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
