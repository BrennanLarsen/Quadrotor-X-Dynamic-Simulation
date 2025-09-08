# Quadrotor-X-Dynamic-Simulation

This repository contains simulations of a quadrotor in the **X-configuration**, implemented in both **MATLAB** and **Python**.  

The project demonstrates quadrotor dynamics, including motor inputs, system response, and visualization through plots and animations.  

For details on the mathematical modeling and equations used, see **[Simulating Quadrotor(X) Dynamics.pdf](./Simulating%20Quadrotor(X)%20Dynamics.pdf)**.  

Several simplifying assumptions are made but the simulation is sufficiently accurate for most uses.

These simulations provide foundation for further studies, including trajectory planning, feedback control, and system identification. 

---

## Repo Structure  

### Python-Simulation  
- **`X-Quad.py`** – Main simulation script. Runs the dynamic model and logs simulation data into an Excel file.  
- **`Motor_Inputs.py`** – Defines the open-loop sequence of motor commands for controlling the quadrotor.  
- **`Dyn_Plots.py`** – Generates plots of the simulated quadrotor dynamics.  

### MATLAB-Simulation  
- **`X_quad.m`** – Main simulation file.  
- **`Motor_inputs.m`** – Open-loop motor input sequence.  
- **`EulerRot.m`** – Handles Euler rotation calculations.  
- **`X_3D_Plot.m`** – Animates the quadrotor dynamics in 3D.  
- **`X_Plotting.m`** – Creates traditional 2D plots of the system response.  




