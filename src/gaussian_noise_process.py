import numpy as np

class GaussianNoiseProcess:
    def __init__(self,
                 *,
                 dimensions,
                 noise_scale=0.1):
        self._dimensions = dimensions
        self._noise_scale = noise_scale

    def reset(self):
      pass

    def simulate(self):
      return np.random.normal(scale=self._noise_scale, size=self._dimensions)
