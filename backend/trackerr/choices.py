from django.db.models import TextChoices
from django.forms import EmailField


class SexChoices(TextChoices):
    MALE = ("M", "Male")
    FEMALE = ("F", "Female")


class ApplicationStatusChoices(TextChoices):
    PENDING = ("P", "Pending")
    ACCEPTED = ("A", "Accepted")
    REJECTED = ("R", "Rejected")


class CompanyDetailTypeChoices(TextChoices):
    EMAIL = ("E", "Email")
    ADDRESS = ("A", "Company Address")
    CONTACT_NUMBER = ("C", "Contact Number")
