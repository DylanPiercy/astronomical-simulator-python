"""
VPython UI controls for the astronomical simulator.
"""

from typing import Any
from vpython import button, scene, slider, wtext

from config.constants import DEFAULT_UPDATE_RATE, MAX_UPDATE_RATE, MIN_UPDATE_RATE


class SimulationControls:
    """
    Creates UI controls for pausing and changing simulation speed.
    """

    def __init__(self, simulation):
        self.simulation = simulation
        self.pause_button: Any = None
        self.speed_text: Any = None

    def setup(self) -> None:
        """
        Adds simulation controls to the VPython scene.
        """
        scene.append_to_caption("\n\n")

        self.pause_button = button(text="Pause", bind=self._toggle_pause)

        scene.append_to_caption("  Updates per second: ")

        slider(
            min=MIN_UPDATE_RATE,
            max=MAX_UPDATE_RATE,
            value=DEFAULT_UPDATE_RATE,
            step=1,
            bind=self._update_rate,
        )

        scene.append_to_caption("  ")
        self.speed_text = wtext(text=self._update_rate_label())

        scene.bind("keydown", self._handle_key_down)

    def _toggle_pause(self, _event=None) -> None:
        self.simulation.toggle_pause()
        self.pause_button.text = "Resume" if self.simulation.is_paused else "Pause"

    def _update_rate(self, event) -> None:
        self.simulation.set_update_rate(int(event.value))
        self.speed_text.text = self._update_rate_label()

    def _handle_key_down(self, event) -> None:
        """
        Toggles pause when the space bar is pressed.
        """
        key = str(event.key).lower()

        if key == " ":
            self._toggle_pause()

    def _update_rate_label(self) -> str:
        return f"{self.simulation.update_rate} simulated day(s) per second"
