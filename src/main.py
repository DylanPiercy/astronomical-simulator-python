"""
Entry point for the astronomical simulator.
"""

from simulation.scene_setup import setup_scene
from simulation.simulation import Simulation


def main() -> None:
    bodies = setup_scene()
    simulation = Simulation(bodies)
    simulation.run()


if __name__ == "__main__":
    main()
