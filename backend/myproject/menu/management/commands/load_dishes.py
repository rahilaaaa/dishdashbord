from django.core.management.base import BaseCommand
from menu.models import Dish
import json

class Command(BaseCommand):
    help = 'Load dishes data from JSON file'

    def handle(self, *args, **kwargs):
        data = [
            {"dishName": "Jeera Rice", "dishId": "1", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/jeera-rice.jpg", "isPublished": True},
            {"dishName": "Paneer Tikka", "dishId": "2", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/paneer-tikka.jpg", "isPublished": True},
            {"dishName": "Rabdi", "dishId": "3", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/rabdi.jpg", "isPublished": True},
            {"dishName": "Chicken Biryani", "dishId": "4", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/chicken-biryani.jpg", "isPublished": True},
            {"dishName": "Alfredo Pasta", "dishId": "5", "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/alfredo-pasta.jpg", "isPublished": True}
        ]
        for dish_data in data:
            Dish.objects.update_or_create(dishId=dish_data['dishId'], defaults=dish_data)
        self.stdout.write(self.style.SUCCESS('Successfully loaded dishes data'))
