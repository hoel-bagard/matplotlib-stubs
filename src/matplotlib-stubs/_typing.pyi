import decimal
import io
from pathlib import Path
from typing import Any, Callable, Literal, Sequence, TypedDict

import numpy as np
import numpy.typing as npt
import pandas as pd
from matplotlib._enums import CapStyle, JoinStyle
from matplotlib.artist import Artist
from matplotlib.backend_bases import Event
from matplotlib.figure import Figure, SubFigure
from matplotlib.markers import MarkerStyle
from matplotlib.patheffects import AbstractPathEffect
from matplotlib.transforms import BboxBase, Transform
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

class SketchParams(TypedDict, total=False):
    scale: float
    length: float
    randomness: float

class Line2DProperty(TypedDict, total=False):
    agg_filter: Callable[[npt.NDArray, float], tuple[npt.NDArray, int, int]]
    alpha: float | None
    animated: bool
    antialiased: bool
    aa: bool
    clip_box: BboxBase | None
    clip_on: bool
    clip_path: Path | tuple[Path, Transform] | None
    color: Color
    c: Color
    dash_capstyle: CapStyle | Literal["butt", "projecting", "round"]
    dash_joinstyle: JoinStyle | Literal["miter", "round", "bevel"]
    dashes: Sequence[float] | tuple[None, None]
    data: npt.NDArray | tuple[npt.NDArray]
    drawstyle: Literal["default", "steps", "steps-pre", "steps-mid", "steps-post"]
    ds: Literal["default", "steps", "steps-pre", "steps-mid", "steps-post"]
    figure: Figure | SubFigure
    fillstyle: Literal["full", "left", "right", "bottom", "top", "none"]
    gapcolor: Color | None
    gid: str
    in_layout: bool
    label: object
    linestyle: (
        Literal["-", "solid", "--", "dashed", "-.", "dashdot", ":", "dotted", "", "none", "None", " "]
        | tuple[int, Sequence[int]]
    )
    ls: (
        Literal["-", "solid", "--", "dashed", "-.", "dashdot", ":", "dotted", "", "none", "None", " "]
        | tuple[int, Sequence[int]]
    )
    linewidth: float
    lw: float
    marker: str | Path | MarkerStyle
    markeredgecolor: Color
    mec: Color
    markeredgewidth: float
    mew: float
    markerfacecolor: Color
    mfc: Color
    markerfacecoloralt: Color
    mfcalt: Color
    markersize: float
    ms: float
    markevery: None | int | tuple[int, int] | slice | list[int] | float | tuple[float, float] | list[bool]
    mouseover: bool
    path_effects: list[AbstractPathEffect]
    picker: float | Callable[[Artist, Event], tuple[bool, dict]]
    pickradius: float
    rasterized: bool
    sketch_params: SketchParams
    snap: bool | None
    solid_capstyle: CapStyle | Literal["butt", "projecting", "round"]
    solid_joinstyle: JoinStyle | Literal["miter", "round", "bevel"]
    transform: Any
    url: str
    visible: bool
    xdata: npt.NDArray
    ydata: npt.NDArray
    zorder: float

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
