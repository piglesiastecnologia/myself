from django.utils.translation import gettext_lazy as _

from django.db import models


# Create your models here.
class Person(models.Model):
    class Gender(models.TextChoices):
        FEMALE = 'F', _('Female')
        MALE = 'M', _('Male')
        OTHER = 'Other', _('Other')

    first_name = models.CharField(max_length=155, blank=False, null=False)
    last_name = models.CharField(max_length=155, blank=False, null=False)
    email = models.EmailField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=30, choices=Gender.choices)
    other_gender = models.CharField(max_length=25)
    phone = models.CharField(max_length=30)

    summary = models.TextField()

    job_position = models.CharField(max_length=100)


class PersonAddress(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    street_number = models.IntegerField()


class PersonSocialMedia(models.Model):
    class SocialMedia(models.TextChoices):
        FB = 'FB', _('Facebook')
        IG = 'IG', _('Instagram')
        LINKEDIN = 'LINKEDIN', _('Linkedin')
        OTHER = 'Other', _('Other')

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    socialmedia = models.CharField(max_length=30, choices=SocialMedia.choices)


class PersonLanguages(models.Model):
    class Type(models.IntegerChoices):
        LISTENING = 1
        READING = 2
        SPEAKING = 3
        WRITING = 4

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    language = models.CharField(max_length=50)
    type = models.IntegerField(choices=Type.choices)
    proficiency = models.IntegerField()

