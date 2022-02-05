from django.contrib.auth.models import User


def print_stats():
    print(len(User.objects.all()))
