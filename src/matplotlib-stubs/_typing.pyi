import decimal
import io

import numpy as np
import numpy.typing as npt
import pandas as pd
from typing_extensions import TypeAlias

Decimal = decimal.Decimal
PythonScalar: TypeAlias = str | int | float | bool

ArrayLike = npt.ArrayLike
FileLike = io.IOBase
PathLike = str

PandasScalar: TypeAlias = pd.Period | pd.Timestamp | pd.Timedelta | pd.Interval
Scalar: TypeAlias = PythonScalar | PandasScalar

RGBColor: TypeAlias = tuple[float, float, float]
RGBAColor: TypeAlias = tuple[np.float64, np.float64, np.float64, np.float64]
RGBAColorInt: TypeAlias = tuple[np.uint8, np.uint8, np.uint8, np.uint8]

Color: TypeAlias = RGBColor | RGBAColor | RGBAColorInt | str

__all__ = [
    "ArrayLike",
    "Color",
    "Decimal",
    "FileLike",
    "PathLike",
    "RGBAColor",
    "RGBAColorInt",
    "RGBColor",
    "Scalar",
]
