from django.db import models


class Contact(models.Model):
    contact_name = models.CharField(max_length=32)
    contact_email = models.EmailField()
    contact_content = models.TextField(max_length=500)

    def __str__(self):
        return self.contact_email
