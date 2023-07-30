from django.core.management.base import BaseCommand, CommandError
from News.models import Post, Category


class Command(BaseCommand):
    help = 'delete post in category'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Do you really want to delete all articles in the category {options["category"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('cancel'))
            return
        try:
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(postCategory=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {category.name}'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category'))



















