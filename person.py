from dataclasses import dataclass


@dataclass
class Person:
    name: str = None
    age: int = 0
    gender: str = None
    nationality: str = None

