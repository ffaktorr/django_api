from django.db import models


class Departments(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name


class Employees(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Departments)

    class Meta:
        verbose_name_plural = "Employees"

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.department})'
