# Pi Day

In honour of Pi day, we've created a repository with the code to the fun little gimmicks shown in our pi day video!

## Features

### Monte Carlo Pi Estimation
The project includes three different implementations of the Monte Carlo method for estimating π:

1. **Simple Version** (`monte_carlo_simple.py`):
   - Basic implementation of the Monte Carlo method
   - Quick and straightforward calculation

2. **Statistics Version** (`monte_carlo_with_stats.py`):
   - Enhanced version with detailed statistics
   - Real-time progress tracking
   - High-precision calculations using mpmath

3. **Animated Visualization** (`monte_carlo_animation.py`):
   - Interactive visualization of the Monte Carlo process
   - Real-time point plotting with neon effect
   - Live statistics updates
   - Custom pixel art styling

### Pi-based Encryption Tool
- Generates encryption keys using digits of π
- Uses high-precision π calculations
- Includes progress visualization

## Requirements
- Python 3.x
- Required packages listed in requirements.txt

## Installation
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Usage
Each script can be run independently:

```bash
# Run the animated visualization
python estimating_pi_using_monte_carlo/monte_carlo_animation.py

# Run the statistics version
python estimating_pi_using_monte_carlo/monte_carlo_with_stats.py

# Run the simple version
python estimating_pi_using_monte_carlo/monte_carlo_simple.py

# Generate a pi-based encryption key
python pi_encryption.py
```

Explore and have a play around!

## Technical Details
- Uses matplotlib for visualizations
- Implements custom neon glow effects
- High-precision calculations using mpmath
- Rich console output for enhanced user experience
