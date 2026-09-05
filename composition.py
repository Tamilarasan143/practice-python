
from dataclasses import dataclass

@dataclass
class Department:
    name:str
    def change_department(self,department):
         self.name = department