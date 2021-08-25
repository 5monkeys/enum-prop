from __future__ import annotations

import enum

import pytest

from enum_prop import enum_getter


def test_can_define_getter() -> None:
    class A(enum.Enum):
        a = 1
        b = 2
        c = 3
        __int__ = enum_getter({a: 300, b: 5000, c: 70000})

    assert int(A.a) == 300
    assert int(A.b) == 5000
    assert int(A.c) == 70000


def test_incomplete_mapping_raises_key_error() -> None:
    class B(enum.Enum):
        a = "a"
        b = "b"
        __int__ = enum_getter({a: 1})

    assert int(B.a) == 1

    with pytest.raises(KeyError, match=""):
        int(B.b)
