from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.schemas import url_schema
from app.services import shortener
from app.database import get_db

router = APIRouter()

@router.post("/urls", response_model=url_schema.URLInfo, status_code=201)
def create_url(url: url_schema.URLCreate, request: Request, db: Session = Depends(get_db)):
    base_url = str(request.base_url)
    if base_url in str(url.original_url):
        raise HTTPException(status_code=400, detail="Não foi possível encurtar esta URL através deste domínio")
    
    db_url = shortener.create_short_url(db = db, url_data=url)
    
    response_data  = url_schema.URLInfo(
        original_url = db_url.original_url,
        short_code = db_url.short_code,
        created_at = db_url.created_at,
        short_url = f"{str(request.base_url)}{db_url.short_code}"
    )

    return response_data

@router.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    db_url = shortener.get_url_by_short_code(db=db, short_code=short_code)

    if db_url is None:
        raise HTTPException(status_code=404, detail="URL não encontrada")
    
    return RedirectResponse(url=db_url.original_url, status_code=307)