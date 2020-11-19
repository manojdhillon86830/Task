from django.db import models
# Create your models here.
class Car(models.Model):
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Email=models.EmailField()
    Password=models.CharField(max_length=100)

    def register(self):
        return self.save()

    @staticmethod
    def get_customer_by_email(Email):
        try:
            return Car.objects.get(Email=Email)
        except:
            return False
        

