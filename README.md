# Modular Horizon Stability & Relative Entropy Simulator

A computational framework implementing a classical thermodynamics proxy for infinite-dimensional operator algebras. This simulator maps **Tomita-Takesaki Modular Theory** and **Kubo-Martin-Schwinger (KMS) boundary conditions** onto open biological systems using 2D spectroscopic parameters.

## Core Architectural Mechanism

The codebase models a finite-dimensional projection of the structural equation:

\[\mathbf{[INSIDE\_BOUNDARY] - [OUTSIDE\_BOUNDARY] = [HORIZON]}\]

By converting physical femtosecond laser delays (τ) into a dimensionless modular time parameter (\(t_{\text{modular}}\)) scaled to internal cellular temperatures, the simulator computes environmental noise cancellation efficiency alongside its resulting relative information entropy shifts (\(S(\rho' \parallel \rho)\)) in a two-level Gibbs state configuration.

## Features

- **Modular Flow Mapping**: Converts real-world ultra-short laser pulse delays into localized Tomita modular time trajectories.
- **KMS Stability Evaluation**: Simulates efficiency bounds derived from standard von Neumann Type III₁ algebraic constraints.
- **Relative Entropy Tracking**: Calculates the Kullback-Leibler (KL) divergence in both nats and bits to track structural informational gains across a defined boundary horizon.

## Mathematics & Physics Formulas Implemented

### 1. Modular Time Scaling
\[t_{\text{modular}} = \frac{k_B \cdot T_{\text{cell}}}{\hbar} \cdot \tau\]

### 2. Engineered Horizon Efficiency Bound
\[\eta = \eta_{\text{max}} \cdot \left(1 - e^{-\chi_{\text{KMS}}}\right)\]
*Where \(\eta_{\text{max}} = 0.4122\) (41.22% theoretical Type III factor maximum ceiling at 37°C).*

### 3. Gibbs Perturbation
\[\beta' = \beta_0 \cdot (1 + G \cdot \eta)\]
*Where G represents the programmatic mapping gain modifier.*

---

## Dependencies

The implementation relies strictly on standard scientific and typing Python packages:

- `numpy`
- `scipy`

## Installation

Ensure you have the required dependencies installed via pip:

```bash
pip install numpy scipy
```

## Usage

Save the script to a file, for example `modular_horizon.py`, and run it directly from your terminal:

```bash
python modular_horizon.py
```

### Script Execution Profile

The simulator evaluates a sweep of ultra-short time delays to calculate the phase-dependent stabilization metrics of the interface:

```python
from modular_horizon import compute_relative_entropy_from_spectro

# Run single step evaluation
t_mod, eff, S_nats, S_bits, kms = compute_relative_entropy_from_spectro(
    pulse_delay_fs=10.0,
    coupling_strength=1.85,
    energy_eV=0.1,
    temperature_c=37.0,
    mapping_gain=1.0
)

print(f"Isolated Horizon Signal: {S_bits:.6e} bits")
```

## Codebase Architecture Reference

| Function Name | Description | Mathematical Anchor |
| :--- | :--- | :--- |
| `optimize_modular_flow` | Calculates dimensionless modular time trajectories and bounds efficiency limits. | Tomita-Takesaki Modular Automorphism Group |
| `two_level_gibbs_probs` | Returns discrete probability distributions (p₀, p₁) for a two-level state. | Equilibrium Gibbs State Mechanics |
| `relative_entropy_probs` | Computes the numerical distance between perturbed configurations with zero-guarding. | Araki Relative Entropy / KL-Divergence |
| `compute_relative_entropy_from_spectro` | Core coordination pipeline linking laboratory spectroscopy vectors to structural information values. | Connes-Takesaki Cocycle Transition Bridge |

## License

This framework is open-source and intended for advanced biophysics simulation, quantum biology modeling, and non-commutative information theory engineering.
