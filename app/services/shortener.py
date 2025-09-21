from sqlalchemy.orm import Session
from app.schemas import url_schema
from app.models import url as url_model
from math import remainder

BASE62_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base62(number: int) -> str:
    if number == 0:
        return BASE62_CHARS[0]
    result = []

    while number > 0:
        number, remainder = divmod(number, 62)
        result.append(BASE62_CHARS[remainder])
    
    return "".join(reversed(result))
    
def create_short_url(db: Session, url_schema: url_schema.URLCreate) -> url_model.URL:
    db_url = url_model.URL (original_url = str(url_schema.original_url))
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    short_code = to_base62(db_url.id)
    
    db_url.short_code = short_code
    db.commit()
    db.refresh(db_url)

    return db_url

def get_url_by_short_code(db: Session, short_code: str) -> URL | None:
    return db.query(URL).filter(URL.short_code == short_code).first()
    