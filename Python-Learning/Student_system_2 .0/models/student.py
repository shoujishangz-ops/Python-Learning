from __future__ import annotations
from dataclasses import dataclass,field,asdict
from datetime import datetime



@dataclass
class Student:

    id: int
    name: str
    score: float
    create_at : datetime = field(default_factory = datetime.now)
    
    def to_dict(self) -> dict:
        data = asdict(self)
        data["create_at"] = self.create_at.isoformat()
        return data
    
    @classmethod
    def from_dict(cls,data: dict) -> Student:
        return cls(
            id = data["id"],
            name = data["name"],
            score = data["score"],
            create_at = datetime.fromisoformat(data["create_at"])
        )
