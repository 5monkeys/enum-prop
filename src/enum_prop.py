"""
Enum definitions can't, for good reasons, reference instances of themselves within their
own definitions. This module allows definitions to come around that by using the enums'
names for lookups, hidden behind a special dict subclass. This allows enum definitions
to look tidy, and avoids having to define instance-specific configuration as property
functions.

Usage:

>>> import enum
>>> class Vehicle(enum.Enum):
...     car = "car"
...     bike = "bike"
...     unicycle = "unicycle"
...     wheels = enum_property({car: 4, bike: 2, unicycle: 1})
...     __int__ = enum_getter({car: 4, bike: 2, unicycle: 1})
>>> Vehicle.unicycle.wheels
1
>>> Vehicle.car.wheels
4
>>> int(Vehicle.unicycle)
1
>>> int(Vehicle.bike)
2
"""

from __future__ import annotations

from enum import Enum
from typing import Callable
from typing import Generic
from typing import Mapping
from typing import TypeVar
from typing import cast

__version__ = "0.0.0a1"
__all__ = ("enum_property", "enum_getter")

K = TypeVar("K")
V = TypeVar("V")


class EnumDict(dict[K, V], Generic[K, V]):
    def __getitem__(self, item: K | Enum) -> V:
        if isinstance(item, Enum):
            return super().__getitem__(item.value)
        return super().__getitem__(item)


E = TypeVar("E")


def enum_getter(mapping: Mapping[K, V]) -> Callable[[E], V]:
    getter = EnumDict(mapping).__getitem__

    def method(self: E) -> V:
        assert isinstance(self, Enum)
        return getter(self)

    return method


def enum_property(mapping: Mapping[K, V]) -> V:
    # Trick mypy into thinking this just returns a plain V, since property isn't
    # generic.
    return cast(V, property(enum_getter(mapping)))
