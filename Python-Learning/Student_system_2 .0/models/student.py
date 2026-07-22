class Student:
    def __init__(self,id,name,score):
        self.id = id
        self.name = name
        self.score = score
    
    def to_dict(self):
        return {
            "id":self.id,
            "name":self.name,
            "score":self.score
        }
    
    @classmethod
    def from_dict(cls,data):
        return cls(
            data["id"],
            data["name"],
            data["score"]
        )