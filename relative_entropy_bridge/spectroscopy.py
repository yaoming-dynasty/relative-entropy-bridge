"""Runnable spectroscopy helpers for the relative_entropy_bridge package.

This module contains the CLI-style runner (run_spectroscopy_sweep) and the
same core pure functions re-exported for ease of use. It is safe to import
(this module does not execute the sweep at import time).
"""

from typing import List, Tuple
import numpy as np

# --- CORE PHYSICAL CONSTANTS ---
BOLTZMANN_K = 1.380649e-23  # J/K
REDUCED_PLANCK_HBAR = 1.0545718e-34  # J*s
TYPE_III_MAX_EFFICIENCY = 0.4122  # Bounded Type III ceiling (~41.22%)


def convert_fs_to_modular_time(pulse_delay_fs: float, temp_celsius: float = 37.0) -> float:
    """Scales a femtosecond laser delay to the dimensionless modular time 't'."""
    T_cell = temp_celsius + 273.15
    tau = pulse_delay_fs * 1e-15
    return (BOLTZMANN_K * T_cell / REDUCED_PLANCK_HBAR) * tau


def compute_kms_stability(t_modular: float, coupling_strength: float) -> float:
    """Evaluate the KMS alignment index (how well an external field tracks modular flow)."""
    base_alignment = np.sin(t_modular)
    return float(np.abs(base_alignment * coupling_strength))


def calculate_engineered_efficiency(kms_stability_index: float) -> float:
    """Calculate thermodynamic efficiency (percentage) bounded by Type III limits."""
    efficiency_fraction = TYPE_III_MAX_EFFICIENCY * (1.0 - np.exp(-kms_stability_index))
    return efficiency_fraction * 100.0


def optimize_modular_flow(pulse_delay_fs: float, coupling_strength: float) -> Tuple[float, float, float]:
    """Coordinate the modular flow tracking pipeline for a given delay phase.

    Returns (t_modular, kms_index, efficiency_percent).
    """
    t_modular = convert_fs_to_modular_time(pulse_delay_fs)
    kms_idx = compute_kms_stability(t_modular, coupling_strength)
    efficiency = calculate_engineered_efficiency(kms_idx)
    return t_modular, kms_idx, efficiency


def run_spectroscopy_sweep(delays: List[float], coupling_strength: float) -> None:
    """Run a sweep over specified delays and print a results table.

    This function is intentionally lightweight so it can be used as a CLI entry
    point (python -m relative_entropy_bridge.spectroscopy) or imported by other
    modules.
    """
    header = f"{'Delay (fs)':<12} | {'Modular Time (t)':<18} | {'KMS Alignment Index':<22} | {'Thermodynamic Efficiency':<24}"
    print(header)
    print("-" * len(header))

    for delay in delays:
        t_mod, kms_idx, efficiency = optimize_modular_flow(delay, coupling_strength)
        print(f"{delay:<12.1f} | {t_mod:<18.4f} | {kms_idx:<22.4f} | {efficiency:.4f}%")


if __name__ == "__main__":
    # Example CLI execution
    target_delays = [0.0, 5.0, 10.0, 15.0]
    target_coupling = 1.85
    run_spectroscopy_sweep(delays=target_delays, coupling_strength=target_coupling)
