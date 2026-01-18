import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tworix.settings')
django.setup()

from website.models import Project

Project.objects.all().delete()

Project.objects.create(
    title="Fragmented Systems",
    description="Decoupled software engineering that prioritizes resilience and rapid iteration cycles."
)

Project.objects.create(
    title="Neural Glitch_AI",
    description="Advanced machine learning models designed to find patterns in chaotic, unstructured data environments."
)

Project.objects.create(
    title="Urban_Grid Cloud",
    description="Distributed cloud architecture that operates on the fringe, ensuring maximum uptime through decentralization."
)

print("Projects created successfully.")
