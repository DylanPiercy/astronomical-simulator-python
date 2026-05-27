"""
Fetches JPL Horizons state vectors for the local solar system preset.

Run from the project root:

python src/tools/fetch_jpl_local_system_vectors.py

This overwrites:
src/config/local_system_state_vectors.py
"""

import json
import re
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path

OUTPUT_FILE = (
    Path(__file__).resolve().parents[1] / "config" / "local_system_state_vectors.py"
)

EPOCH_START = "2026-Jan-01 00:00"
EPOCH_STOP = "2026-Jan-02 00:00"

SUN_CENTER = "500@10"
EARTH_CENTER = "500@399"


@dataclass(frozen=True)
class BodyQuery:
    command: str
    center: str


@dataclass(frozen=True)
class StateVector:
    position_m: tuple[float, float, float]
    velocity_m_s: tuple[float, float, float]


BODIES: dict[str, BodyQuery] = {
    "MERCURY": BodyQuery(command="199", center=SUN_CENTER),
    "VENUS": BodyQuery(command="299", center=SUN_CENTER),
    "EARTH": BodyQuery(command="399", center=SUN_CENTER),
    "MOON": BodyQuery(command="301", center=EARTH_CENTER),
    "MARS": BodyQuery(command="499", center=SUN_CENTER),
    "JUPITER": BodyQuery(command="599", center=SUN_CENTER),
    "SATURN": BodyQuery(command="699", center=SUN_CENTER),
    "URANUS": BodyQuery(command="799", center=SUN_CENTER),
    "NEPTUNE": BodyQuery(command="899", center=SUN_CENTER),
    "PLUTO": BodyQuery(command="999", center=SUN_CENTER),
}


def run_fetch_tool() -> None:
    vectors = {
        body_name: fetch_state_vector(body_query)
        for body_name, body_query in BODIES.items()
    }

    write_output_file(vectors)


def fetch_state_vector(body_query: BodyQuery) -> StateVector:
    params = {
        "format": "json",
        "COMMAND": f"'{body_query.command}'",
        "OBJ_DATA": "NO",
        "MAKE_EPHEM": "YES",
        "EPHEM_TYPE": "VECTORS",
        "CENTER": f"'{body_query.center}'",
        "START_TIME": f"'{EPOCH_START}'",
        "STOP_TIME": f"'{EPOCH_STOP}'",
        "STEP_SIZE": "'1 d'",
        "VEC_TABLE": "2",
        "OUT_UNITS": "'KM-S'",
        "REF_PLANE": "ECLIPTIC",
        "REF_SYSTEM": "J2000",
    }

    url = "https://ssd.jpl.nasa.gov/api/horizons.api?" + urllib.parse.urlencode(params)

    with urllib.request.urlopen(url) as response:
        payload = json.loads(response.read().decode("utf-8"))

    result = payload["result"]

    position_km = extract_vector(result, "X", "Y", "Z")
    velocity_km_s = extract_vector(result, "VX", "VY", "VZ")

    return StateVector(
        position_m=(
            position_km[0] * 1000,
            position_km[1] * 1000,
            position_km[2] * 1000,
        ),
        velocity_m_s=(
            velocity_km_s[0] * 1000,
            velocity_km_s[1] * 1000,
            velocity_km_s[2] * 1000,
        ),
    )


def extract_vector(
    text: str,
    x_key: str,
    y_key: str,
    z_key: str,
) -> tuple[float, float, float]:
    pattern = (
        rf"{x_key}\s*=\s*([+-]?\d+\.\d+E[+-]\d+)"
        rf"\s+{y_key}\s*=\s*([+-]?\d+\.\d+E[+-]\d+)"
        rf"\s+{z_key}\s*=\s*([+-]?\d+\.\d+E[+-]\d+)"
    )

    match = re.search(pattern, text)

    if match is None:
        raise ValueError(
            f"Could not parse {x_key}, {y_key}, {z_key} from Horizons output."
        )

    x_value, y_value, z_value = match.groups()

    return (
        float(x_value),
        float(y_value),
        float(z_value),
    )


def write_output_file(vectors: dict[str, StateVector]) -> None:
    lines = [
        '"""',
        "JPL Horizons state vectors for the local solar system preset.",
        "",
        "Generated for {EPOCH_START} UTC.",
        "Positions are in metres.",
        "Velocities are in metres per second.",
        "",
        "Planet vectors are relative to the Sun.",
        "Moon vector is relative to Earth.",
        '"""',
        "",
        "STATE_VECTORS_GENERATED = True",
        "",
    ]

    for body_name, state_vector in vectors.items():
        lines.append(f"{body_name}_RELATIVE_POSITION = {state_vector.position_m}")
        lines.append(f"{body_name}_RELATIVE_VELOCITY = {state_vector.velocity_m_s}")
        lines.append("")

    OUTPUT_FILE.write_text("\n".join(lines))
    print(f"Generated {OUTPUT_FILE}")


if __name__ == "__main__":
    run_fetch_tool()
