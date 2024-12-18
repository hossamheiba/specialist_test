from django.core.management.base import BaseCommand
from Book_Service.models import UnavailableDate
from datetime import datetime

class Command(BaseCommand):
    help = "Delete unavailable dates that have passed."

    def handle(self, *args, **kwargs):
        today = datetime.today().date()
        # حذف التواريخ التي انتهت
        deleted_count, _ = UnavailableDate.objects.filter(date__lt=today).delete()
        self.stdout.write(self.style.SUCCESS(f"Successfully deleted {deleted_count} expired dates"))
