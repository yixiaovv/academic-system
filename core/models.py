from django.db import models

class Teacher(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    degree = models.CharField(max_length=100, blank=True, verbose_name="Учёная степень")
    login = models.CharField(max_length=50, unique=True, verbose_name="Логин")
    password_hash = models.CharField(max_length=255, verbose_name="Пароль (хэш)")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название группы")
    course = models.IntegerField(verbose_name="Курс")
    year = models.IntegerField(verbose_name="Год набора")
    curator = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="Куратор"
    )

    def __str__(self):
        return self.name

class Student(models.Model):
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    login = models.CharField(max_length=50, unique=True, verbose_name="Логин")
    password_hash = models.CharField(max_length=255, verbose_name="Пароль (хэш)")
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="Учебная группа"
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"