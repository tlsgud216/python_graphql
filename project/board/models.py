from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.TextField()
    content = models.TextField()
    category = models.ForeignKey(Category, related_name='notice', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
