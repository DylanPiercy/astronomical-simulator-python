"""
Entry point for the astronomical simulator.
"""

from simulation.scene_setup import setup_scene
from simulation.simulation import Simulation
from ui.simulation_controls import SimulationControls


def main() -> None:
    bodies = setup_scene()
    simulation = Simulation(bodies)

    controls = SimulationControls(simulation)
    controls.setup()

    simulation.run()


if __name__ == "__main__":
    main()
