import random
import time
from mpmath import mp
from rich.console import Console
from rich.progress import track


console = Console()

mp.dps = 1000  
pi_digits = str(mp.pi)[2:] 

def generate_pi_key(length=16):
    console.print("[bold cyan]Generating Encryption Key...[/bold cyan]", style="bold magenta")

    key = ""
    for i in track(range(length), description="Selecting Digits..."):
        time.sleep(0.3 - (i * 0.015))  # Simulate processing delay
        key += random.choice(pi_digits)

    console.print(f"\n[bold cyan]Generated Encryption Key:[/bold cyan] [yellow]{key}[/yellow]\n")

# Run the function
generate_pi_key(16)
