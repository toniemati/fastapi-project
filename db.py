from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query  # type: ignore
from sqlmodel import Session, select, create_engine  # type: ignore


sqlite_file_name = "burgir.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
