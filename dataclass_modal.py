
from typing import Optional
from dataclasses import dataclass
@dataclass
class Project:
    name:str
    technology: Optional[str] = None