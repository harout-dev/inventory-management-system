from django.db import models


class Laptop(models.Model):

    laptop_manufacturer_choices = (
        ('lenovo', 'LENOVO'), ('acer', 'ACER'), ('macbook','MACBOOK'),('dell', 'DELL')
       , ('hp', 'HP'), ('asus', 'ASUS') )
    processor_choices = ( ('core i3', 'CORE I3'), ('core i5', 'CORE I5'),('core i7', 'CORE I7')  )
    manufacturer = models.CharField(max_length=100,blank= False, choices = laptop_manufacturer_choices)
    serial_number = models.CharField(max_length=100,blank= False)
    ram = models.IntegerField()
    processor = models.CharField(max_length=100,choices = processor_choices)
    purchased_date = models.DateField()
    employee_name = models.CharField(max_length=100,)
    handover_date = models.DateField(max_length=100,)

class Mobile(models.Model):

    mobile_manufacturer_choices = (
        ('lenovo', 'LENOVO'), ('samsung', 'SAMSUNG'),('huawei','HUAWEI'),('nokia', 'NOKIA')
    )
    manufacturer = models.CharField(max_length=100,blank= False, choices = mobile_manufacturer_choices)
    model_name = models.CharField(max_length=100,)
    serial_number = models.CharField(max_length=100,blank= False)
    purchased_date = models.DateField()
    employee_name = models.CharField(max_length=100,)
    handover_date = models.DateField()

class Tab(models.Model):

    tab_manufacturer_choices = (
        ('lenovo', 'LENOVO'), ('samsung', 'SAMSUNG'),('huawei','HUAWEI'),
    )
    manufacturer = models.CharField(max_length=100,blank= False, choices = tab_manufacturer_choices)
    serial_number = models.CharField(max_length=100,blank= False)
    purchased_date = models.DateField()
    employee_name = models.CharField(max_length=100,)
    handover_date = models.DateField()

class Sim(models.Model):

    operator_choices = ( ('alfa', 'ALFA'), ('mtc', 'MTC') )
    type_choices = ( ('data', 'DATA'), ('primary', 'PRIMARY'), ('vpn', 'VPS'))
    operator = models.CharField(max_length=100,blank= False, choices = operator_choices)
    sim_number = models.IntegerField(blank= False)
    line_number = models.IntegerField(blank = False)
    sim_type = models.CharField(max_length=100,blank = False, choices = type_choices)
    sim_status = models.CharField(max_length=100,blank = False)





