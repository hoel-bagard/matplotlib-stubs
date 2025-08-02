# COMPLETE

from collections.abc import Mapping
from pathlib import Path
from typing import Any, Union

from typing_extensions import TypeAlias

_Style: TypeAlias = Union[str, Path, Mapping[str, Any]]
_StyleOrList: TypeAlias = Union[_Style, list[_Style]]

def context(style: _StyleOrList, after_reset: bool = ...) -> None: ...
def reload_library() -> None: ...
def use(style: _StyleOrList) -> None: ...

library: dict[str, Any]
available: list[str]
