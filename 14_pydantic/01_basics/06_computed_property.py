from pydantic import BaseModel, computed_field, Field


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field()
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


print(Product(price=3, quantity=2).model_dump())


# This is useful for fields that are computed from other fields, or for fields that are expensive to compute and should be cached.


class Rectangle(BaseModel):
    width: int
    length: int

    @computed_field
    @property
    def area(self) -> int:
        return self.width * self.length


print(Rectangle(width=3, length=2).model_dump())
# > {'width': 3, 'length': 2, 'area': 6}


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_nights: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_nights


booking = Booking(user_id=1, room_id=101, nights=1, rate_per_nights=600.0)

print(f"Total price of room 1 day: {booking.total_amount}")
print(f"Total price of room 1 day: {booking.model_dump()}")
