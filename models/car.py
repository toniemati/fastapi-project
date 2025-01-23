from sqlmodel import Field, SQLModel  # type: ignore


class Car(SQLModel, table=True):
    __tablename__ = "cars"

    id: int = Field(primary_key=True)
    plates: str
    bussy: bool
    mileage: float
    created_at: str
    updated_at: str
