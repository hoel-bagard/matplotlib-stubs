import numpy as np

from .triangulation import Triangulation

class TriAnalyzer:
    def __init__(self, triangulation: Triangulation) -> None: ...
    @property
    def scale_factors(self) -> tuple[float, float]: ...
    def circle_ratios(self, rescale: bool = True): ...
    def get_flat_tri_mask(
        self, min_circle_ratio: float = 0.01, rescale: bool = True,
    ) -> np.ndarray: ...
