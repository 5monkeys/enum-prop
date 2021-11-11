from __future__ import annotations

import enum

import pytest

from enum_prop import enum_property

from django.db.models import IntegerChoices, TextChoices

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


def test_django_choices():
    class D(TextChoices):
        LOW = "one", "test"
        MEDIUM = "two",
        HIGH = "three",
        colour = enum_property({LOW: "green", MEDIUM: "yellow", HIGH: "red"})

    assert D.LOW.colour == "green"
    assert D.MEDIUM.colour == "yellow"

    class E(IntegerChoices):
        LOW = 1, "test"
        MEDIUM = 2,
        HIGH = 3,
        colour = enum_property({LOW: "green", MEDIUM: "yellow", HIGH: "red"})

    assert D.LOW.colour == "green"
    assert D.MEDIUM.colour == "yellow"
