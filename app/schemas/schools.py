from pydantic import BaseModel, EmailStr


class SchoolScheme(BaseModel):
    area: str
    city: str
    phone: str
    fax: str
    email: EmailStr
    site_url: str | None = None
