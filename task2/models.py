from pydantic import BaseModel
from pydantic import Field

class Inventory(BaseModel):
    id: int = Field(ge=1)
    name: str = Field(min_length=3)
    stock: int 
    
    
    
    