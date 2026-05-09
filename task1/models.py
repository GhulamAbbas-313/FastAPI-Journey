from pydantic import BaseModel
from pydantic import Field  

class Product(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    quantity: int = Field(ge=0)
    