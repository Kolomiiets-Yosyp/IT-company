import os
import django
from django.core.files import File

# Налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tworix.settings')
django.setup()

from website.models import Project

# Шлях до директорії зі статичними файлами
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'website', 'static', 'images', 'projects')

# Очищення існуючих проектів
Project.objects.all().delete()

# Дані проектів
projects_data = [
    {
        "title": "Перероблення дизайну та архітектури програми для запису клієнтів фітнес-студії",
        "description": "Комплексне оновлення існуючої системи для покращення користувацького досвіду, оптимізації продуктивності та масштабованості. Створено інтуїтивно зрозумілий інтерфейс та впроваджено нову архітектуру бекенду.",
        "image_name": "fitness_app.jpg",
        "details": """
- Аналіз існуючої системи та виявлення слабких місць.
- Розробка нового UX/UI дизайну.
- Переписування бекенду з використанням сучасних фреймворків.
- Впровадження системи сповіщень для клієнтів.
- Тестування та розгортання оновленої програми.
""",
        "link": "http://example.com/fitness"
    },
    {
        "title": "Система обслуговування столиків у ресторані",
        "description": "Розробка веб-додатку для офіціантів, що дозволяє приймати замовлення, відправляти їх на кухню та керувати статусом столиків у режимі реального часу. Система інтегрована з існуючою POS-системою.",
        "image_name": "restaurant_system.jpg",
        "details": """
- Створення інтерфейсу для планшетів.
- Інтеграція з кухонним принтером та POS-системою.
- Розробка системи керування меню та замовленнями.
- Впровадження аналітики продажів.
- Навчання персоналу та підтримка.
""",
        "link": "http://example.com/restaurant"
    }
]

# Створення проектів
for data in projects_data:
    image_path = os.path.join(STATIC_DIR, data["image_name"])

    project = Project(
        title=data["title"],
        description=data["description"],
        details=data["details"],
        link=data["link"]
    )

    with open(image_path, 'rb') as f:
        project.image.save(data["image_name"], File(f), save=True)

    project.save()

print("Projects created successfully with local images.")
