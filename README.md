<h1 align=center>enum-prop</h1>

Enum definitions can't, for good reasons, reference instances of themselves within their
own definitions. This module allows definitions to come around that by mapping the names
of enums for lookups, hidden behind a special dict subclass. This allows enum
definitions to remain tidy, and avoids having to define instance-specific configuration
as property functions.

### Usage

```python
import enum
from enum_prop import enum_property, enum_getter

class Vehicle(enum.Enum):
    car = "car"
    bike = "bike"
    unicycle = "unicycle"
    wheels = enum_property({car: 4, bike: 2, unicycle: 1})
    __int__ = enum_getter({car: 4, bike: 2, unicycle: 1})

print(Vehicle.unicycle.wheels)  # 1
print(Vehicle.car.wheels)  # 4
print(int(Vehicle.unicycle))  # 1
print(int(Vehicle.bike))  # 2
```
