from django.db.models import TextChoices


class SexChoices(TextChoices):
    MALE = ("M", "Male")
    FEMALE = ("F", "Female")


class ApplicationStatusChoices(TextChoices):
    PENDING = ("P", "Pending")
    ACCEPTED = ("A", "Accepted")
    REJECTED = ("R", "Rejected")
