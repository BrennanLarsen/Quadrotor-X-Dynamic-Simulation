import numpy as np
import pandas as pd
from pathlib import Path

from Motor_Inputs import open_loop_motor_inputs
from Dyn_Plots import plot_states

# ================================================== #
#    Assumptions
# ================================================== #
#  All state variables are directly measurable (perfect observability)
#  Sensor dynamics, noise, and filtering are neglected (ideal sensors)
#  Rotor thrust and drag are modeled using average/lumped coefficients, c_T and c_RD
#  The quadrotor is modeled as a rigid, unreformable body
#  Aerodynamic body drag, ground effects, rotor inertia (gyroscopic effects), and rotor flapping are neglected



# ================================================== #
#    Paths
# ================================================== #
data_path = Path(__file__).parent / "Data" / "Data1.xlsx"



# ================================================== #
#    Misc Sim Values  
# ================================================== #
t_tot = 120
dt = 0.05
g = 9.81
rad2deg = 180/np.pi
deg2rad = np.pi/180



# ================================================== #
# Control loop not currently implemented
# -------------------------------------------------- #
# If Ctrl = True  --> Att controlled
# If Ctrl = False --> Open loop
# ================================================== #
Ctrl = False 



# ================================================== #
#    Parameters 
# ================================================== #
m = 0.369                                            # Mass [kg]

# !! Inertia in the X-Config!!
I_x = 0.004856                                       # X-inertia [kg*m**2]
I_y = 0.004856                                       # Y-inertia [kg*m**2]
I_z = 0.008801                                       # Z-inertia [kg*m**2]

l = 0.225                                            # Arm length [m]
angle_motor1_2 = 90                                  # Angle between front motors (1 and 2) [deg]

c_T = 2.98e-06                                       # Thrust coefficient [(N*s^2)/(rad^2)]
c_RD = 1.14e-07                                      # Rotor drag coefficient [(N*m*s^2)/(rad^2)]



# ================================================== #
#    Rotation Matrices  
# ================================================== #
def Inertial2Body(phi, theta, psi, x, y, z):
    R_1 = np.array([[             1,            0,             0],
                    [             0,  np.cos(phi),  -np.sin(phi)],
                    [             0,  np.sin(phi),   np.cos(phi)]])
    R_2 = np.array([[ np.cos(theta),            0, np.sin(theta)],
                    [             0,            1,             0],
                    [-np.sin(theta),            0, np.cos(theta)]])
    R_3 = np.array([[   np.cos(psi), -np.sin(psi),             0],
                    [   np.sin(psi),  np.cos(psi),             0],
                    [             0,            0,             1]])
    R = R_3 @ R_2 @ R_1
    Inertial = np.array([x, y, z])
    Body = R @ Inertial
    return Body[0], Body[1], Body[2]

def Body2Inertial(phi, theta, p, q, r):
    R = np.array([[1, np.sin(phi) * np.tan(theta), np.cos(phi) * np.tan(theta)],
                  [0,                 np.cos(phi),                -np.sin(phi)],
                  [0, np.sin(phi) / np.cos(theta), np.cos(phi) / np.cos(theta)]])
    Vehicle = np.array([p, q, r])
    Inertial = R @ Vehicle
    return Inertial[0], Inertial[1], Inertial[2]



