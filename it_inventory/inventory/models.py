from django.db import models


class Device(models.Model):

    device_choices = (
        ('laptop', 'LAPTOP'), ('mobile', 'MOBILE'), ('tab', 'TAB')
    )

    manufacturer_choices = (
        ('lenovo', 'LENOVO'), ('samsung', 'SAMSUNG'), ('acer', 'ACER'), ('macbook','MACBOOK'),
        ('huawei','HUAWEI'), ('hp', 'HP'), ('asus', 'ASUS'),('nokia', 'NOKIA')
    )
    device = models.CharField(max_length=10, choices = device_choices)
    manufacturer = models.CharField(max_length=100 , blank= False, choices = manufacturer_choices)
    serial_number = models.CharField(max_length=100, blank= False)
    purchased_date = models.DateField()
    employee_name = models.CharField(max_length=100)
    employee_mobile = models.IntegerField()
    handover_date = models.DateField()



