import builtins
import types
from _typeshed import ReadableBuffer, SupportsRead, SupportsWrite
from typing import Any
from typing_extensions import TypeAlias

version: int

_Marshallable: TypeAlias = (
    # handled in w_object() in marshal.c
    None
    | type[StopIteration]
    | builtins.ellipsis
    | bool
    # handled in w_complex_object() in marshal.c
    | int
    | float
    | complex
    | bytes
    | str
    | tuple[_Marshallable, ...]
    | list[Any]
    | dict[Any, Any]
    | set[Any]
    | frozenset[_Marshallable]
    | types.CodeType
    | ReadableBuffer
)

def dump(__value: _Marshallable, __file: SupportsWrite[bytes], __version: int = 4) -> None: ...
def load(__file: SupportsRead[bytes]) -> Any: ...
def dumps(__value: _Marshallable, __version: int = 4) -> bytes: ...
def loads(__bytes: ReadableBuffer) -> Any: ...
