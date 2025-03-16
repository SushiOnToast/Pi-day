# Pi Day

In honour of Pi day, we've created a repository with the code to the fun little gimmicks shown in our pi day video!

## Table of Contents
- [Features](#features)
  - [Monte Carlo Pi Estimation](#monte-carlo-pi-estimation)
  - [Pi-based Encryption Tool](#pi-based-encryption-tool)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Features

### Monte Carlo Pi Estimation
The project includes three different implementations of the Monte Carlo method for estimating π:

1. **Simple Version** (`monte_carlo_simple.py`):
   - Basic implementation of the Monte Carlo method
   - Quick and straightforward calculation

2. **Statistics Version** (`monte_carlo_with_stats.py`):
   - Enhanced version with detailed statistics
   - Prettier console outputs
   - High-precision calculations using mpmath

3. **Animated Visualization** (`monte_carlo_animation.py`):
   - Cool visualization of the Monte Carlo process
   - Real-time point plotting with neon effect
   - Live statistics updates

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

## Contributing
We welcome contributions to make this Pi Day celebration even better! Here's how you can contribute:

### Ways to Contribute
1. **Add New Features**
   - New π estimation methods
   - Different visualization styles
   - Additional π-based tools

2. **Improve Existing Code**
   - Optimize performance
   - Enhance visualizations
   - Add error handling
   - Improve documentation

3. **Report Issues**
   - Bug reports
   - Feature requests
   - Documentation improvements

### How to Submit Changes
1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Test your changes thoroughly
5. Submit a pull request with a clear description of your changes

### Style Guidelines
- Follow PEP 8 Python style guide
- Add docstrings to new functions/classes
- Comment complex code sections
- Keep a similar aesthetic for visualizations

### Get in Touch
Have questions or ideas? Feel free to:
- Open an issue
- Start a discussion
- Reach out to the maintainers

Thank you for helping make this project better! 🥧

