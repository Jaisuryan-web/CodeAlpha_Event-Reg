from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from events.models import Event

class Command(BaseCommand):
    help = 'Create sample events for testing'

    def handle(self, *args, **options):
        # Clear existing events
        Event.objects.all().delete()
        
        # Create sample events
        events_data = [
            {
                'title': 'Tech Innovation Summit 2024',
                'description': 'Join industry leaders and innovators for a day of cutting-edge technology discussions, workshops, and networking. Explore the latest trends in AI, blockchain, cloud computing, and more. This summit brings together tech enthusiasts, entrepreneurs, and experts to share knowledge and shape the future of technology.',
                'date': timezone.now() + timedelta(days=7),
                'location': 'Silicon Valley Convention Center, San Francisco, CA'
            },
            {
                'title': 'Digital Marketing Masterclass',
                'description': 'Learn advanced digital marketing strategies from industry experts. This comprehensive workshop covers SEO, social media marketing, content strategy, email campaigns, and analytics. Perfect for marketing professionals looking to upgrade their skills and drive better results for their brands.',
                'date': timezone.now() + timedelta(days=14),
                'location': 'Marketing Hub, New York, NY'
            },
            {
                'title': 'Startup Pitch Night',
                'description': 'Watch promising startups pitch their innovative ideas to a panel of venture capitalists and angel investors. This exciting event showcases the next generation of entrepreneurs and their groundbreaking solutions. Network with founders, investors, and industry professionals.',
                'date': timezone.now() + timedelta(days=21),
                'location': 'Innovation Lab, Austin, TX'
            },
            {
                'title': 'AI & Machine Learning Conference',
                'description': 'Dive deep into the world of artificial intelligence and machine learning. This conference features keynote speeches from leading AI researchers, hands-on workshops, and panel discussions on the ethical implications of AI. Learn about the latest breakthroughs and practical applications.',
                'date': timezone.now() + timedelta(days=10),
                'location': 'Tech Center, Boston, MA'
            },
            {
                'title': 'Web Development Bootcamp',
                'description': 'Intensive 3-day bootcamp covering modern web development technologies including React, Node.js, and cloud deployment. Perfect for beginners and intermediate developers looking to enhance their skills. Build real projects and learn from experienced developers.',
                'date': timezone.now() + timedelta(days=5),
                'location': 'Code Academy, Seattle, WA'
            },
            {
                'title': 'Cybersecurity Workshop',
                'description': 'Essential cybersecurity training for IT professionals. Learn about the latest security threats, defense strategies, and compliance requirements. Hands-on labs and real-world case studies help you understand how to protect your organization from cyber attacks.',
                'date': timezone.now() + timedelta(days=12),
                'location': 'Security Training Center, Washington, DC'
            },
            {
                'title': 'Product Management Excellence',
                'description': 'Master the art and science of product management. Learn product strategy, user research, roadmap planning, and cross-functional collaboration. This workshop is designed for product managers and entrepreneurs who want to build products that customers love.',
                'date': timezone.now() + timedelta(days=18),
                'location': 'Business Innovation Center, Chicago, IL'
            },
            {
                'title': 'Data Science & Analytics Summit',
                'description': 'Explore the power of data science and analytics in driving business decisions. This summit features data scientists from top companies sharing their experiences, tools, and techniques. Learn about data visualization, predictive modeling, and machine learning applications.',
                'date': timezone.now() + timedelta(days=25),
                'location': 'Analytics Hub, Los Angeles, CA'
            }
        ]

        created_events = []
        for event_data in events_data:
            event = Event.objects.create(**event_data)
            created_events.append(event)
            self.stdout.write(
                self.style.SUCCESS(f'Created event: {event.title}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(created_events)} sample events')
        )
