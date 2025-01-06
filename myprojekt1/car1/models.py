from django.db import models

class CarMake(models.Model):
    CarMake_name = models.CharField(max_length=64)


    def __str__(self):
        return self.CarMake_name




class CarModel(models.Model):
    car_model_name = models.CharField(max_length=64)
    CarMake_name = models.ForeignKey(CarMake, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.car_model_name}, {self.CarMake_name}'



class Car(models.Model):
    car_name = models.CharField(max_length=64)
    CarMake_name = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    car_model_name = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    year = models.PositiveSmallIntegerField()
    color = models.CharField(max_length=10)
    volum = models.DecimalField(max_digits=10, decimal_places=1)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='imagase/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.car_name