from weasyprint import HTML
from datetime import datetime

def create_offer_pdf(data, template_path='offer_template.html', output_path='job_offer.pdf'):
    """
    Создает PDF-файл с оффером на основе HTML-шаблона.

    :param data: Словарь с данными для вставки в шаблон.
    :param template_path: Путь к HTML-шаблону.
    :param output_path: Путь для сохранения готового PDF-файла.
    """
    try:
        # Читаем HTML-шаблон
        with open(template_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Заменяем плейсхолдеры на реальные данные
        for key, value in data.items():
            html_content = html_content.replace(f'{{{{ {key} }}}}', str(value))

        # Создаем PDF
        html = HTML(string=html_content)
        html.write_pdf(output_path)

        print(f"🎉 PDF-оффер успешно создан и сохранен как '{output_path}'")

    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")

if __name__ == '__main__':
    # --- Заполните здесь данные для оффера ---
    offer_data = {
        "candidate_name": "Иван Иванов",
        "position_title": "Senior Python Developer",
        "company_name": "Tech Solutions Inc.",
        "department": "IT-департамент",
        "start_date": "1 октября 2025 г.",
        "salary": "250 000 руб.",
        "deadline_date": "26 сентября 2025 г.",
        "hiring_manager_name": "Елена Петрова",
        "hiring_manager_title": "Руководитель отдела разработки",
        "company_address": "ул. Технологическая, д. 1, Москва, Россия",
        "company_phone": "+7 (495) 123-45-67",
        "date": datetime.now().strftime("%d %B %Y г.")
    }

    # Генерируем PDF
    create_offer_pdf(offer_data)