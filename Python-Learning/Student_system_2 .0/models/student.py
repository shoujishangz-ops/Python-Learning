class Student:
    def __init__(self,id: int,name: str,score: float):
        self.id = id
        self.name = name
        self.score = score
    
    def to_dict(self) -> None:
        return {
            "id":self.id,
            "name":self.name,
            "score":self.score
        }
    
    @classmethod
    def from_dict(cls,data) -> None:
        return cls(
            data["id"],
            data["name"],
            data["score"]
        )