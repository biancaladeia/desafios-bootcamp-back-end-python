from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum

# Tipos de roles
class Role(str, Enum):
    role_1 = "admin"
    role_2 = "aluna"
    role_3 = "instrutora"

# Tipos de informações de cada item da lista
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    email: str
    role: List[Role]