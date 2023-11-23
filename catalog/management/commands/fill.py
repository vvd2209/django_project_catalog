from django.core.management import BaseCommand
from catalog.models import Category

class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()

        category_list = [
            {'name': 'Торты', 'description': 'Торты - это настоящее произведение мастерства, которое обязательно оставит яркие впечатления. У нас каждый найдёт то, что придется ему по душе, а главное - по вкусу. Вся продукция производится из натуральных ингредиентов, без добавления химических добавок, ароматизаторов и эмульгаторов.'},
            {'name': 'Пирожные', 'description': 'Торты - это настоящее произведение мастерства, которое обязательно оставит яркие впечатления. У нас каждый найдёт то, что придется ему по душе, а главное - по вкусу. Вся продукция производится из натуральных ингредиентов, без добавления химических добавок, ароматизаторов и эмульгаторов.'},
            {'name': 'Пироги', 'description': 'Пирог - это не просто блюдо, а лакомство, любимое с самого детства. Наши пироги не оставят равнодушным даже искушенного гурмана. Вся продукция производится из натуральных ингредиентов, без добавления химических добавок, ароматизаторов и эмульгаторов.'},
        ]


        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)

