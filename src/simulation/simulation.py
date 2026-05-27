"""
Simulation runner for the astronomical simulator.
"""

from datetime import datetime, timedelta
from typing import Optional

from vpython import mag, rate, scene, vector

from config.constants import (
    DEFAULT_DAYS_PER_SECOND,
    EPOCH_START,
    RENDER_RATE,
    SECONDS_IN_DAY,
)
from models.celestial_body import CelestialBody, VisualScalingMode
from physics.orbital_integrator import OrbitalIntegrator
from physics.physics_diagnostics import PhysicsDiagnostics
from physics.physics_engine import PhysicsEngine
from ui.body_label import BodyLabel


class Simulation:
    """
    Runs the gravitational simulation loop.
    """

    def __init__(self, bodies):
        self.bodies = bodies
        self.physics_engine = PhysicsEngine()
        self.orbital_integrator = OrbitalIntegrator(self.physics_engine)
        self.physics_diagnostics = PhysicsDiagnostics()

        self.is_paused = False
        self.days_per_second = DEFAULT_DAYS_PER_SECOND
        self.camera_focus_body: Optional[CelestialBody] = None
        self.visual_scaling_mode = VisualScalingMode.ARTISTIC
        self.trails_enabled = True

        self.epoch_start = datetime.strptime(EPOCH_START, "%Y-%b-%d %H:%M")
        self.simulated_elapsed_seconds = 0

        self.body_hover_label = BodyLabel(self.bodies)
        self.simulation_date_text = None
        self.system_diagnostics_text = None
        self.diagnostics_frame_counter = 0

        scene.bind("click", self._handle_scene_click)

    def run(self) -> None:
        """
        Starts the simulation loop.
        """
        while True:
            rate(RENDER_RATE)

            if not self.is_paused:
                self._update_bodies()

            self._update_camera_focus()
            self.body_hover_label.update()
            self._update_simulation_date_panel()
            self._update_system_diagnostics_panel()

    def toggle_pause(self) -> None:
        self.is_paused = not self.is_paused

    def set_days_per_second(
        self,
        days_per_second: int,
    ) -> None:
        self.days_per_second = days_per_second

    def set_camera_focus_body(self, body: Optional[CelestialBody]) -> None:
        self.camera_focus_body = body

    def set_visual_scaling_mode(self, visual_scaling_mode: VisualScalingMode) -> None:
        """
        Updates the visual scaling mode for all bodies.
        """
        self.visual_scaling_mode = visual_scaling_mode

        for body in self.bodies:
            body.set_visual_scaling_mode(visual_scaling_mode)

    def set_trails_enabled(self, trails_enabled: bool) -> None:
        self.trails_enabled = trails_enabled

        for body in self.bodies:
            body.set_trails_enabled(trails_enabled)

    def set_simulation_date_text(self, simulation_date_text) -> None:
        self.simulation_date_text = simulation_date_text
        self._update_simulation_date_panel()

    def set_system_diagnostics_text(self, system_diagnostics_text) -> None:
        """
        Stores the UI text widget used to display system diagnostics.
        """
        self.system_diagnostics_text = system_diagnostics_text

    def _handle_scene_click(self, _event=None) -> None:
        """
        Handles clicking bodies to pin or unpin labels.
        """
        self.body_hover_label.handle_click()

    def _get_time_step(self) -> float:
        return SECONDS_IN_DAY * self.days_per_second / RENDER_RATE

    def _update_bodies(self) -> None:
        """
        Updates all bodies using the physics-layer orbital integrator.
        """
        time_step = self._get_time_step()

        self.orbital_integrator.update_bodies(
            self.bodies,
            time_step,
        )

        self.simulated_elapsed_seconds += time_step

    def _update_camera_focus(self) -> None:
        """
        Updates the camera center to follow the selected body.
        """
        if self.camera_focus_body is None:
            scene.center = vector(0, 0, 0)
            return

        scene.center = self.camera_focus_body.visual.pos

    def _update_simulation_date_panel(self) -> None:
        """
        Updates the current simulation date UI panel.
        """
        if self.simulation_date_text is None:
            return

        current_date = self.epoch_start + timedelta(
            seconds=self.simulated_elapsed_seconds
        )

        self.simulation_date_text.text = (
            f"\nSimulation date: {current_date:%Y-%m-%d %H:%M:%S} UTC"
        )

    def _update_system_diagnostics_panel(self) -> None:
        """
        Updates the system diagnostics UI panel once per second.
        """
        if self.system_diagnostics_text is None:
            return

        self.diagnostics_frame_counter += 1

        if self.diagnostics_frame_counter < RENDER_RATE:
            return

        self.diagnostics_frame_counter = 0
        snapshot = self.physics_diagnostics.calculate_snapshot(self.bodies)

        self.system_diagnostics_text.text = (
            "\n\nSystem diagnostics"
            f"\nBodies: {len(self.bodies)}"
            f"\nTotal kinetic energy: {snapshot.kinetic_energy:.3e} J"
            f"\nTotal potential energy: {snapshot.potential_energy:.3e} J"
            f"\nTotal mechanical energy: {snapshot.total_energy:.3e} J"
            f"\nTotal momentum: {mag(snapshot.linear_momentum):.3e} kg m/s"
        )
