# app/main.py
import os
from fastapi import FastAPI, Response
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
from urllib.parse import quote

from .models import OfferData

app = FastAPI(
    title="PDF Offer Generator API",
    description="API для генерации PDF-офферов с различными цветовыми схемами.",
    version="1.0.0"
)

# Настраиваем Jinja2 для работы с шаблонами
templates_dir = os.path.join(os.path.dirname(__file__), "templates")
env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template("offer_template.html")


@app.post("/generate-offer", tags=["PDF Generation"])
def generate_offer(data: OfferData):
    """
    Принимает данные в формате JSON и генерирует PDF-файл оффера.
    
    - **data**: JSON-объект с полями для оффера.
    - **Возвращает**: PDF-файл для скачивания.
    """
    context = data.dict()
    
    html_content = template.render(context)
    
    pdf_bytes = HTML(string=html_content).write_pdf()
    
    filename = f"Job_Offer_{data.candidate_name.replace(' ', '_')}.pdf"
    
    # Корректно кодируем имя файла для заголовка Content-Disposition
    content_disposition = f"attachment; filename*=UTF-8''{quote(filename)}"

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": content_disposition
        }
    )

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the PDF Offer Generator! Visit /docs for the API documentation."}