from typing import Annotated

from fastapi import FastAPI, File, UploadFile, Depends
from sqlmodel import Session
from contextlib import asynccontextmanager

from .models import Nyx, NyxSQL
from .db import init_db, get_session
from .get_text import get_text_from_img
from .regex_practice import format_text

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

# Já está mandando o texto extraido para o banco
@app.post('/uploadimages/', response_model=NyxSQL)
async def read_img(file: Annotated[UploadFile, File(description='Upload an image:')],
             session: Session = Depends(get_session)):
    image_file = await file.read()
    extracted_text = get_text_from_img(image_file)
    formatted_text = format_text(extracted_text)
#  Cósigo para selecionar o tipo de id entraria nessa linha.
    nyx = Nyx(id_tipo= 1, 
              fields=formatted_text)
    nyx_data = NyxSQL(id_tipo= nyx.id_tipo,
                      fields = nyx.fields)
    session.add(nyx_data)   
    session.commit()
    session.refresh(nyx_data)
    return nyx_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)