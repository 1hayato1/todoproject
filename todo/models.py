from django.db import models


# Create your models here.
CATEGORY = (('business', 'ビジネス'), ('life', '生活'), ('other', 'その他'))

class todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.CharField(
        max_length=100,
        choices = CATEGORY
        )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title