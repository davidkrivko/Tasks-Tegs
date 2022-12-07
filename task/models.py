from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    date_of_creation = models.DateTimeField(auto_now=True)
    deadline = models.DateField(null=True, blank=True)
    done = models.BooleanField()
    tag = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return self.content
