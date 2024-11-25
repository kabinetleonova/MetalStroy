from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название услуги')
    image = models.ImageField(null=True, blank=True, upload_to="menu/")
    content = models.TextField('Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    class Meta:
        db_table = 'menu'
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title

class record(models.Model):
    name = models.CharField(max_length=150, verbose_name='ФИО')
    number = models.CharField(max_length=150, verbose_name='Номер телефона')
    message = models.TextField(verbose_name="Описание работы")
    
    class Meta:
#        managed = False
        db_table = 'record'
        verbose_name = 'запись'
        verbose_name_plural = 'Записи'
        
    def __str__(self):
        return self.name

class completedrecord(models.Model):
    record = models.ForeignKey(record, on_delete=models.CASCADE, null=True, blank=True,verbose_name = 'Выберите клиента')
    completed_work = models.TextField('Назначенное время и доп. условия', default="")

    class Meta:
#        managed = False
        db_table = 'completedrecord'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи Выполненые'
        
    def __str__(self):
        return self.completed_work