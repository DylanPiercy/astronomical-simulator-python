"""
Celestial body model used to represent stars, planets, moons, and other astronomical objects.
"""

from vpython import sphere, vector

from config.constants import DISTANCE_SCALE, MIN_BODY_VISUAL_RADIUS, RADIUS_SCALE, TRAIL_RETAIN


class CelestialBody:
    """
    Represents a physical body in the simulation.

    Position, velocity, mass, and radius use real SI units.
    The visual sphere is scaled separately for display.
    """

    def __init__(
        self,
        name: str,
        mass: float,
        radius: float,
        position: vector,
        velocity: vector,
        colour: vector,
        make_trail: bool = True,
    ):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.position = position
        self.velocity = velocity

        self.visual = sphere(
            pos=self.position * DISTANCE_SCALE,
            radius=max(self.radius * RADIUS_SCALE, MIN_BODY_VISUAL_RADIUS),
            color=colour,
            make_trail=make_trail,
            retain=TRAIL_RETAIN,
        )

    def update_visual_position(self) -> None:
        """
        Updates the VPython sphere position to match the body's physical position.
        """
        self.visual.pos = self.position * DISTANCE_SCALE
