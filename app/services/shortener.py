from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
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
    
def create_short_url(db: Session, url_data: url_schema.URLCreate) -> url_model.URL:
    utm_params = {
        "utm_source": url_data.utm_source,
        "utm_medium": url_data.utm_medium,
        "utm_campaign": url_data.utm_campaign,
        "utm_term": url_data.utm_term,
        "utm_content": url_data.utm_content
    }
    
    provided_utms = {k: v for k, v in utm_params.items() if v is not None}

    final_original_url = str(url_data.original_url)

    if provided_utms:
        parsed_url = urlparse(final_original_url)
        existing_params = parse_qs(parsed_url.query)
        existing_params.update(provided_utms)
        new_query_string = urlencode(existing_params, doseq=True)

        final_original_url = urlunparse(
            (parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params,
             new_query_string, parsed_url.fragment)
        )


    db_url = url_model.URL(original_url=final_original_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)

    short_code = to_base62(db_url.id)
    
    db_url.short_code = short_code
    db.commit()
    db.refresh(db_url)

    return db_url

def get_url_by_short_code(db: Session, short_code: str) -> url_model.URL | None:
    return db.query(url_model.URL).filter(url_model.URL.short_code == short_code).first()
    