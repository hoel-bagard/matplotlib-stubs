import decimal
import io

import numpy.typing
import numpy as np
import pandas as pd

Decimal = decimal.Decimal
PythonScalar = str | int | float | bool

ArrayLike = numpy.typing.ArrayLike
FileLike = io.IOBase
PathLike = str

PandasScalar = pd.Period | pd.Timestamp | pd.Timedelta | pd.Interval
Scalar = PythonScalar | PandasScalar

RGBColor = tuple[float, float, float]
RGBAColor = tuple[np.float_, np.float_, np.float_, np.float_]
RGBAColorBytes = tuple[np.uint8, np.uint8, np.uint8, np.uint8]

Color = RGBColor | RGBAColor | RGBAColorBytes | str

__all__ = [
    "ArrayLike",
    "Color",
    "Decimal",
    "FileLike",
    "PathLike",
    "RGBAColor",
    "RGBAColorBytes",
    "RGBColor",
    "Scalar",
]
