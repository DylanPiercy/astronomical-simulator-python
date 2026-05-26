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


class SimulationControls:
    """
    Creates UI controls for pausing, changing simulation speed, and camera focus.
    """

    def __init__(self, simulation):
        self.simulation = simulation
        self.pause_button: Any = None
        self.speed_text: Any = None
        self.camera_focus_menu: Any = None

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

        scene.append_to_caption("\nCamera focus: ")

        self.camera_focus_menu = menu(
            choices=self._get_camera_focus_choices(),
            selected="Center",
            bind=self._update_camera_focus,
        )

        scene.append_to_caption(
            "\nControls: click the scene once, then press Space to pause/resume."
        )

        scene.bind("keydown", self._handle_key_down)

    def _toggle_pause(self, _event=None) -> None:
        self.simulation.toggle_pause()
        self.pause_button.text = "Resume" if self.simulation.is_paused else "Pause"

    def _update_simulation_speed(self, event) -> None:
        self.simulation.set_days_per_second(int(event.value))
        self.speed_text.text = self._simulation_speed_label()

    def _update_camera_focus(self, event) -> None:
        """
        Updates the camera focus based on the selected dropdown option.
        """
        selected_name = event.selected

        if selected_name == "Center":
            self.simulation.set_camera_focus_body(None)
            return

        selected_body = next(
            body for body in self.simulation.bodies if body.name == selected_name
        )
        self.simulation.set_camera_focus_body(selected_body)

    def _handle_key_down(self, event) -> None:
        """
        Toggles pause when the space bar is pressed.
        """
        key = str(event.key)

        if key == " ":
            self._toggle_pause()

    def _simulation_speed_label(self) -> str:
        return f"{self.simulation.days_per_second} " "simulated day(s) per second"

    def _get_camera_focus_choices(self) -> list[str]:
        return ["Center"] + [body.name for body in self.simulation.bodies]
