import numpy as np
import matplotlib.pyplot as plt
from euler_py.euler import euler_solve

def projectile_ode(t, y):
    x,y,vx,vy = y

    k = 0.25 # constante de friccion con el aire

    dx_dt = vx
    dy_dt = vy
    dvx_dt = -k*vx 
    dvy_dt = -9.8 - k*vy
    return np.array([dx_dt, dy_dt, dvx_dt, dvy_dt])

def analytical_solution(t, x0,y0,vx0,vy0):
    x = x0 + vx0*t
    y = y0 + vy0*t - 1/2*9.8*t**2
    vx = vx0 * np.ones_like(t)
    vy = vy0 - 9.8*t 
    return np.column_stack([x,y,vx,vy])

t, y_euler = euler_solve(projectile_ode, y0=[0,0,20,20], ti=0, tf=4, h=0.01)
y_analytical = analytical_solution(t, 0,0,20,20)

plt.figure(figsize=(12,10))

plt.subplot(2,1,1)
plt.plot(y_euler[:,0], y_euler[:,1], 'o-', label='Euler')
plt.plot(y_analytical[:,0], y_analytical[:,1], 'x-', label='Analytical')
plt.xlabel('Horizontal distance(m)')
plt.ylabel('Vertical distance(m)')
plt.title('Projectile motion')
plt.grid(True)
plt.legend()

plt.subplot(2,1,2)
plt.plot(t, y_euler[:,1], 'o-', label='Euler')
plt.plot(t, y_analytical[:,1], 'x-', label='Analytical')
plt.xlabel('Time(s)')
plt.ylabel('Vertical distance(m)')
plt.title('Projectile motion')
plt.grid(True)
plt.legend()

plt.show()

