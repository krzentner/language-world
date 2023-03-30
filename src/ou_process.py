import numpy as np


class OUProcess:
    r"""An implementation of a Ornstein-Uhlenbeck process.

    The process is governed by the following stochastic differential equation.

    .. math::
       dx_t = -\theta(\mu - x_t)dt + \sigma \sqrt{dt} \mathcal{N}(\mathbb{0}, \mathbb{1})  # noqa: E501

    Args:
        dimensions (int): Number of dimensions of the process.
        mu (float): :math:`\mu` parameter of this OU process. This is the drift
            component.
        sigma (float): :math:`\sigma > 0` parameter of this OU process. This is
            the coefficient for the Wiener process component. Must be greater
            than zero.
        theta (float): :math:`\theta > 0` parameter of this OU process. Must be
            greater than zero.
        dt (float): Time-step quantum :math:`dt > 0` of this OU process. Must
            be greater than zero.
        x0 (float): Initial state :math:`x_0` of this OU process.

    """

    def __init__(self, *, dimensions, mu=0, sigma=0.3, theta=0.15, dt=1e-2, x0=None):
        self._dimensions = dimensions
        self._mu = mu
        self._sigma = sigma
        self._theta = theta
        self._dt = dt
        self._x0 = x0 if x0 is not None else self._mu * np.zeros(self._dimensions)
        self._state = self._x0

    def simulate(self):
        """Advance the OU process.

        Returns:
            np.ndarray: Updated OU process state.

        """
        x = self._state
        dx = self._theta * (self._mu - x) * self._dt + self._sigma * np.sqrt(
            self._dt
        ) * np.random.normal(size=len(x))
        self._state = x + dx
        return self._state

    def reset(self):
        """Reset the state of the process."""
        self._state = self._x0
