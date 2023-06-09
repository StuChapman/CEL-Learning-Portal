from django.db import models

# Create your models here.


class Pages(models.Model):

    class Meta:
        verbose_name_plural = 'Pages'

    user = models.CharField(max_length=254, null=True)
    page = models.CharField(max_length=254, null=True)
    status = models.DecimalField(max_digits=2, decimal_places=0)

    def __str__(self):
        return self.page


class Tests(models.Model):

    class Meta:
        verbose_name_plural = 'Tests'

    user = models.CharField(max_length=254, null=True)
    test = models.CharField(max_length=254, null=True)
    status = models.DecimalField(max_digits=2, decimal_places=0)
    answer = models.CharField(max_length=254, null=True)
    result = models.DecimalField(max_digits=2, decimal_places=0, null=True)

    def __str__(self):
        return self.test


class Answers(models.Model):

    class Meta:
        verbose_name_plural = 'Answers'

    test = models.CharField(max_length=254, null=True)
    correctanswer = models.CharField(max_length=254, null=True)
    nexttest = models.CharField(max_length=254, null=True)

    def __str__(self):
        return self.test