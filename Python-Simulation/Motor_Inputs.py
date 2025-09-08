# Motor_Inputs.py
import numpy as np

def open_loop_motor_inputs(t, omega_h):
    # ================================================= #
    #    Thrust
    # ================================================= #
    small_thrust_up =   ( 3,  3,  3,  3)  
    small_thrust_down = (-3, -3, -3, -3)
    large_thrust_up =   ( 9,  9,  9,  9)  
    large_thrust_down = (-9, -9, -9, -9)
    
    # ================================================= #
    #    Roll (motors 1&4 vs 2&3)
    # ================================================= #
    small_roll_forward =  (0.1, 0.0, 0.0, 0.1)
    small_roll_backward = (0.0, 0.1, 0.1, 0.0)
    large_roll_forward =  (0.3, 0.0, 0.0, 0.3)
    large_roll_backward = (0.0, 0.3, 0.3, 0.0)
    
    # ================================================= #
    #    Pitch (motors 2&3 vs 1&4)
    # ================================================= #
    small_pitch_forward =  (0.0, 0.0, 0.1, 0.1)
    small_pitch_backward = (0.1, 0.1, 0.0, 0.0)
    large_pitch_forward =  (0.0, 0.0, 0.3, 0.3)
    large_pitch_backward = (0.3, 0.3, 0.0, 0.0)
    
    # ================================================= #
    #    Yaw (diagonal motors pairs)
    # ================================================= #
    yaw_cw =  ( 0.1, -0.1,  0.1, -0.1)
    yaw_ccw = (-0.1,  0.1, -0.1,  0.1)
    
    # ================================================= #
    #    Maintain (open loop) hover
    # ================================================= #
    neutral = (0, 0, 0, 0)
    
    offsets = [
        # THRUST MOVEMENTS 
        neutral,             # 0:   0.00 – 1.25s
        small_thrust_up,     # 1:   1.25 – 2.50s
        neutral,             # 2:   2.50 – 3.75s
        small_thrust_down,   # 3:   3.75 – 5.00s
        neutral,             # 4:   5.00 – 6.25s
        neutral,             # 5:   6.25 – 7.50s
        large_thrust_up,     # 6:   7.50 – 8.75s
        large_thrust_down,   # 7:   8.75 – 10.00s
        
        # ROLL MOVEMENTS 
        neutral,             # 8:   10.00 – 11.25s
        small_thrust_up,     # 9:   11.25 – 12.50s
        neutral,             # 10:  12.50 – 13.75s
        small_roll_forward,  # 11:  13.75 – 15.00s
        small_roll_backward, # 12:  15.00 – 16.25s
        small_roll_backward, # 13:  16.25 – 17.50s
        small_roll_forward,  # 14:  17.50 – 18.75s
        small_roll_backward, # 15:  18.75 – 20.00s
        small_roll_forward,  # 16:  20.00 – 21.25s
        small_roll_forward,  # 17:  21.25 – 22.50s
        small_roll_backward, # 18:  22.50 – 23.75s
        neutral,             # 19:  23.75 – 25.00s
        large_roll_backward, # 20:  25.00 – 26.25s
        large_roll_forward,  # 21:  26.25 – 27.50s
        large_roll_forward,  # 22:  27.50 – 28.75s
        large_roll_backward, # 23:  28.75 – 30.00s
        large_roll_forward,  # 24:  30.00 – 31.25s
        large_roll_backward, # 25:  31.25 – 32.50s
        large_roll_backward, # 26:  32.50 – 33.75s
        large_roll_forward,  # 27:  33.75 – 35.00s

        # PITCH MOVEMENTS
        neutral,             # 28:  35.00 – 36.25s
        small_thrust_down,   # 29:  36.25 – 37.50s
        neutral,             # 30:  37.50 – 38.75s
        small_pitch_forward, # 31:  38.75 – 40.00s
        small_pitch_backward,# 32: 40.00 – 41.25s
        small_pitch_backward,# 33: 41.25 – 42.50s
        small_pitch_forward, # 34: 42.50 – 43.75s
        small_pitch_backward,# 35: 43.75 – 45.00s
        small_pitch_forward, # 36:  45.00 – 46.25s
        small_pitch_forward, # 37: 46.25 – 47.50s
        small_pitch_backward,# 38: 47.50 – 48.75s
        neutral,             # 39:  48.75 – 50.00s
        large_pitch_backward,# 40: 50.00 – 51.25s
        large_pitch_forward, # 41: 51.25 – 52.50s
        large_pitch_forward, # 42: 52.50 – 53.75s
        large_pitch_backward,# 43: 53.75 – 55.00s
        large_pitch_forward, # 44: 55.00 – 56.25s
        large_pitch_backward,# 45: 56.25 – 57.50s
        large_pitch_backward,# 46: 57.50 – 58.75s
        large_pitch_forward, # 47: 58.75 – 60.00s

        # YAW MOVEMENTS
        neutral,             # 48:  60.00 – 61.25s
        small_thrust_up,     # 49:  61.25 – 62.50s
        small_thrust_up,     # 50:  62.50 – 63.75s
        yaw_cw,              # 51:  63.75 – 65.00s
        yaw_ccw,             # 52:  65.00 – 66.25s
        yaw_ccw,             # 53:  66.25 – 67.50s
        yaw_cw,              # 54:  67.50 – 68.75s
        
        # PITCH MOVEMENTS
        small_pitch_forward, # 55:  68.75 – 70.00s
        small_pitch_backward,# 56:  70.00 – 71.25s
        small_pitch_backward,# 57:  71.25 – 72.50s
        small_pitch_forward, # 58:  72.50 – 73.75s
        small_pitch_backward,# 59:  73.75 – 75.00s
        small_pitch_forward, # 60:  75.00 – 76.25s
        small_pitch_forward, # 61:  76.25 – 77.50s
        small_pitch_backward,# 62:  77.50 – 78.75s

        # ROLL MOVEMENTS
        small_roll_backward, # 63:  78.75 – 80.00s
        small_roll_forward,  # 64:  80.00 – 81.25s
        small_roll_forward,  # 65:  81.25 – 82.50s
        small_roll_backward, # 66:  82.50 – 83.75s
        small_roll_forward,  # 67:  83.75 – 85.00s
        small_roll_backward, # 68:  85.00 – 86.25s
        small_roll_backward, # 69:  86.25 – 87.50s
        small_roll_forward,  # 70:  87.50 – 88.75s

        # YAW MOVEMENTS
        yaw_ccw,             # 71:  88.75 – 90.00s
        yaw_cw,              # 72:  90.00 – 91.25s
        yaw_cw,              # 73:  91.25 – 92.50s
        yaw_ccw,             # 74:  92.50 – 93.75s
        large_thrust_up,     # 75:  93.75 – 95.00s
        neutral,             # 76:  95.00 – 96.25s
        large_thrust_down,   # 77:  96.25 – 97.50s
        neutral,             # 78:  97.50 – 98.75s
        neutral,             # 79:  98.75 – 100.00s

        # ROLL MOVEMENTS
        large_roll_forward,  # 80:  100.00 – 101.25s
        large_roll_backward, # 81:  101.25 – 102.50s
        large_roll_backward, # 82:  102.50 – 103.75s
        large_roll_forward,  # 83:  103.75 – 105.00s
        large_roll_backward, # 84:  105.00 – 106.25s
        large_roll_forward,  # 85:  106.25 – 107.50s
        large_roll_forward,  # 86:  107.50 – 108.75s
        large_roll_backward, # 87:  108.75 – 110.00s

        # PITCH MOVEMENTS
        large_pitch_forward, # 88:  110.00 – 111.25s
        large_pitch_backward,# 89:  111.25 – 112.50s
        large_pitch_backward,# 90:  112.50 – 113.75s
        large_pitch_forward, # 91:  113.75 – 115.00s
        large_pitch_backward,# 92:  115.00 – 116.25s
        large_pitch_forward, # 93:  116.25 – 117.50s
        large_pitch_forward, # 94:  117.50 – 118.75s
        large_pitch_backward,# 95:  118.75 – 120.00s
    ]
    
    # ================================================= #
    #    Calculate time bin 
    # ================================================= #
    idx = int(t // 1.25)
    
    # ================================================= #
    #    Apply offsets
    # ================================================= #
    if 0 <= idx < len(offsets):
        o1, o2, o3, o4 = offsets[idx]
        u1 = omega_h + o1
        u2 = omega_h + o2
        u3 = omega_h + o3
        u4 = omega_h + o4
    else:
        # ================================================= #
        #    Default to hover for times outside sequence
        # ================================================= #
        u1 = u2 = u3 = u4 = omega_h
    
    # ================================================= #
    #    Prevent negative motor speeds
    # ================================================= #
    u1 = max(u1, 0)
    u2 = max(u2, 0)
    u3 = max(u3, 0)
    u4 = max(u4, 0)
    
    return u1, u2, u3, u4