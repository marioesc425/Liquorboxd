from django.core.management.base import BaseCommand
from spirits.models import Spirit

class Command(BaseCommand):
    help = 'Seeds the database with sample spirits'

    def handle(self, *args, **kwargs):
        spirits_data = [
            {'name': 'Buffalo Trace', 'category': 'Whiskey', 'brand': 'Buffalo Trace', 'abv': 45.0, 'description': 'A classic, approachable Kentucky bourbon with notes of vanilla and caramel.'},
            {'name': 'Maker\'s Mark', 'category': 'Whiskey', 'brand': 'Maker\'s Mark', 'abv': 45.0, 'description': 'A wheated bourbon known for its smooth, sweet finish.'},
            {'name': 'Jameson', 'category': 'Whiskey', 'brand': 'Jameson', 'abv': 40.0, 'description': 'A smooth, triple-distilled Irish whiskey.'},
            {'name': 'Tito\'s Handmade Vodka', 'category': 'Vodka', 'brand': 'Tito\'s', 'abv': 40.0, 'description': 'A smooth, corn-based vodka distilled in Austin, Texas.'},
            {'name': 'Grey Goose', 'category': 'Vodka', 'brand': 'Grey Goose', 'abv': 40.0, 'description': 'A premium French vodka made from winter wheat.'},
            {'name': 'Ketel One', 'category': 'Vodka', 'brand': 'Ketel One', 'abv': 40.0, 'description': 'A classic Dutch vodka with a crisp, clean taste.'},
            {'name': 'Bacardi Superior', 'category': 'Rum', 'brand': 'Bacardi', 'abv': 40.0, 'description': 'A light, versatile white rum great for cocktails.'},
            {'name': 'Captain Morgan Spiced', 'category': 'Rum', 'brand': 'Captain Morgan', 'abv': 35.0, 'description': 'A spiced rum with notes of vanilla and caramel.'},
            {'name': 'Mount Gay Eclipse', 'category': 'Rum', 'brand': 'Mount Gay', 'abv': 40.0, 'description': 'A smooth Barbadian rum with a rich, oaky flavor.'},
            {'name': 'Patrón Silver', 'category': 'Tequila', 'brand': 'Patrón', 'abv': 40.0, 'description': 'A smooth, 100% agave silver tequila.'},
            {'name': 'Casamigos Blanco', 'category': 'Tequila', 'brand': 'Casamigos', 'abv': 40.0, 'description': 'A clean, citrusy blanco tequila.'},
            {'name': 'Don Julio Reposado', 'category': 'Tequila', 'brand': 'Don Julio', 'abv': 38.0, 'description': 'A rich, oak-aged tequila with vanilla notes.'},
            {'name': 'Hendrick\'s Gin', 'category': 'Gin', 'brand': 'Hendrick\'s', 'abv': 44.0, 'description': 'A Scottish gin infused with rose and cucumber.'},
            {'name': 'Tanqueray London Dry', 'category': 'Gin', 'brand': 'Tanqueray', 'abv': 47.3, 'description': 'A classic juniper-forward London dry gin.'},
            {'name': 'Bombay Sapphire', 'category': 'Gin', 'brand': 'Bombay Sapphire', 'abv': 47.0, 'description': 'A smooth gin infused with ten exotic botanicals.'},
        ]

        for spirit in spirits_data:
            spirit_obj, created = Spirit.objects.get_or_create(
                name=spirit['name'],
                defaults={
                    'category': spirit['category'],
                    'brand': spirit['brand'],
                    'abv': spirit['abv'],
                    'description': spirit['description'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created {spirit['name']}"))
            else:
                self.stdout.write(f"{spirit['name']} already exists, skipping")