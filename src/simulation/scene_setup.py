"""
Scene setup for the astronomical simulator.
"""

from vpython import vector, scene

from models.celestial_body import CelestialBody
from presets.local_system import create_local_system
from presets.alpha_centauri import create_alpha_centauri_system


def setup_scene() -> list[CelestialBody]:
    """
    Sets up the initial VPython scene and creates the starting celestial bodies.
    """
    scene.title = "Astronomical Simulator"
    scene.width = 2400
    scene.height = 1200
    scene.background = vector(0.02, 0.03, 0.10)
    scene.resizable = True

    # Create a default celestial body to ensure the scene is initialized.
    system = create_local_system()
    # system = create_alpha_centauri_system()
    return system.get_bodies()
