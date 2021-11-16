from django.db import models

# Create your models here.

class Activity(models.Model):
    name = models.CharField(max_length=25)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Activities"

class Applicant(models.Model):
    name = models.CharField(max_length=25)
    birth_date = models.DateField()
    reg_date = models.DateField()
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
