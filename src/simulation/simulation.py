"""
Simulation runner for the astronomical simulator.
"""

from typing import Optional

from vpython import rate, scene, vector

from config.constants import (
    DEFAULT_DAYS_PER_SECOND,
    RENDER_RATE,
    SECONDS_IN_DAY,
)
from models.celestial_body import CelestialBody, VisualScalingMode
from physics.physics_engine import PhysicsEngine
from ui.body_label import BodyLabel


class Simulation:
    """
    Runs the gravitational simulation loop.
    """

    def __init__(self, bodies):
        self.bodies = bodies
        self.physics_engine = PhysicsEngine()
        self.is_paused = False
        self.days_per_second = DEFAULT_DAYS_PER_SECOND
        self.camera_focus_body: Optional[CelestialBody] = None
        self.visual_scaling_mode = VisualScalingMode.ARTISTIC
        self.trails_enabled = True
        self.body_hover_label = BodyLabel(self.bodies)

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

    def toggle_pause(self) -> None:
        self.is_paused = not self.is_paused

    def set_days_per_second(
        self,
        days_per_second: int,
    ) -> None:
        self.days_per_second = days_per_second

    def set_camera_focus_body(self, body: Optional[CelestialBody]) -> None:
        """
        Sets the body the camera should follow.

        If body is None, the camera focuses on the system center.
        """
        self.camera_focus_body = body

    def set_visual_scaling_mode(self, visual_scaling_mode: VisualScalingMode) -> None:
        self.visual_scaling_mode = visual_scaling_mode

        for body in self.bodies:
            body.set_visual_scaling_mode(visual_scaling_mode)

    def set_trails_enabled(self, trails_enabled: bool) -> None:
        self.trails_enabled = trails_enabled

        for body in self.bodies:
            body.set_trails_enabled(trails_enabled)

    def _handle_scene_click(self, _event=None) -> None:
        """
        Handles clicking bodies to pin or unpin labels.
        """
        self.body_hover_label.handle_click()

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

    def _update_camera_focus(self) -> None:
        """
        Updates the camera center to follow the selected body.
        """
        if self.camera_focus_body is None:
            scene.center = vector(0, 0, 0)
            return

        scene.center = self.camera_focus_body.visual.pos
