import numpy as np
import matplotlib.pyplot as plt
from euler_py.euler import euler_solve

def heat_transfer_ode(t, T):
    k = 0.1 # constante de transferencia de calor
    T_env = 20 # temperatura ambiente
    dT_dt = k *(T_env - T)

    return np.array([dT_dt])

def analytical_solution(t, T0):
    k = 0.1
    T_env = 20
    return T_env + (T0 - T_env)*np.exp(-k*t)

t, T_euler = euler_solve(heat_transfer_ode, y0 = 100, ti = 0, tf=50, h=0.001)
T_analytical = analytical_solution(t, 100)

plt.figure(figsize=(10,6))
plt.plot(t, T_euler, 'o-', label='Euler')
plt.plot(t, T_analytical, 'x-', label='Analytical')

plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Heat transfer')
plt.grid(True)
plt.legend()
plt.show()
