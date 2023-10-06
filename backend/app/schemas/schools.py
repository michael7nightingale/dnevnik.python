from pydantic import BaseModel, EmailStr


class SchoolScheme(BaseModel):
    address: str
    name: str
    phone: str
    fax: str | None = None
    email: EmailStr
    site_url: str | None = None
