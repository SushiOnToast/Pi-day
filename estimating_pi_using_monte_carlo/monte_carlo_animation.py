"""
Monte Carlo Pi Estimation - Animated Visualization
-----------------------------------------------

This script provides an interactive visualization of the Monte Carlo method for estimating π (pi).
It creates two windows:
1. Animation window: Shows the actual Monte Carlo simulation with points and geometric shapes
2. Stats window: Displays real-time statistics and the estimation formula

The Monte Carlo method estimates π by comparing the ratio of points that fall inside a quarter circle
to the total number of randomly generated points. The ratio, multiplied by 4, approximates π.

"""

import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.font_manager as fm
import os
from matplotlib.patches import Rectangle

# Define font path relative to the script directory
font_filename = "../Ticketing.ttf"  # Custom pixel font for retro aesthetic
font_path = os.path.join(os.path.dirname(__file__), font_filename)

# Check if the font file exists, otherwise fall back to default
if os.path.exists(font_path):
    pixel_font = fm.FontProperties(fname=font_path, size=20)  # Main title font
    stats_font = fm.FontProperties(fname=font_path, size=14)  # Stats display font
else:
    print("Font file not found! Using default font.")
    pixel_font = None
    stats_font = None

# Set style
plt.style.use("dark_background")

# Data storage
inside_x, inside_y = [], []
outside_x, outside_y = [], []
inside_circle = 0  # Count points inside the circle
total_points = 5000  # Number of points
animation_running = True

# Initialize main figure with custom background
fig_main = plt.figure(figsize=(8, 8), facecolor='#141414')  # Smaller square figure
ax_main = plt.subplot(111)
ax_main.set_facecolor('#141414')
fig_main.canvas.manager.set_window_title('Animation')  # Set window title

# Initialize stats figure
fig_stats = plt.figure(figsize=(4, 3), facecolor='#141414')  # Smaller stats window
ax_stats = plt.subplot(111)
ax_stats.set_facecolor('#141414')
fig_stats.canvas.manager.set_window_title('Stats')  # Set window title

# Create stats text with formulas
stats_text = ax_stats.text(0.5, 0.5, '', 
                          fontproperties=stats_font if stats_font else None,
                          color='white',
                          horizontalalignment='center',
                          verticalalignment='center',
                          transform=ax_stats.transAxes)

# Add formula text with explanation
formula_text = ax_stats.text(0.5, 0.9, 
                           'π = 4 × (points_inside / total_points)',
                           fontproperties=stats_font if stats_font else None,
                           color='#888888',
                           horizontalalignment='center',
                           verticalalignment='center',
                           transform=ax_stats.transAxes,
                           alpha=0.7)

# Remove unnecessary elements from stats window
ax_stats.set_xticks([])
ax_stats.set_yticks([])
for spine in ax_stats.spines.values():
    spine.set_visible(False)

# Initialize static plot elements
def init():
    """Initialize the animation plot with static elements.
    
    Sets up the coordinate system, adds title, and creates the basic geometric shapes
    with neon glow effects (circle and square).
    
    Returns:
        list: Empty list for animation initialization
    """
    ax_main.set_xlim(-1.2, 1.2)
    ax_main.set_ylim(-1.2, 1.2)
    ax_main.set_aspect('equal')
    
    # Add title with custom font
    if pixel_font:
        ax_main.set_title('Estimation of Pi using Monte Carlo', 
                    fontproperties=pixel_font,
                    color='#00fff9',  # Cyan to match the circle
                    pad=15,  # Reduced padding
                    y=1.01)  # Lower position
    
    # Remove axes and grid for clean look
    ax_main.set_xticks([])
    ax_main.set_yticks([])
    for spine in ax_main.spines.values():
        spine.set_visible(False)
    
    # Draw unit circle with cyan neon glow effect
    for alpha, width in zip([0.1, 0.2, 0.3], [3.0, 2.0, 1.0]):
        circle = plt.Circle((0, 0), 1, 
                          color='#00fff9',  # Cyan
                          fill=False, 
                          linestyle="-", 
                          lw=width, 
                          alpha=alpha)
        ax_main.add_patch(circle)
    
    # Add square border with purple neon glow
    for alpha, width in zip([0.1, 0.2, 0.3], [3.0, 2.0, 1.0]):
        square = Rectangle((-1, -1), 2, 2, 
                         fill=False, 
                         color='#ff00ff',  # Purple
                         linestyle='-', 
                         linewidth=width, 
                         alpha=alpha)
        ax_main.add_patch(square)
    
    return []

