from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_one = Product(id=101, name="Laptop", price=14323.2, in_stock=True)
product_two = Product(id=102, name="Mobile", price=1432.32)


# pydantic is convert for you

# int - "123" -> 123
# bool - "true" -> True
# float - 123 -> 123.0
