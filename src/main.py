"""
Entry point for the astronomical simulator.
"""

import warnings

warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API.*",
    category=UserWarning,
    module="vpython",
)

from simulation.scene_setup import setup_scene
from simulation.simulation import Simulation
from ui.simulation_controls import SimulationControls
from config.local_system_state_vectors import STATE_VECTORS_GENERATED
from tools.fetch_jpl_local_system_vectors import run_fetch_tool


def main() -> None:
    if not STATE_VECTORS_GENERATED:
        print("State vectors not generated. Fetching from JPL Horizons...")
        run_fetch_tool()

    bodies = setup_scene()
    simulation = Simulation(bodies)

    controls = SimulationControls(simulation)
    controls.setup()

    simulation.run()


if __name__ == "__main__":
    main()
