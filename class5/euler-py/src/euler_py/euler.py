import numpy as np

def euler_solve(f, y0, ti, tf, h):
    """
    Solve the ODE y' = f(t, y) using Euler's method.

    Parameters
    ----------
    f : callable
        The function f(t, y) that defines the right-hand side of the ODE.
    y0 : float or ndarray
        The initial condition y(t0) = y0.
    ti : float
        The initial time t0.
    tf : float
        The final time t.
    h : float
        The time step size.

    Returns
    -------
    t : ndarray
        The array of time values.
    y : ndarray
        The array of solution values.
    """
    
    n_steps = int((tf - ti) / h) +1

    y0 = np.array(y0, dtype=float)
    #1 -> [1]
    scalar_input = False
    if y0.ndim == 0:
        y0 = y0.reshape(1)
        scalar_input = True
    
    y = np.zeros((n_steps, len(y0)))
    t = np.linspace(ti, tf, n_steps)

    y[0] = y0 
    t[0] = ti

    for i in range(0, n_steps-1):
        y[i+1] = y[i] + h * f(t[i], y[i]) #metodo de euler

    if scalar_input:
        y = y.flatten()

    return t, y
