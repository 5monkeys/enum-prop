from __future__ import annotations

import enum

import pytest

from enum_prop import enum_property


def test_can_define_property() -> None:
    class A(enum.Enum):
        a = 1
        b = 2
        c = 3
        prop = enum_property({a: 300, b: 5000, c: 70000})

    assert A.a.prop == 300
    assert A.b.prop == 5000
    assert A.c.prop == 70000


def test_incomplete_mapping_raises_attribute_error() -> None:
    class B(enum.Enum):
        a = "a"
        b = "b"
        val = enum_property({a: 1})

    assert B.a.val == 1

    with pytest.raises(AttributeError, match=r"B.b has no attribute 'val'"):
        B.b.val

def test_getting_enum_property() -> None:
    class C(enum.Enum):
        a = "a"
        b = "b"
        val = enum_property({a: 1, b: 2})

    assert C.val
    assert C.val.bound_name is "val"
