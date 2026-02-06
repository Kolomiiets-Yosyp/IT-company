
import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tworix.settings')
django.setup()

from website.models import Project, ProjectMedia

# Clear existing data
Project.objects.all().delete()
ProjectMedia.objects.all().delete()

# --- Create Project 1: Fragmented Systems ---
project1 = Project.objects.create(
    title="Fragmented Systems",
    description="Decoupled software engineering that prioritizes resilience and rapid iteration cycles.",
    intro_title="Fragmented Systems: A Modular Approach",
    intro_description="This project showcases a software architecture that breaks down monolithic structures into smaller, independent services. This allows for greater flexibility, easier maintenance, and resilience against system-wide failures.",
    phase01_title="Phase 01",
    phase01_subtitle="Architectural Blueprint",
    phase01_description="The initial phase focused on designing a scalable and resilient microservices architecture. Key features include service discovery, load balancing, and containerization using Docker.",
    phase01_feature1="Containerized services with Docker",
    phase01_feature2="Service discovery with Consul",
    phase01_button_text="View on GitHub",
    link="https://github.com/example/fragmented-systems",
    phase02_title="Phase 02",
    phase02_subtitle="Tech Stack & Implementation",
    phase02_description="The system is built on a modern tech stack, emphasizing performance and reliability. Python and Go are used for backend services, with a React-based frontend for a dynamic user experience."
)

# --- Create Project 2: Neural Glitch_AI ---
project2 = Project.objects.create(
    title="Neural Glitch_AI",
    description="Advanced machine learning models designed to find patterns in chaotic, unstructured data environments.",
    intro_title="Neural Glitch_AI: Uncovering Hidden Patterns",
    intro_description="This project explores the use of advanced machine learning to analyze and interpret complex datasets. The 'glitch' aspect refers to its ability to find meaningful signals in noisy, seemingly random data.",
    phase01_title="Phase 01",
    phase01_subtitle="Data Modeling & Analysis",
    phase01_description="The core of this project is a custom-built neural network that uses unsupervised learning to identify anomalies and trends. It has been trained on a diverse range of datasets, from financial markets to network traffic.",
    phase01_feature1="Custom neural network architecture",
    phase01_feature2="Unsupervised learning for anomaly detection",
    phase01_button_text="Read the Research Paper",
    link="https://example.com/research/neural-glitch-ai",
    phase02_title="Phase 02",
    phase02_subtitle="Tech Stack & Performance",
    phase02_description="The AI model is implemented in Python using TensorFlow and Keras. The data processing pipeline is optimized for performance, leveraging parallel computing to handle large-scale datasets."
)

# --- Create Project 3: Urban_Grid Cloud ---
project3 = Project.objects.create(
    title="Urban_Grid Cloud",
    description="Distributed cloud architecture that operates on the fringe, ensuring maximum uptime through decentralization.",
    intro_title="Urban_Grid Cloud: A Decentralized Future",
    intro_description="This project is a decentralized cloud platform designed for high-availability and low-latency applications. It leverages a distributed network of nodes to provide resilient and secure cloud services.",
    phase01_title="Phase 01",
    phase01_subtitle="Network & Infrastructure",
    phase01_description="The foundation of the Urban_Grid Cloud is a peer-to-peer network that ensures data redundancy and fault tolerance. The infrastructure is designed to be self-healing, with automatic failover and load balancing.",
    phase01_feature1="Peer-to-peer network architecture",
    phase01_feature2="Automated failover and self-healing",
    phase01_button_text="Explore the Network",
    link="https://example.com/urban-grid-cloud",
    phase02_title="Phase 02",
    phase02_subtitle="Tech Stack & Security",
    phase02_description="The platform is built with Go and Rust for performance and security. It uses advanced cryptographic techniques to ensure data integrity and confidentiality across the distributed network."
)

# --- Add Media to Projects ---
# Define the path to your static images
static_image_path = os.path.join(os.path.dirname(__file__), 'website', 'static', 'images', 'test_image.png')

# Check if the image file exists
if os.path.exists(static_image_path):
    with open(static_image_path, 'rb') as f:
        image_name = os.path.basename(static_image_path)
        image_file = File(f, name=image_name)

        # Add multiple media items to Project 1
        ProjectMedia.objects.create(
            project=project1,
            media_type='image',
            image=image_file
        )
        ProjectMedia.objects.create(
            project=project1,
            media_type='image',
            image=image_file
        )

        # Add media to Project 2
        ProjectMedia.objects.create(
            project=project2,
            media_type='image',
            image=image_file
        )

        # Add media to Project 3
        ProjectMedia.objects.create(
            project=project3,
            media_type='image',
            image=image_file
        )

        print("Media items added to projects successfully.")
else:
    print(f"Image file not found at: {static_image_path}")

print("Projects and media created successfully.")
