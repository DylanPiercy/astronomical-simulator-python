"""
Physics diagnostics for checking simulation stability.
"""

from dataclasses import dataclass

from vpython import mag, vector

from config.constants import GRAVITATIONAL_CONSTANT


@dataclass
class PhysicsDiagnosticsSnapshot:
    kinetic_energy: float
    potential_energy: float
    total_energy: float
    linear_momentum: vector


class PhysicsDiagnostics:
    """
    Calculates system-wide energy and momentum diagnostics.
    """

    def calculate_snapshot(self, bodies) -> PhysicsDiagnosticsSnapshot:
        kinetic_energy = self._calculate_total_kinetic_energy(bodies)
        potential_energy = self._calculate_total_potential_energy(bodies)
        linear_momentum = self._calculate_total_linear_momentum(bodies)

        return PhysicsDiagnosticsSnapshot(
            kinetic_energy=kinetic_energy,
            potential_energy=potential_energy,
            total_energy=kinetic_energy + potential_energy,
            linear_momentum=linear_momentum,
        )

    def _calculate_total_kinetic_energy(self, bodies) -> float:
        total_kinetic_energy = 0

        for body in bodies:
            speed = mag(body.velocity)
            total_kinetic_energy += 0.5 * body.mass * speed**2

        return total_kinetic_energy

    def _calculate_total_potential_energy(self, bodies) -> float:
        total_potential_energy = 0

        for index, body in enumerate(bodies):
            for other_body in bodies[index + 1 :]:
                distance = mag(other_body.position - body.position)

                if distance == 0:
                    continue

                total_potential_energy -= (
                    GRAVITATIONAL_CONSTANT * body.mass * other_body.mass / distance
                )

        return total_potential_energy

    def _calculate_total_linear_momentum(self, bodies) -> vector:
        total_momentum = vector(0, 0, 0)

        for body in bodies:
            total_momentum += body.velocity * body.mass

        return total_momentum
