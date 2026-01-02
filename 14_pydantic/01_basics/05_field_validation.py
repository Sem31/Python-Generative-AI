from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username: str

    @field_validator("username")
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v


data = {"username": "kam"}

user = User(**data)
print(f"user: {user}")


class SignupData(BaseModel):
    password: str
    confirm_passowrd: str

    @model_validator(mode="after")  # access all the values at same time
    def password_match(cls, values):
        if values.password != values.confirm_passowrd:
            raise ValueError("Password do not match")
        return values
