from sqlalchemy.orm import Session
from app.schemas.url import URLCreate
from app.models.url import URL
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
    
def create_short_url(db: Session, url: URLCreate) -> URL:
    db_url = URL(original_url = str(URL.original_url))
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
    