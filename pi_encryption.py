"""
Pi-Based Encryption Key Generator
------------------------------

This script generates encryption keys using digits of π (pi). It provides a unique
approach to key generation by randomly selecting digits from a high-precision
calculation of π.

Features:
- Uses mpmath for high-precision π calculation (1000 decimal places)
- Customizable key length
- Rich console output with colored text and formatting

The generated keys are suitable for various encryption purposes and provide
a mathematically interesting source of randomness.

"""

import random
import time
from mpmath import mp
from rich.console import Console
from rich.progress import track

# Initialize console for rich output
console = Console()

# Set precision for pi calculation
mp.dps = 1000  # 1000 decimal places
pi_digits = str(mp.pi)[2:]  # Remove "3." from the start

def generate_pi_key(length=16):
    """Generate an encryption key using random digits of π.
    
    Args:
        length (int): Length of the key to generate (default: 16)
    
    The function displays a progress bar during generation and shows
    the final key with fancy formatting.
    """
    console.print("\n\n[bold cyan]Generating Encryption Key...[/bold cyan]", style="bold magenta")

    key = ""
    for i in track(range(length), description="Selecting Digits..."):
        time.sleep(0.3 - (i * 0.015))  # Decreasing delay for visual effect
        key += random.choice(pi_digits)

    console.print(f"\n[bold cyan]Generated Encryption Key:[/bold cyan] [yellow]{key}[/yellow]\n")

# Generate a 16-digit key
generate_pi_key(16)
