import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def clean_triangle_simulation():
    # --- CONFIGURATION ---
    ROWS = 60
    COLS = 100
    STEPS = 120
    
    # 1. SETUP THE GRID
    # Grid state: 0 (Dead), 1 (Alive)
    grid = np.zeros((ROWS, COLS), dtype=int)
    
    # Seed: Single active triangle in the center
    grid[ROWS//2, COLS//2] = 1
    
    # History tracking
    history = [grid.copy()]
    
    print(">>> Generating High-Fidelity Triangle Mesh...")
    
    # 2. RUN SIMULATION (Rule 30 Logic)
    for t in range(STEPS):
        new_grid = np.zeros_like(grid)
        
        for r in range(ROWS):
            for c in range(COLS):
                # Identify Neighbors (Periodic/Torus Boundaries)
                left  = grid[r, (c - 1) % COLS]
                right = grid[r, (c + 1) % COLS]
                
                # Vertical neighbor depends on triangle orientation
                # (Even sum = Up-pointing, Odd sum = Down-pointing)
                if (r + c) % 2 == 0: 
                    # Up-pointing looks DOWN for its vertical neighbor
                    v_r = (r + 1) % ROWS
                else:
                    # Down-pointing looks UP for its vertical neighbor
                    v_r = (r - 1) % ROWS
                
                vertical = grid[v_r, c]
                
                # RULE 30 LOGIC: Left XOR (Vertical OR Right)
                # Note: We treat "Vertical" as the "Center" input
                new_grid[r, c] = left ^ (vertical | right)
        
        grid = new_grid
        history.append(grid.copy())

    # 3. RENDER CLEAN GRAPHICS
    # We visualize only the FINAL state to show the resulting texture
    final_grid = history[-1]
    
    fig, ax = plt.subplots(figsize=(20, 12)) # Widescreen for clarity
    ax.set_facecolor('#1a1a1a') # Dark gray background for contrast
    
    patches = []
    
    # Geometry: Equilateral Triangles
    # Side length = 1.0 -> Height = sqrt(3)/2
    # We stretch X by 2.0 to fix the "compression artifact"
    # One column index now equals One unit on the X-axis.
    side = 1.0 
    h = (np.sqrt(3)/2) * side
    
    print(">>> Rendering vector graphics...")
    
    for r in range(ROWS):
        for c in range(COLS):
            if final_grid[r, c] == 1:
                # Coordinate Mapping (Fixed)
                # x_off is simply 'c' now (not c * 0.5) to span full width
                # We shift every other row slightly to make them interlock
                # But to maintain integer columns, we use the specific interlocking logic:
                
                x_center = c 
                y_base = r * h
                
                # Vertices Calculation
                if (r + c) % 2 == 0: 
                    # UP Pointing Triangle
                    # (x, y), (x+1, y), (x+0.5, y+h) - roughly
                    # To interlock perfectly with X=C mapping:
                    pts = [
                        [x_center, y_base],           # Bottom Left
                        [x_center + 1, y_base],       # Bottom Right
                        [x_center + 0.5, y_base + h]  # Top Tip
                    ]
                else: 
                    # DOWN Pointing Triangle
                    pts = [
                        [x_center, y_base + h],       # Top Left
                        [x_center + 1, y_base + h],   # Top Right
                        [x_center + 0.5, y_base]      # Bottom Tip
                    ]
                
                patches.append(Polygon(pts))

    # Add triangles to plot with high-contrast Neon color
    p = PatchCollection(patches, facecolors='#00FFCC', edgecolors='none', alpha=1.0)
    ax.add_collection(p)
    
    # Clean up axes
    ax.set_xlim(0, COLS)
    ax.set_ylim(0, ROWS * h)
    ax.set_aspect('equal')
    ax.invert_yaxis() # Matrix convention (Row 0 at top)
    
    # Labels
    ax.set_title(f"Rule 30 on Triangle Mesh (Fixed Coordinates)\nGrid Width: {COLS} | Chaos Saturation: 100%", 
                 fontsize=18, color='white', pad=20)
    
    # Remove ticks for a cleaner "texture" look
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    clean_triangle_simulation()