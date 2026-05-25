"""
Solar system model to represent a collection of celestial bodies.
"""


class SolarSystem:
    """
    Represents a named collection of celestial bodies.
    """

    def __init__(self, name: str, bodies):
        self.name = name
        self.bodies = bodies

    def get_bodies(self):
        """
        Returns all celestial bodies in the solar system.
        """
        return self.bodies
