import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.font_manager as fm
import os
from matplotlib.patches import Rectangle

# Define font path relative to the script directory
font_filename = "Ticketing.ttf"  # Make sure this file is in the same directory as the script
font_path = os.path.join(os.path.dirname(__file__), font_filename)

# Check if the font file exists, otherwise fall back to default
if os.path.exists(font_path):
    pixel_font = fm.FontProperties(fname=font_path, size=20)  # Increased base font size
else:
    print("Font file not found! Using default font.")
    pixel_font = None

# Set style
plt.style.use("dark_background")

# Data storage
inside_x, inside_y = [], []
outside_x, outside_y = [], []
inside_circle = 0  # Count points inside the circle
total_points = 5000  # Number of points
animation_running = True

# Initialize figure with dark background
fig = plt.figure(figsize=(12, 12), facecolor='black')  # Back to square figure
ax = plt.subplot(111)  # Single plot
ax.set_facecolor('black')

# Initialize static plot elements
def init():
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    
    # Remove axes and grid
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    
    # Draw unit circle with cyan neon effect
    # Multiple circles for glow effect
    for alpha, width in zip([0.1, 0.2, 0.3], [3.0, 2.0, 1.0]):
        circle = plt.Circle((0, 0), 1, 
                          color='#00fff9',  # Cyan to match inside dots
                          fill=False, 
                          linestyle="-", 
                          lw=width, 
                          alpha=alpha)
        ax.add_patch(circle)
    
    # Add square border with purple glow
    # Multiple squares for glow effect
    for alpha, width in zip([0.1, 0.2, 0.3], [3.0, 2.0, 1.0]):
        square = Rectangle((-1, -1), 2, 2, 
                         fill=False, 
                         color='#ff00ff', 
                         linestyle='-', 
                         linewidth=width, 
                         alpha=alpha)
        ax.add_patch(square)
    
    return []

# Create scatter plot artists with manual glow effect
def create_glow_scatter(color, size_base=30):
    return [
        ax.scatter([], [], color=color, s=size_base*4, alpha=0.05),  # Outer glow
        ax.scatter([], [], color=color, s=size_base*2, alpha=0.1),   # Middle glow
        ax.scatter([], [], color=color, s=size_base, alpha=0.8)      # Core
    ]

inside_scatters = create_glow_scatter("#00fff9")  # Cyan for inside points
outside_scatters = create_glow_scatter("#ff00ff")  # Purple for outside points

def update(frame):
    global inside_circle, animation_running
    
    if not animation_running:
        return []
        
    try:
        # Generate random point
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        distance = x**2 + y**2

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
            
    except Exception as e:
        print(f"Animation error caught: {e}")
        animation_running = False
    
    return inside_scatters + outside_scatters

def on_close(event):
    global animation_running
    print("Window closed. Stopping animation...")
    animation_running = False
    plt.close('all')

# Initialize the plot
init()

# Animation with optimized settings
ani = animation.FuncAnimation(
    fig, 
    update, 
    frames=total_points, 
    interval=0.0000001,  # Animation speed
    repeat=False,
    blit=True
)

# Connect the close event
fig.canvas.mpl_connect("close_event", on_close)

plt.show()
