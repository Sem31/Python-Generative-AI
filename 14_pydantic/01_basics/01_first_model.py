from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {"id": 101, "name": "kamlesh", "is_active": True}
# input_data = {"id": "101", "name": "kamlesh", "is_active": 43}  Getting error because of is_active 43, it expecting Bool
# input_data = {"id": "101a", "name": "kamlesh", "is_active": True} Getting error because of id, you send string there.

user = User(**input_data)
print(f"User: {user}")

print("Start of pydantic first model example")
