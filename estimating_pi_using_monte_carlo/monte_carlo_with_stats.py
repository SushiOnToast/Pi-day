import numpy as np
import time
from mpmath import mp
from rich.console import Console
from rich.progress import track
from rich.panel import Panel

console = Console()
mp.dps = 50  

# Configuration
total = 1700000 
batch_size = 100000  

console.print("\n[bold cyan]Monte Carlo Pi Estimation[/bold cyan]", style="bold magenta")
console.print("[dim]Using random points to approximate π...[/dim]\n")

actual_pi = float(mp.pi)

inside = 0
num_batches = total // batch_size

for batch in track(range(num_batches), description="Generating Points\n"):
    x = np.random.uniform(-1, 1, batch_size)
    y = np.random.uniform(-1, 1, batch_size)
    distances = x*x + y*y
    inside += np.sum(distances <= 1)
    time.sleep(0.1)  

pi_estimate = (inside / total) * 4
error = abs(pi_estimate - actual_pi) / actual_pi * 100
accuracy = 100 - error

radius = 1.0
estimated_circle_area = pi_estimate * radius**2
actual_circle_area = actual_pi * radius**2
square_area = (2 * radius)**2

points_ratio = inside / total
theoretical_ratio = actual_pi / 4
ratio_error = abs(points_ratio - theoretical_ratio) / theoretical_ratio * 100

result = f"""[cyan]Points Used:[/cyan] [yellow]{total:,}[/yellow]
[cyan]Points Inside Circle:[/cyan] [yellow]{inside:,}[/yellow]
[cyan]Points Ratio (Inside/Total):[/cyan] [yellow]{points_ratio:.10f}[/yellow]

[cyan]Pi Estimation:[/cyan]
[cyan]Estimated π:[/cyan] [yellow]{pi_estimate:.10f}[/yellow]
[cyan]Actual π:[/cyan] [yellow]{actual_pi:.10f}[/yellow]
[cyan]Accuracy:[/cyan] [yellow]{accuracy:.6f}%[/yellow]
"""

console.print(Panel(result, 
                   title="[bold magenta]Monte Carlo Pi Estimation[/bold magenta]",
                   border_style="cyan",
                   padding=(1, 2)))
