#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
import re
import argparse
from matplotlib.widgets import Slider, Button, TextBox

def read_hkl_file(filename):
    hkl_data = []
    found_header = False
    
    with open(filename, 'r') as f:
        for line in f:
            if "# H   K   L     Mult    dspc                   |Fc|^2" in line:
                found_header = True
                continue
            if found_header and line.strip() and not line.startswith('#'):
                # Parse the line
                values = line.split()
                if len(values) >= 6:
                    h, k, l = map(int, values[0:3])
                    fc_squared = float(values[5])
                    hkl_data.append((h, k, l, fc_squared))
    
    return hkl_data

def plot_crystal_structure(hkl_data, initial_size=50):
    # Create figure and 3D axes with extra space for controls
    fig = plt.figure(figsize=(16, 14))
    ax = fig.add_subplot(111, projection='3d')
    
    # Extract coordinates and sizes
    h = np.array([x[0] for x in hkl_data])
    k = np.array([x[1] for x in hkl_data])
    l = np.array([x[2] for x in hkl_data])
    sizes = np.array([x[3] for x in hkl_data])
    
    # Store max_size for normalization
    max_size = np.max(sizes)
    
    # Calculate initial sizes
    initial_sizes = initial_size * (sizes / max_size)
    
    # Create scatter plot
    scatter = ax.scatter(h, k, l, 
                        s=initial_sizes,
                        alpha=0.6,
                        c=sizes,
                        cmap='viridis')
    
    # Add colorbar
    colorbar = plt.colorbar(scatter, label='|Fc|²')
    
    # Set labels and title
    ax.set_xlabel('H')
    ax.set_ylabel('K')
    ax.set_zlabel('L')
    title = ax.set_title(f'Crystal Structure Visualization\nSphere size proportional to |Fc|² (size factor: {initial_size})')
    
    # Set equal aspect ratio
    ax.set_box_aspect([1,1,1])
    
    # Add grid
    ax.grid(True)
    
    # Adjust layout to make room for controls
    plt.subplots_adjust(bottom=0.4)
    
    # HKL Range Control Section
    # Extract H, K, L ranges
    h_min, h_max = min(h), max(h)
    k_min, k_max = min(k), max(k)
    l_min, l_max = min(l), max(l)
    intensity_min, intensity_max = min(sizes), max(sizes)
    
    # Create sliders for H, K, L ranges
    slider_height = 0.02
    slider_width = 0.3
    
    # H range sliders (min and max separately)
    h_min_slider_ax = plt.axes([0.1, 0.32, slider_width, slider_height])
    h_min_slider = Slider(h_min_slider_ax, 'H Min', h_min, h_max, valinit=h_min, valfmt='%d')
    
    h_max_slider_ax = plt.axes([0.1, 0.30, slider_width, slider_height])
    h_max_slider = Slider(h_max_slider_ax, 'H Max', h_min, h_max, valinit=h_max, valfmt='%d')
    
    # K range sliders (min and max separately)
    k_min_slider_ax = plt.axes([0.1, 0.26, slider_width, slider_height])
    k_min_slider = Slider(k_min_slider_ax, 'K Min', k_min, k_max, valinit=k_min, valfmt='%d')
    
    k_max_slider_ax = plt.axes([0.1, 0.24, slider_width, slider_height])
    k_max_slider = Slider(k_max_slider_ax, 'K Max', k_min, k_max, valinit=k_max, valfmt='%d')
    
    # L range sliders (min and max separately)
    l_min_slider_ax = plt.axes([0.1, 0.20, slider_width, slider_height])
    l_min_slider = Slider(l_min_slider_ax, 'L Min', l_min, l_max, valinit=l_min, valfmt='%d')
    
    l_max_slider_ax = plt.axes([0.1, 0.18, slider_width, slider_height])
    l_max_slider = Slider(l_max_slider_ax, 'L Max', l_min, l_max, valinit=l_max, valfmt='%d')
    
    # Intensity threshold slider
    intensity_slider_ax = plt.axes([0.1, 0.14, slider_width, slider_height])
    intensity_slider = Slider(intensity_slider_ax, 'Intensity Min', intensity_min, intensity_max, 
                            valinit=intensity_min, valfmt='%.2e')
    
    # Size factor slider (moved up)
    size_slider_ax = plt.axes([0.1, 0.10, slider_width, slider_height])
    size_slider = Slider(size_slider_ax, 'Size Factor', 1, 1000, valinit=initial_size)
    
    # Control buttons
    # Toggle visibility button
    toggle_ax = plt.axes([0.45, 0.28, 0.15, 0.05])
    toggle_button = Button(toggle_ax, 'Show All')
    
    # Reset ranges button
    reset_ranges_ax = plt.axes([0.45, 0.24, 0.15, 0.05])
    reset_ranges_button = Button(reset_ranges_ax, 'Reset Ranges')
    
    # Reset size button
    reset_size_ax = plt.axes([0.45, 0.20, 0.15, 0.05])
    reset_size_button = Button(reset_size_ax, 'Reset Size')
    
    # Clear filter button
    clear_ax = plt.axes([0.45, 0.16, 0.15, 0.05])
    clear_button = Button(clear_ax, 'Clear Filter')
    
    # Size presets
    preset_ax1 = plt.axes([0.65, 0.28, 0.12, 0.05])
    preset_ax2 = plt.axes([0.65, 0.24, 0.12, 0.05])
    preset_ax3 = plt.axes([0.65, 0.20, 0.12, 0.05])
    
    preset1 = Button(preset_ax1, '2x Max')
    preset2 = Button(preset_ax2, '3x Max')
    preset3 = Button(preset_ax3, '5x Max')
    
    # Status text box
    status_ax = plt.axes([0.65, 0.12, 0.3, 0.08])
    status_textbox = TextBox(status_ax, 'Status:', initial=f'Showing all {len(hkl_data)} reflections\nH: {h_min}-{h_max}, K: {k_min}-{k_max}, L: {l_min}-{l_max}')
    
    # Store original data for filtering
    original_h = h.copy()
    original_k = k.copy()
    original_l = l.copy()
    original_sizes = sizes.copy()
    original_indices = np.arange(len(hkl_data))
    
    # Store colorbar reference to avoid overplotting
    current_colorbar = colorbar
    
    def update_display():
        """Update display based on current filter settings"""
        nonlocal current_colorbar
        
        # Get current range values
        h_min_val = h_min_slider.val
        h_max_val = h_max_slider.val
        k_min_val = k_min_slider.val
        k_max_val = k_max_slider.val
        l_min_val = l_min_slider.val
        l_max_val = l_max_slider.val
        intensity_threshold = intensity_slider.val
        size_factor = size_slider.val
        
        # Filter data based on ranges
        mask = ((original_h >= h_min_val) & (original_h <= h_max_val) &
                (original_k >= k_min_val) & (original_k <= k_max_val) &
                (original_l >= l_min_val) & (original_l <= l_max_val) &
                (original_sizes >= intensity_threshold))
        
        filtered_indices = original_indices[mask]
        
        # Remove existing colorbar to avoid overplotting
        if current_colorbar is not None:
            current_colorbar.remove()
        
        if len(filtered_indices) > 0:
            # Update scatter plot with filtered data
            h_filtered = original_h[filtered_indices]
            k_filtered = original_k[filtered_indices]
            l_filtered = original_l[filtered_indices]
            sizes_filtered = original_sizes[filtered_indices]
            
            # Calculate new sizes
            new_sizes = size_factor * (sizes_filtered / max_size)
            
            # Clear previous scatter plot and create new one
            ax.clear()
            
            # Recreate the scatter plot
            new_scatter = ax.scatter(h_filtered, k_filtered, l_filtered, 
                                   s=new_sizes, c=sizes_filtered, cmap='viridis', 
                                   alpha=0.6)
            
            # Create new colorbar
            current_colorbar = plt.colorbar(new_scatter, label='|Fc|²')
            
            # Restore labels and title
            ax.set_xlabel('H')
            ax.set_ylabel('K')
            ax.set_zlabel('L')
            ax.set_title(f'Crystal Structure Visualization\nSphere size proportional to |Fc|² (size factor: {int(size_factor)})')
            
            # Restore grid and aspect ratio
            ax.grid(True)
            ax.set_box_aspect([1,1,1])
            
            # Restore HKL info text
            ax.text2D(0.02, 0.98, f'HKL Data: {len(hkl_data)} reflections\nH: {h_min} to {h_max}\nK: {k_min} to {k_max}\nL: {l_min} to {l_max}', 
                      transform=ax.transAxes, fontsize=10, verticalalignment='top',
                      bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
            # Update status
            status_textbox.set_val(f'Showing {len(filtered_indices)} reflections\nH: {h_min_val}-{h_max_val}, K: {k_min_val}-{k_max_val}, L: {l_min_val}-{l_max_val}\nIntensity ≥ {intensity_threshold:.2e}')
        else:
            # Clear scatter plot if no data matches
            ax.clear()
            current_colorbar = None
            
            # Restore labels and title
            ax.set_xlabel('H')
            ax.set_ylabel('K')
            ax.set_zlabel('L')
            ax.set_title(f'Crystal Structure Visualization\nNo reflections match criteria')
            
            # Restore grid and aspect ratio
            ax.grid(True)
            ax.set_box_aspect([1,1,1])
            
            # Restore HKL info text
            ax.text2D(0.02, 0.98, f'HKL Data: {len(hkl_data)} reflections\nH: {h_min} to {h_max}\nK: {k_min} to {k_max}\nL: {l_min} to {l_max}', 
                      transform=ax.transAxes, fontsize=10, verticalalignment='top',
                      bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
            status_textbox.set_val(f'No reflections match criteria\nH: {h_min_val}-{h_max_val}, K: {k_min_val}-{k_max_val}, L: {l_min_val}-{l_max_val}\nIntensity ≥ {intensity_threshold:.2e}')
        
        fig.canvas.draw_idle()
    
    def toggle_visibility(event):
        """Toggle between showing all data and filtered data"""
        nonlocal current_colorbar
        
        if toggle_button.label.get_text() == 'Show All':
            # Show filtered data
            toggle_button.label.set_text('Show Filtered')
            update_display()
        else:
            # Show all data
            toggle_button.label.set_text('Show All')
            
            # Remove existing colorbar to avoid overplotting
            if current_colorbar is not None:
                current_colorbar.remove()
            
            # Clear and recreate with all data
            ax.clear()
            
            # Recreate scatter plot with all data
            all_scatter = ax.scatter(original_h, original_k, original_l, 
                                   s=initial_sizes, c=original_sizes, cmap='viridis', 
                                   alpha=0.6)
            
            # Create new colorbar
            current_colorbar = plt.colorbar(all_scatter, label='|Fc|²')
            
            # Restore labels and title
            ax.set_xlabel('H')
            ax.set_ylabel('K')
            ax.set_zlabel('L')
            ax.set_title(f'Crystal Structure Visualization\nSphere size proportional to |Fc|² (size factor: {initial_size})')
            
            # Restore grid and aspect ratio
            ax.grid(True)
            ax.set_box_aspect([1,1,1])
            
            # Restore HKL info text
            ax.text2D(0.02, 0.98, f'HKL Data: {len(hkl_data)} reflections\nH: {h_min} to {h_max}\nK: {k_min} to {k_max}\nL: {l_min} to {l_max}', 
                      transform=ax.transAxes, fontsize=10, verticalalignment='top',
                      bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
            status_textbox.set_val(f'Showing all {len(hkl_data)} reflections\nH: {h_min}-{h_max}, K: {k_min}-{k_max}, L: {l_min}-{l_max}')
            fig.canvas.draw_idle()
    
    def reset_ranges(event):
        """Reset all range sliders to full range"""
        h_min_slider.set_val(h_min)
        h_max_slider.set_val(h_max)
        k_min_slider.set_val(k_min)
        k_max_slider.set_val(k_max)
        l_min_slider.set_val(l_min)
        l_max_slider.set_val(l_max)
        intensity_slider.set_val(intensity_min)
    
    def reset_size(event):
        """Reset size slider to initial value"""
        size_slider.set_val(initial_size)
    
    def clear_filter(event):
        """Clear all filters and show all data"""
        nonlocal current_colorbar
        
        reset_ranges(event)
        reset_size(event)
        toggle_button.label.set_text('Show All')
        
        # Remove existing colorbar to avoid overplotting
        if current_colorbar is not None:
            current_colorbar.remove()
        
        # Clear and recreate with all data
        ax.clear()
        
        # Recreate scatter plot with all data
        all_scatter = ax.scatter(original_h, original_k, original_l, 
                               s=initial_sizes, c=original_sizes, cmap='viridis', 
                               alpha=0.6)
        
        # Create new colorbar
        current_colorbar = plt.colorbar(all_scatter, label='|Fc|²')
        
        # Restore labels and title
        ax.set_xlabel('H')
        ax.set_ylabel('K')
        ax.set_zlabel('L')
        ax.set_title(f'Crystal Structure Visualization\nSphere size proportional to |Fc|² (size factor: {initial_size})')
        
        # Restore grid and aspect ratio
        ax.grid(True)
        ax.set_box_aspect([1,1,1])
        
        # Restore HKL info text
        ax.text2D(0.02, 0.98, f'HKL Data: {len(hkl_data)} reflections\nH: {h_min} to {h_max}\nK: {k_min} to {k_max}\nL: {l_min} to {l_max}', 
                  transform=ax.transAxes, fontsize=10, verticalalignment='top',
                  bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
        
        status_textbox.set_val(f'Showing all {len(hkl_data)} reflections\nH: {h_min}-{h_max}, K: {k_min}-{k_max}, L: {l_min}-{l_max}')
        fig.canvas.draw_idle()
    
    def set_preset_size(factor):
        def handler(event):
            size_slider.set_val(factor * max_size)
        return handler
    
    # Connect sliders and buttons
    h_min_slider.on_changed(lambda val: update_display())
    h_max_slider.on_changed(lambda val: update_display())
    k_min_slider.on_changed(lambda val: update_display())
    k_max_slider.on_changed(lambda val: update_display())
    l_min_slider.on_changed(lambda val: update_display())
    l_max_slider.on_changed(lambda val: update_display())
    intensity_slider.on_changed(lambda val: update_display())
    size_slider.on_changed(lambda val: update_display())
    
    toggle_button.on_clicked(toggle_visibility)
    reset_ranges_button.on_clicked(reset_ranges)
    reset_size_button.on_clicked(reset_size)
    clear_button.on_clicked(clear_filter)
    
    preset1.on_clicked(set_preset_size(2))
    preset2.on_clicked(set_preset_size(3))
    preset3.on_clicked(set_preset_size(5))
    
    # Add HKL info text on plot
    ax.text2D(0.02, 0.98, f'HKL Data: {len(hkl_data)} reflections\nH: {h_min} to {h_max}\nK: {k_min} to {k_max}\nL: {l_min} to {l_max}', 
              transform=ax.transAxes, fontsize=10, verticalalignment='top',
              bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    # Show the plot
    plt.show()

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Visualize crystal structure from HKL file with adjustable HKL range controls')
    parser.add_argument('filename', help='Input HKL file')
    parser.add_argument('-s', '--size', type=float, default=50.0,
                      help='Initial size factor for spheres (default: 50.0)')
    
    args = parser.parse_args()
    
    try:
        hkl_data = read_hkl_file(args.filename)
        if not hkl_data:
            print("No data found in the file or incorrect format.")
            sys.exit(1)
        plot_crystal_structure(hkl_data, args.size)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 