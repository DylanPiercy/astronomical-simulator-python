"""
Physics diagnostics for checking simulation stability.
"""

from dataclasses import dataclass
from typing import Optional

from vpython import mag, vector

from config.constants import GRAVITATIONAL_CONSTANT


@dataclass
class BodyDiagnosticsSnapshot:
    """
    Stores calculated physics diagnostics for one celestial body.
    """

    speed: float
    kinetic_energy: float
    linear_momentum: vector
    linear_momentum_magnitude: float
    parent_distance: Optional[float]


@dataclass
class SystemDiagnosticsSnapshot:
    """
    Stores calculated physics diagnostics for the full simulation system.
    """

    kinetic_energy: float
    potential_energy: float
    total_energy: float
    linear_momentum: vector


class PhysicsDiagnostics:
    """
    Calculates body-specific and system-wide physics diagnostics.
    """

    def calculate_body_snapshot(self, body) -> BodyDiagnosticsSnapshot:
        """
        Calculates physics diagnostics for a single body.
        """
        speed = mag(body.velocity)
        linear_momentum = body.velocity * body.mass

        parent_distance = None

        if body.parent_body is not None:
            parent_distance = mag(body.position - body.parent_body.position)

        return BodyDiagnosticsSnapshot(
            speed=speed,
            kinetic_energy=0.5 * body.mass * speed**2,
            linear_momentum=linear_momentum,
            linear_momentum_magnitude=mag(linear_momentum),
            parent_distance=parent_distance,
        )

    def calculate_snapshot(self, bodies) -> SystemDiagnosticsSnapshot:
        """
        Calculates the current total kinetic energy, potential energy,
        total mechanical energy, and linear momentum.
        """
        kinetic_energy = self._calculate_total_kinetic_energy(bodies)
        potential_energy = self._calculate_total_potential_energy(bodies)
        linear_momentum = self._calculate_total_linear_momentum(bodies)

        return SystemDiagnosticsSnapshot(
            kinetic_energy=kinetic_energy,
            potential_energy=potential_energy,
            total_energy=kinetic_energy + potential_energy,
            linear_momentum=linear_momentum,
        )

    def _calculate_total_kinetic_energy(self, bodies) -> float:
        """
        Calculates total kinetic energy for all bodies.
        """
        total_kinetic_energy = 0

        for body in bodies:
            body_snapshot = self.calculate_body_snapshot(body)
            total_kinetic_energy += body_snapshot.kinetic_energy

        return total_kinetic_energy

    def _calculate_total_potential_energy(self, bodies) -> float:
        """
        Calculates total gravitational potential energy for all unique body pairs.
        """
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
        """
        Calculates total linear momentum for all bodies.
        """
        total_momentum = vector(0, 0, 0)

        for body in bodies:
            body_snapshot = self.calculate_body_snapshot(body)
            total_momentum += body_snapshot.linear_momentum

        return total_momentum
