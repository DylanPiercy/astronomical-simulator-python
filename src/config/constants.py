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
DISTANCE_SCALE = 1 / ASTRONOMICAL_UNIT  # 1 AU becomes 1 VPython unit
RADIUS_SCALE = 1 / 10_000_000  # keeps planets visible without realistic radius scale

# Simulation settings
UPDATE_RATE = 100  # VPython animation updates per second
TRAIL_RETAIN = 500  # number of trail points to keep