"""Core calculations for the relative-entropy-bridge package.

This module provides functions to convert femtosecond pulse delays to a
dimensionless modular time, evaluate a KMS alignment index, and compute a
Type-III-bounded engineered efficiency.

The package directory was renamed from `relative-entropy-bridge` to
`relative_entropy_bridge` to be a valid Python package name. These functions
are intentionally side-effect free so importing the package won't run scripts.
"""

from typing import Tuple
import numpy as np

# --- CORE PHYSICAL CONSTANTS ---
BOLTZMANN_K = 1.380649e-23  # J/K
REDUCED_PLANCK_HBAR = 1.0545718e-34  # J*s
TYPE_III_MAX_EFFICIENCY = 0.4122  # Bounded Type III ceiling (~41.22%)


def convert_fs_to_modular_time(pulse_delay_fs: float, temp_celsius: float = 37.0) -> float:
    """Scales a femtosecond laser delay to the dimensionless modular time 't'.

    Args:
        pulse_delay_fs: Delay in femtoseconds.
        temp_celsius: Temperature in Celsius used for the conversion (default: 37°C).

    Returns:
        Dimensionless modular time 't'.
    """
    T_cell = temp_celsius + 273.15
    tau = pulse_delay_fs * 1e-15
    return (BOLTZMANN_K * T_cell / REDUCED_PLANCK_HBAR) * tau


def compute_kms_stability(t_modular: float, coupling_strength: float) -> float:
    """Evaluate the KMS alignment index.

    Measures how well an external field tracks the intrinsic modular flow.
    """
    base_alignment = np.sin(t_modular)
    return float(np.abs(base_alignment * coupling_strength))


def calculate_engineered_efficiency(kms_stability_index: float) -> float:
    """Calculate thermodynamic efficiency (percentage) bounded by Type III limits.

    Returns the efficiency as a percentage (0.0 -- 100.0).
    """
    efficiency_fraction = TYPE_III_MAX_EFFICIENCY * (1.0 - np.exp(-kms_stability_index))
    return efficiency_fraction * 100.0


def optimize_modular_flow(pulse_delay_fs: float, coupling_strength: float) -> Tuple[float, float, float]:
    """Coordinate the modular flow tracking pipeline for a given delay phase.

    Returns a tuple: (t_modular, kms_index, efficiency_percent)
    """
    t_modular = convert_fs_to_modular_time(pulse_delay_fs)
    kms_idx = compute_kms_stability(t_modular, coupling_strength)
    efficiency = calculate_engineered_efficiency(kms_idx)
    return t_modular, kms_idx, efficiency


__all__ = [
    "convert_fs_to_modular_time",
    "compute_kms_stability",
    "calculate_engineered_efficiency",
    "optimize_modular_flow",
]
