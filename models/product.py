from sqlmodel import Field, SQLModel  # type: ignore


class Product(SQLModel, table=True):
    __tablename__ = "products"

    id: int = Field(primary_key=True)
    name: str
    img: str
    description: str
    price: float
    available: bool
    category_id: int
    created_at: str
    updated_at: str
