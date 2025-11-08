from django.db import models


class Students(models.Model):
    student_name = models.CharField(max_length=100)

    age = models.IntegerField()

    email = models.EmailField()

    cours = models.CharField(max_length=50, default="python")

    data_created_at = models.DateTimeField(auto_now_add=True)

    active_now = models.BooleanField(default=True)

    def __str__(self):
        return self.student_name
