# Dyn_Plots.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

rad2deg = 180 / np.pi

def plot_states():
    # ================================================== #
    #    Load Excel and extract data
    # ================================================== #
    data_path = Path(__file__).parent / "Data" / "Data1.xlsx"
    df = pd.read_excel(data_path)



    t = df["t"].to_numpy()

    x, y, z = df["x"].to_numpy(), df["y"].to_numpy(), df["z"].to_numpy()
    dx, dy, dz = df["dx"].to_numpy(), df["dy"].to_numpy(), df["dz"].to_numpy()
    ddx, ddy, ddz = df["ddx"].to_numpy(), df["ddy"].to_numpy(), df["ddz"].to_numpy()

    phi, theta, psi = df["phi"].to_numpy(), df["theta"].to_numpy(), df["psi"].to_numpy()
    p, q, r = df["p"].to_numpy(), df["q"].to_numpy(), df["r"].to_numpy()
    dp, dq, dr = df["dp"].to_numpy(), df["dq"].to_numpy(), df["dr"].to_numpy()



    # ================================================== #
    #    Create two columns for fig
    # ================================================== #
    fig, axes = plt.subplots(3, 2, sharex=True, figsize=(12, 10))
    ax_left = axes[:, 0]                                 # left column (3 subplots)
    ax_right = axes[:, 1]                                # right column (3 subplots)



    # ================================================= #
    #    Left column:
    #    x, y, z pos, vel, and acc
    # ================================================= #
    ax_left[0].plot(t, x, label="x [m]")
    ax_left[0].plot(t, y, label="y [m]")
    ax_left[0].plot(t, z, label="z [m]")
    ax_left[0].set_ylabel("Inertial Pos.")
    ax_left[0].legend(loc="upper right", fontsize=8)
    ax_left[0].grid(True)

    ax_left[1].plot(t, dx, label="$\dot{x}$ [m/s]")
    ax_left[1].plot(t, dy, label="$\dot{y}$ [m/s]")
    ax_left[1].plot(t, dz, label="$\dot{z}$ [m/s]")
    ax_left[1].set_ylabel("Inertial Vel.")
    ax_left[1].legend(loc="upper right", fontsize=8)
    ax_left[1].grid(True)

    ax_left[2].plot(t, ddx, label="$\ddot{x}$ [m/s²]")
    ax_left[2].plot(t, ddy, label="$\ddot{y}$ [m/s²]")
    ax_left[2].plot(t, ddz, label="$\ddot{z}$ [m/s²]")
    ax_left[2].set_ylabel("Inertial Acc.")
    ax_left[2].legend(loc="upper right", fontsize=8)
    ax_left[2].grid(True)
    ax_left[2].set_xlabel("Time [s]")



    # ================================================= #
    #    Right column: 
    #    Euler angles, vel, and acc
    # ================================================= #
    ax_right[0].plot(t, phi * rad2deg, label=  "phi [deg]")
    ax_right[0].plot(t, theta * rad2deg, label="theta [deg]")
    ax_right[0].plot(t, psi * rad2deg, label=  "psi [deg]")
    ax_right[0].set_ylabel("Euler Angles")
    ax_right[0].legend(loc="upper right", fontsize=8)
    ax_right[0].grid(True)

    ax_right[1].plot(t, p * rad2deg, label="p [deg/s]")
    ax_right[1].plot(t, q * rad2deg, label="q [deg/s]")
    ax_right[1].plot(t, r * rad2deg, label="r [deg/s]")
    ax_right[1].set_ylabel("Body Rates")
    ax_right[1].legend(loc="upper right", fontsize=8)
    ax_right[1].grid(True)

    ax_right[2].plot(t, dp * rad2deg, label="$\dot{p}$ [deg/s²]")
    ax_right[2].plot(t, dq * rad2deg, label="$\dot{q}$ [deg/s²]")
    ax_right[2].plot(t, dr * rad2deg, label="$\dot{r}$ [deg/s²]")
    ax_right[2].set_ylabel("Body Acc.")
    ax_right[2].legend(loc="upper right", fontsize=8)
    ax_right[2].grid(True)
    ax_right[2].set_xlabel("Time [s]")

    fig.suptitle("Quadrotor Dynamics\n", fontsize=16)
    fig.tight_layout()
    plt.show()
