from django.db import models


class Member(models.Model):

    def __str__(self):
        return (self.first_name + " " + self.last_name).title()

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    current_membership = models.BooleanField(default=False)
    card_number = models.CharField(default=999, max_length=4)
    email = models.EmailField(max_length=255, default=None, blank=True, null=True)
    address = models.CharField(max_length=255, default=None, blank=True, null=True)
    phone_number = models.CharField(max_length=25, blank=True, null=True, default=None)
