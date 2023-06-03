from typing import Literal, overload

import numpy as np
from matplotlib._typing import *

from .triangulation import Triangulation
from .trifinder import TriFinder

__all__ = ("TriInterpolator", "LinearTriInterpolator", "CubicTriInterpolator")

class TriInterpolator:
    def __init__(
        self, triangulation: Triangulation, z: ArrayLike, trifinder: TriFinder = ...,
    ) -> None: ...

class LinearTriInterpolator(TriInterpolator):
    def __init__(
        self,
        triangulation: Triangulation,
        z: ArrayLike,
        trifinder: TriFinder = ...,
    ) -> None: ...
    def __call__(self, x: ArrayLike, y: ArrayLike) -> np.ndarray: ...
    def gradient(self, x: ArrayLike, y: ArrayLike) -> list: ...

class CubicTriInterpolator(TriInterpolator):
    def __init__(
        self,
        triangulation: Triangulation,
        z: ArrayLike,
        kind: Literal["min_E", "geom", "user"] = ...,
        trifinder: TriFinder = ...,
        dz: tuple = ...,
    ) -> None: ...
    def __call__(self, x: ArrayLike, y: ArrayLike) -> np.ndarray: ...
    def gradient(self, x: ArrayLike, y: ArrayLike)-> list: ...

class _ReducedHCT_Element:

    M: np.ndarray = ...
    M0: np.ndarray = ...
    M1: np.ndarray = ...
    M2: np.ndarray = ...
    rotate_dV: np.ndarray = ...
    rotate_d2V: np.ndarray = ...
    n_gauss = ...
    gauss_pts: np.ndarray = ...
    gauss_w: np.ndarray = ...
    E: np.ndarray = ...
    J0_to_J1: np.ndarray = ...
    J0_to_J2: np.ndarray = ...

    def get_function_values(
        self, alpha: np.ndarray, ecc: np.ndarray, dofs: np.ndarray,
    ) -> np.ndarray: ...
    def get_function_derivatives(
        self, alpha: np.ndarray, J: np.ndarray, ecc: np.ndarray, dofs: np.ndarray,
    ) -> np.ndarray: ...
    def get_function_hessians(
        self, alpha: np.ndarray, J: np.ndarray, ecc: np.ndarray, dofs: np.ndarray,
    ) -> np.ndarray: ...
    def get_d2Sidksij2(self, alpha: np.ndarray, ecc: np.ndarray): ...
    def get_bending_matrices(self, J: np.ndarray, ecc: np.ndarray): ...
    @overload
    def get_Hrot_from_J(
        self, J: np.ndarray, return_area: Literal[True],
    ) -> tuple[np.ndarray, np.ndarray]: ...
    @overload
    def get_Hrot_from_J(self, J: np.ndarray, return_area=...) -> np.ndarray: ...
    def get_Kff_and_Ff(
        self, J: np.ndarray, ecc: np.ndarray, triangles: np.ndarray, Uc: np.ndarray,
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: ...

class _DOF_estimator:
    def __init__(self, interpolator, **kwargs) -> None: ...
    def compute_dz(self, **kwargs): ...
    def compute_dof_from_df(self) -> np.ndarray: ...
    @staticmethod
    def get_dof_vec(
        tri_z: np.ndarray, tri_dz: np.ndarray, J: np.ndarray,
    ) -> np.ndarray: ...

class _DOF_estimator_user(_DOF_estimator):
    def compute_dz(self, dz): ...

class _DOF_estimator_geom(_DOF_estimator):
    def compute_dz(self) -> np.ndarray: ...
    def compute_geom_weights(self) -> np.ndarray: ...
    def compute_geom_grads(self) -> np.ndarray: ...

class _DOF_estimator_min_E(_DOF_estimator_geom):
    def __init__(self, Interpolator) -> None: ...
    def compute_dz(self) -> np.ndarray: ...

class _Sparse_Matrix_coo:
    def __init__(
        self, vals: np.ndarray, rows: np.ndarray, cols: np.ndarray, shape: tuple,
    ) -> None: ...
    def dot(self, V) -> np.ndarray: ...
    def compress_csc(self) -> None: ...
    def compress_csr(self) -> None: ...
    def to_dense(self) -> np.ndarray: ...
    def __str__(self) -> str: ...
    @property
    def diag(self) -> np.ndarray: ...
