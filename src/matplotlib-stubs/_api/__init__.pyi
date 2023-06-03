import functools
from collections.abc import Callable, Generator, Iterable

from .deprecation import (
    MatplotlibDeprecationWarning,
)

class classproperty:
    def __init__(
        self, fget: Callable, fset: None = ..., fdel: None = ..., doc: None = ...,
    ) -> None: ...
    def __get__(self, instance, owner): ...
    @property
    def fget(self): ...

def check_isinstance(**kwargs) -> None: ...
def check_in_list(
    _values: Iterable, *, _print_supported_values: bool = True, **kwargs,
) -> None: ...
def check_shape(**kwargs) -> None: ...
def check_getitem(_mapping: dict, **kwargs): ...
def caching_module_getattr(cls) -> functools._lru_cache_wrapper: ...
def define_aliases(
    alias_d: dict[str, list[str]], cls: None = ...,
) -> functools.partial: ...
def select_matching_signature(funcs: list[Callable], *args, **kwargs): ...
def recursive_subclasses(cls) -> Generator: ...
def warn_external(
    message: MatplotlibDeprecationWarning | PendingDeprecationWarning | str,
    category: None | type[MatplotlibDeprecationWarning] = ...,
) -> None: ...
