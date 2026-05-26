"""
VPython UI controls for the astronomical simulator.
"""

from typing import Any

from vpython import button, menu, scene, slider, wtext

from config.constants import (
    DEFAULT_DAYS_PER_SECOND,
    MAX_DAYS_PER_SECOND,
    MIN_DAYS_PER_SECOND,
)
from models.celestial_body import VisualScalingMode


class SimulationControls:
    """
    Creates UI controls for pausing, changing simulation speed, camera focus,
    and visual scaling.
    """

    def __init__(self, simulation):
        self.simulation = simulation
        self.pause_button: Any = None
        self.speed_text: Any = None
        self.scaling_button: Any = None
        self.scaling_text: Any = None
        self.camera_focus_menu: Any = None
        self.camera_focus_button: Any = None
        self.selected_camera_focus_name = "Center"

    def setup(self) -> None:
        """
        Adds simulation controls to the VPython scene.
        """
        scene.append_to_caption("\n\n")

        self.pause_button = button(text="Pause", bind=self._toggle_pause)

        scene.append_to_caption("  Simulated days per second: ")

        slider(
            min=MIN_DAYS_PER_SECOND,
            max=MAX_DAYS_PER_SECOND,
            value=DEFAULT_DAYS_PER_SECOND,
            step=1,
            bind=self._update_simulation_speed,
        )

        scene.append_to_caption("  ")
        self.speed_text = wtext(text=self._simulation_speed_label())

        scene.append_to_caption("\nVisual scaling: ")
        self.scaling_text = wtext(text=self._visual_scaling_label())

        scene.append_to_caption(" ")

        self.scaling_button = button(
            text="Switch to realistic",
            bind=self._toggle_visual_scaling,
        )

        scene.append_to_caption("\nCamera focus: ")

        self.camera_focus_menu = menu(
            choices=self._get_camera_focus_choices(),
            selected="Center",
            bind=self._select_camera_focus,
        )

        scene.append_to_caption(" ")

        self.camera_focus_button = button(
            text="Focus camera",
            bind=self._apply_camera_focus,
        )

        scene.append_to_caption("\nControls: Press SPACE to pause/resume.")

        scene.bind("keydown", self._handle_key_down)

    def _toggle_pause(self, _event=None) -> None:
        self.simulation.toggle_pause()
        self.pause_button.text = "Resume" if self.simulation.is_paused else "Pause"

    def _update_simulation_speed(self, event) -> None:
        self.simulation.set_days_per_second(int(event.value))
        self.speed_text.text = self._simulation_speed_label()

    def _toggle_visual_scaling(self, _event=None) -> None:
        """
        Toggles between artistic and realistic visual scaling.
        """
        if self.simulation.visual_scaling_mode == VisualScalingMode.ARTISTIC:
            self.simulation.set_visual_scaling_mode(VisualScalingMode.REALISTIC)
            self.scaling_button.text = "Switch to artistic"
        else:
            self.simulation.set_visual_scaling_mode(VisualScalingMode.ARTISTIC)
            self.scaling_button.text = "Switch to realistic"

        self.scaling_text.text = self._visual_scaling_label()

    def _select_camera_focus(self, event) -> None:
        """
        Stores the selected camera focus option without applying it immediately.
        """
        self.selected_camera_focus_name = event.selected

    def _apply_camera_focus(self, _event=None) -> None:
        """
        Applies the selected camera focus option.
        """
        selected_name = self.selected_camera_focus_name

        if selected_name == "Center":
            self.simulation.set_camera_focus_body(None)
            return

        selected_body = next(
            body for body in self.simulation.bodies if body.name == selected_name
        )
        self.simulation.set_camera_focus_body(selected_body)

    def _handle_key_down(self, event) -> None:
        key = str(event.key).lower()

        if key == " ":
            self._toggle_pause()

    def _simulation_speed_label(self) -> str:
        return f"{self.simulation.days_per_second} simulated day(s) per second"

    def _visual_scaling_label(self) -> str:
        return self.simulation.visual_scaling_mode.value

    def _get_camera_focus_choices(self) -> list[str]:
        return ["Center"] + [body.name for body in self.simulation.bodies]