# ================================================== #
#    Dynamic Model  
# ================================================== #
def model():
    # ================================================== #
    #    Initial Values 
    # ================================================== #
    x = y = z = 0
    dx = dy = dz = 0
    ddx = ddy = ddz = 0

    u = v = w = 0
    du = dv = dw = 0

    phi = theta = psi = 0
    dphi = dtheta = dpsi = 0
    prev_dphi = prev_dtheta = prev_dpsi = 0.0
    ddphi = ddtheta = ddpsi = 0
    

    p = q = r = 0
    dp = dq = dr = 0

    u1 = u2 = u3 = u4 = 0
    omega_1 = omega_2 = omega_3 = omega_4 = 0
    F_T = M_x = M_y = M_z = 0



    # ================================================== #
    #    Effective Arm Length
    # ================================================== #
    arm_ang_23  = 180 - angle_motor1_2                   # [deg]
    l_x = l * np.sin(deg2rad * (arm_ang_23 / 2))         # [m]
    l_y = l * np.sin(deg2rad * (angle_motor1_2 / 2))     # [m]

    omega_h = np.sqrt((m*g)/(4*c_T))                     # [rad/sec]
    


    # ================================================== #
    #    Logging dictionary
    # ================================================== #
    logs = {i: [] for i in [
        "t", 
        "x", "y", "z", 
        "dx", "dy", "dz", 
        "ddx", "ddy", "ddz",
        
        "u", "v", "w",
        "du", "dv", "dw",

        "phi", "theta", "psi", 
        "dphi", "dtheta", "dpsi", 
        "ddphi", "ddtheta", "ddpsi",
        
        "p", "q", "r", 
        "dp", "dq", "dr",

        "omega_1", "omega_2", "omega_3", "omega_4",
        "F_T", "M_x", "M_y", "M_z",

        "m", 
        "I_x", "I_y", "I_z", 
        "l", "angle_motor1_2", 
        "c_T", "c_RD"
    ]}



    # ================================================== #
    #    Time loop
    # ================================================== #
    for t in np.arange(0, t_tot + dt, dt):
        if not Ctrl:
            u1, u2, u3, u4 = open_loop_motor_inputs(t, omega_h)

            omega_1, omega_2, omega_3, omega_4 = u1, u2, u3, u4

            F_T = c_T * (omega_1**2 + omega_2**2 + omega_3**2 + omega_4**2)
            M_x = l_y * c_T * (-omega_1**2 + omega_2**2 + omega_3**2 - omega_4**2)
            M_y = l_x * c_T * (-omega_1**2 - omega_2**2 + omega_3**2 + omega_4**2)
            M_z = c_RD * (omega_1**2 - omega_2**2 + omega_3**2 - omega_4**2)



        # ================================================= #
        #    Inertial frame linear dynamics
        # ================================================= #
        ddx = (F_T / m) * (np.cos(psi) * np.sin(theta) * np.cos(phi) + np.sin(psi) * np.sin(phi))
        ddy = (F_T / m) * (np.sin(psi) * np.sin(theta) * np.cos(phi) - np.cos(psi) * np.sin(phi))
        ddz = -g + (F_T / m) * (np.cos(theta) * np.cos(phi))
        dx += ddx * dt
        dy += ddy * dt
        dz += ddz * dt
        x += dx * dt
        y += dy * dt
        z += dz * dt

        # ================================================= #
        #    Body frame linear dynamics
        # ================================================= #
        u, v, w = Inertial2Body(phi, theta, psi, dx, dy, dz)
        du, dv, dw = Inertial2Body(phi, theta, psi, ddx, ddy, ddz)

        # ================================================= #
        #    Body frame angular dynamics 
        # ================================================= #
        dp = (((I_y - I_z) * q * r) / I_x) + (M_x / I_x)
        dq = (((I_z - I_x) * p * r) / I_y) + (M_y / I_y)
        dr = (((I_x - I_y) * p * q) / I_z) + (M_z / I_z)
        p += dp * dt
        q += dq * dt
        r += dr * dt

        # ================================================= #
        #    Inertial angular dynamics
        # ================================================= #
        dphi, dtheta, dpsi = Body2Inertial(phi, theta, p, q, r)
        ddphi = (dphi - prev_dphi) / dt
        ddtheta = (dtheta - prev_dtheta) / dt
        ddpsi = (dpsi - prev_dpsi) / dt
        phi += dphi * dt
        theta += dtheta * dt
        psi += dpsi * dt
        prev_dphi, prev_dtheta, prev_dpsi = dphi, dtheta, dpsi



# ================================================== #
#    Save data as text and/or Excel
# ================================================== #
        for key, value in {
            "t": t,
            "x": x, "y": y, "z": z,
            "dx": dx, "dy": dy, "dz": dz,
            "ddx": ddx, "ddy": ddy, "ddz": ddz,

            "u": u, "v": v, "w": w,
            "du": du, "dv": dv, "dw": dw,

            "phi": phi, "theta": theta, "psi": psi,
            "dphi": dphi, "dtheta": dtheta, "dpsi": dpsi,
            "ddphi": ddphi, "ddtheta": ddtheta, "ddpsi": ddpsi,

            "p": p, "q": q, "r": r,
            "dp": dp, "dq": dq, "dr": dr,

            "omega_1": omega_1, "omega_2": omega_2,
            "omega_3": omega_3, "omega_4": omega_4,
            "F_T": F_T, "M_x": M_x, "M_y": M_y, "M_z": M_z,

            "m": m,
            "I_x": I_x, "I_y": I_y, "I_z": I_z,
            "l": l, "angle_motor1_2": angle_motor1_2,
            "c_T": c_T, "c_RD": c_RD
        }.items():
            logs[key].append(value)


    return logs



# ================================================== #
#    Run, log and plot
# ================================================== #
logs = model()
df = pd.DataFrame(logs)
df.to_excel(data_path, index=False)
plot_states()