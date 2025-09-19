# app/models.py
from pydantic import BaseModel, Field
from datetime import datetime

class OfferData(BaseModel):
    """Модель данных для генерации оффера."""
    candidate_name: str = Field(..., example="Иван Иванов")
    position_title: str = Field(..., example="Senior Python Developer")
    company_name: str = Field(..., example="Tech Solutions Inc.")
    department: str = Field(..., example="IT-департамент")
    salary: str = Field(..., example="250 000 руб.")
    start_date: str = Field(..., example="1 октября 2025 г.")
    deadline_date: str = Field(..., example="26 сентября 2025 г.")
    hiring_manager_name: str = Field(..., example="Елена Петрова")
    hiring_manager_title: str = Field(..., example="Руководитель отдела разработки")
    company_address: str = Field(..., example="ул. Технологическая, д. 1, Москва")
    company_phone: str = Field(..., example="+7 (495) 123-45-67")
    
    # Поле date с текущей датой по умолчанию
    date: str = Field(default_factory=lambda: datetime.now().strftime("%d %B %Y г."))