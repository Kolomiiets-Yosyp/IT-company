
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tworix.settings')
django.setup()

from website.models import Content

content_data = {
    'home_main_title': 'Tworix',
    'home_subtitle': 'Fragmented_Code',
    'home_description': 'A next-gen IT collective. We slice through legacy constraints to engineer',
    'home_description_highlight': 'fragmented intelligence',
    'home_description_cont': 'for the modern grid.',
    'home_cta_button': 'write a line',
    'capabilities_section_title': 'CORE_CAPABILITIES',
    'capabilities_section_subtitle': 'SLICED_',
    'capabilities_section_subtitle_highlight': 'INFRASTRUCTURE',
    'capabilities_section_description': "We don't build monolithic blocks. We deploy modular, fragmented architectures that evolve at the speed of the urban grid.",
    'capability_1_title': 'FRAGMENTED<br/>SYSTEMS',
    'capability_1_description': 'Decoupled software engineering that prioritizes resilience and rapid iteration cycles.',
    'capability_2_title': 'NEURAL<br/>GLITCH_AI',
    'capability_2_description': 'Advanced machine learning models designed to find patterns in chaotic, unstructured data environments.',
    'capability_3_title': 'URBAN_GRID<br/>CLOUD',
    'capability_3_description': 'Distributed cloud architecture that operates on the fringe, ensuring maximum uptime through decentralization.',
    'lab_section_title': 'EXPERIMENTAL<br/><span class="text-primary italic">LAB_</span>',
    'lab_section_description': 'Where we push the boundaries of fragmented aesthetics and high-performance computing.',
    'lab_section_cta': 'VIEW_MANIFESTO',
    'solutions_title': 'SOLUTIONS',
    'solutions_subtitle': 'We engineer fragmented intelligence. Our core capabilities are designed to slice through legacy constraints and build the future of the urban grid.',
    'capability_1_tag': 'CORE_CAPABILITY_01',
    'capability_1_long_description': 'We specialize in decoupled software engineering that prioritizes resilience, scalability, and rapid iteration cycles. Our approach allows for modular updates and fault isolation, ensuring your systems evolve without catastrophic failures. We build architectures that breathe, adapt, and scale at the speed of your needs.',
    'capability_2_tag': 'CORE_CAPABILITY_02',
    'capability_2_long_description': 'Our advanced machine learning models are designed to thrive in chaos. We find critical patterns in unstructured, high-volume data environments. From predictive analytics to anomaly detection, our Glitch_AI cuts through the noise to deliver actionable, fragmented intelligence where others only see static.',
    'capability_3_tag': 'CORE_CAPABILITY_03',
    'capability_3_long_description': 'We deploy distributed cloud architecture that operates on the fringe, ensuring maximum uptime and resilience through radical decentralization. Our infrastructure is built for the high-stakes environment of the modern urban grid, providing low-latency, secure, and continuously available services.',
    'connect_title': 'INITIALIZE_SYNC',
    'connect_subtitle': "We're at the edge of the grid. Open a channel.",
    'about_title': 'OUR_MANIFESTO',
    'about_subtitle': 'FRAGMENTED_INTELLIGENCE',
    'manifesto_1_title': '01. EMBRACE THE GLITCH',
    'manifesto_1_text': "Perfection is a fragile myth. We find strength in imperfection, opportunity in chaos. The glitch is not an error; it's a deviation, a new path, a source of unexpected innovation. We build systems that don't just tolerate noise, but learn from it.",
    'manifesto_2_title': '02. DECENTRALIZE OR DIE',
    'manifesto_2_text': "Monolithic structures are doomed to collapse. The future is a distributed network of autonomous, intelligent fragments. We champion radical decentralization to create resilient, anti-fragile systems that thrive on the edge, far from any single point of failure.",
    'manifesto_3_title': '03. RECODE REALITY',
    'manifesto_3_text': "The urban grid is our canvas. Code is our medium. We don't just write software; we rewrite the operating system of our cities. We see technology not as a tool, but as a fundamental force for reshaping the physical world. Every line of code is an architectural act.",
    'manifesto_4_title': '04. DATA IS THE GHOST',
    'manifesto_4_text': "Data is the ghost in the machine, the invisible layer that animates the physical world. We harness this spectral force, transforming raw, chaotic data streams into fragmented intelligence that provides clarity, foresight, and a decisive strategic advantage.",
}

for key, value in content_data.items():
    Content.objects.get_or_create(key=key, defaults={'value': value})

print('Content seeded successfully.')
