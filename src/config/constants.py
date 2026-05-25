"""
Shared constants for the astronomical simulator.
"""

# Physics constants
GRAVITATIONAL_CONSTANT = 6.67430e-11  # m^3 kg^-1 s^-2

# Distance constants
ASTRONOMICAL_UNIT = 149_597_870_700  # metres

# Time constants
SECONDS_PER_DAY = 86_400
TIME_STEP = SECONDS_PER_DAY  # one simulated day per update

# Visual scaling
DISTANCE_SCALE = 300 / ASTRONOMICAL_UNIT

STAR_RADIUS_SCALE = 300 / ASTRONOMICAL_UNIT
PLANET_RADIUS_SCALE = 300 / ASTRONOMICAL_UNIT
MOON_RADIUS_SCALE = 300 / ASTRONOMICAL_UNIT

MIN_PLANET_RADIUS_SCALE = 0.5
MIN_MOON_RADIUS_SCALE = 0.1

# Simulation settings
UPDATE_RATE = 1  # VPython animation updates per second
PLANET_TRAIL_RETAIN = 50
MOON_TRAIL_RETAIN = 10
