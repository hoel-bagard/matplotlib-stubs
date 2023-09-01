import decimal
import io

import numpy.typing
import pandas as pd

Decimal = decimal.Decimal
PythonScalar = str | int | float | bool

ArrayLike = numpy.typing.ArrayLike
FileLike = io.IOBase
PathLike = str

PandasScalar = pd.Period | pd.Timestamp | pd.Timedelta | pd.Interval
Scalar = PythonScalar | PandasScalar

RGBColor = tuple[float, float, float]
RGBAColor = tuple[float, float, float, float]

Color = RGBColor | RGBAColor | str

__all__ = [
    "ArrayLike",
    "Color",
    "Decimal",
    "FileLike",
    "PathLike",
    "RGBAColor",
    "RGBColor",
    "Scalar",
]
