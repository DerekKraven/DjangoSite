from django.db import models

class Groups(models.Model):
    name = models.CharField(max_length=20, verbose_name='Наименование группы')
    number_of_students = models.IntegerField(verbose_name='Количество студентов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['name']


class Students(models.Model):
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    series = models.CharField(max_length=5, verbose_name='Серия паспорта')
    number = models.CharField(max_length=6,verbose_name="Номер паспорта")
    group_name = models.ForeignKey(Groups, on_delete=models.CASCADE, verbose_name="Группа")



    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name', 'date_of_birth']

