import matplotlib.pyplot as plt
import numpy as np
from fluorescence_loader.compute_intensity import Compute_with_asrry, ComputeMean_with_asrry, Compute_tot_max, Auto_ROI_brightest_region, Compute_intensity_timeframe


def plot_intensity(mean_intensity):
    plt.plot(mean_intensity, marker='o')
    plt.xlabel("Time frame")
    plt.ylabel("Mean intensity")
    plt.title("Fluorescence Intensity vs Time")
    plt.grid()
    plt.show()

def plot_intensity_realtime(times, mean_intensity):
    plt.plot(times, mean_intensity, marker='o')
    plt.xlabel("Time (minutes)")
    plt.ylabel("Mean intensity")
    plt.title("Intensity vs Time (real time)")
    plt.grid()
    plt.show()

def plot_tot_max_median(tot, max_int, median):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, constrained_layout=True)

    # Plot on first axis
    ax1.plot(tot, 'tab:orange')
    ax1.set_xlabel("Time frame")
    ax1.set_title('Total Intensity')

    # Plot on second axis
    ax2.plot(max_int, 'tab:green')
    ax2.set_xlabel("Time frame")
    ax2.set_title('Maximum Intensity')
    
    ax3.plot(max_int, 'tab:purple')
    ax3.set_xlabel("Time frame")
    ax3.set_title('Median')
 
    plt.show()

def plot_auto_roi(time, mean_intensity, visroi=None):
    plt.plot(time, mean_intensity, marker='.', color= "green", linestyle='None')
    plt.xlabel("Time")
    plt.ylabel("ROI intensity")
    plt.title("Auto ROI Intensity vs Time")
    plt.show()

    if(visroi):
        plt.imshow(first_frame, cmap='gray')
        plt.scatter([x], [y], color='red', s=50)
        plt.title("Auto ROI center")
        plt.show()

def plot_xy_intensity(vmin, vmax, data, indices, n_plots = 10):
    # -----------------------------
    # CREATE GRID PLOT
    # -----------------------------
    ncols = 5
    nrows = int(np.ceil(n_plots / ncols))

    # -----------------------------
    # SELECT FRAMES (evenly spaced)
    # -----------------------------

    #indices = np.linspace(0, T - 1, n_plots, dtype=int)
    print("Selected frames:", indices)


    fig, axes = plt.subplots(2, 5, figsize=(15, 6))

    axes = axes.ravel()

    # -----------------------------
    # PLOT EACH FRAME (X,Y IMAGE)
    # -----------------------------
    for ax, idx in zip(axes, indices):
        frame = data[idx].compute()

        im = ax.imshow(frame, cmap='gray', vmin=vmin, vmax=vmax)
        ax.set_title(f"T={idx}")
        ax.axis('off')

    plt.subplots_adjust(wspace=0.1, hspace=0.3)
    plt.show()

    plt.savefig("time_series_grid.png", dpi=300)


def main():

    mean_intensity = ComputeMean_with_asrry()
    #print("Intensity", mean_intensity)

    #time = RealTime_Extract()
       
    mean_intensity = np.array(mean_intensity)

    # x-axis (time index)
    time = np.arange(len(mean_intensity))

    print("time shape:", np.shape(time))
    print("mean shape:", np.shape(mean_intensity))

    #plot_intensity(mean_intensity)  #open it

    dt = 15 / 94
    times = np.arange(94) * dt

    #plot_intensity_realtime(times, mean_intensity #Open it)

    total_intn, max_intn, median =  Compute_tot_max()
    
    #plot_tot_max_median(total_intn, max_intn, median) #open it

    #print(f"tot: {total_intn} : max_intn : {max_intn} : median {median}")

    intensity_roi_mean = Auto_ROI_brightest_region()
    time = np.arange(len(intensity_roi_mean))

    #plot_auto_roi(time, intensity_roi_mean) #open it

    n_plots = 10

    vmin, vmax, data_intensity, indices  = Compute_intensity_timeframe(10)
    plot_xy_intensity(vmin, vmax, data_intensity, indices)

    


if __name__ == "__main__":
    main()