# Create scatter plot artists with manual glow effect
def create_glow_scatter(color, size_base=20):
    """Create scatter plot artists with manual glow effect.
    
    Args:
        color (str): Hex color code for the points
        size_base (int): Base size for the scatter points
    
    Returns:
        list: List of scatter plot artists with different sizes and alphas for glow effect
    """
    return [
        ax_main.scatter([], [], color=color, s=size_base*4, alpha=0.05),  # Outer glow
        ax_main.scatter([], [], color=color, s=size_base*2, alpha=0.1),   # Middle glow
        ax_main.scatter([], [], color=color, s=size_base, alpha=0.8)      # Core
    ]

# Create scatter artists for points
inside_scatters = create_glow_scatter("#00fff9")  # Cyan for inside points
outside_scatters = create_glow_scatter("#ff00ff")  # Purple for outside points

def update_stats():
    """Update the statistics display in the stats window.
    
    Calculates and displays:
    - Number of points inside circle
    - Total number of points
    - Current π estimate
    - Current accuracy percentage
    """
    if inside_circle == 0:
        return
    
    total = len(inside_x + outside_x)
    pi_estimate = (inside_circle / total) * 4
    error = abs(pi_estimate - np.pi) / np.pi * 100
    accuracy = 100 - error
    
    stats_str = f"""Points Inside: {inside_circle:,}
Total Points: {total:,}
π Estimate: {pi_estimate:.6f}
Accuracy: {accuracy:.2f}%"""
    
    stats_text.set_text(stats_str)
    fig_stats.canvas.draw_idle()

def update(frame):
    """Animation update function called for each frame.
    
    Args:
        frame: Frame number (not used directly)
    
    Returns:
        list: List of artists to update in the animation
    """
    global inside_circle, animation_running
    
    if not animation_running:
        return []
        
    try:
        # Generate random point
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        distance = x**2 + y**2

        # Determine if point is inside circle
        if distance <= 1:
            inside_x.append(x)
            inside_y.append(y)
            inside_circle += 1
        else:
            outside_x.append(x)
            outside_y.append(y)
        
        # Update scatter data with glow effect
        if inside_x:
            for scatter in inside_scatters:
                scatter.set_offsets(np.c_[inside_x, inside_y])
        if outside_x:
            for scatter in outside_scatters:
                scatter.set_offsets(np.c_[outside_x, outside_y])
        
        # Update stats periodically
        if frame % 10 == 0:
            update_stats()
            
    except Exception as e:
        print(f"Animation error caught: {e}")
        animation_running = False
    
    return inside_scatters + outside_scatters

def on_close(event):
    """Handle window close event.
    
    Ensures clean shutdown of animation when either window is closed.
    """
    global animation_running
    print("Window closed. Stopping animation...")
    animation_running = False
    plt.close('all')

# Initialize the plot
init()

# Set up the animation
ani = animation.FuncAnimation(
    fig_main, 
    update, 
    frames=total_points, 
    interval=0.000000000000001,  # Maximum animation speed
    repeat=False,
    blit=True
)

# Connect close event handlers
fig_main.canvas.mpl_connect("close_event", on_close)
fig_stats.canvas.mpl_connect("close_event", on_close)

# Position the windows on screen
fig_stats.canvas.manager.window.geometry("+0+0")  # Stats window at top-left
fig_main.canvas.manager.window.geometry("+400+0")  # Main window to the right

# Start the animation
plt.show()
