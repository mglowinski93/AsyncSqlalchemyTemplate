from dataclasses import dataclass


@dataclass(frozen=True)
class Template:
    id: int
    value: int
