from pydantic import BaseModel


class UserInput(BaseModel):
    Price: float
    Stock: int
    Rating: float
    Reviews_Count: int
    Previous_Sales: float
    Discount_Percentage: float
    Transaction_Quantity: int
    Holiday_Flag: int
    Month: int
    Category: str
    Brand: str
    Region: str