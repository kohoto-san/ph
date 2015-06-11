from django.db import models


class Product(models.Model):

    votes_count = models.IntegerField()
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=255)

    discussion_url = models.CharField(max_length=255)
    redirect_url = models.CharField(max_length=255)

    created_at = models.CharField(max_length=50)

    # День с момента основания сайта (1-ый день = 0)
    day = models.IntegerField()

    comments_count = models.IntegerField()

    def __str__(self):
        return self.name
