from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    age = models.IntegerField()
    email =models.EmailField()
    department=models.DateField()
    def __str__(self):
        return self.name

    #create a staff model firstname,lastname,position,phone,email,hiredate
    #REturn firstname and lastname

class Staff(models.Model):
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    position = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    hiredate = models.DateField()

    def __str__(self):
        return self.firstname
        return self.lastname




#creat a ward model name,totalbeds,availablebeds,
  #return the name

class Ward(models.Model):
    name = models.CharField(max_length=100)
    totalbeds = models.IntegerField()
    availablebeds = models.IntegerField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date =models.DateTimeField()
    department = models.CharField(max_length=35)
    doctor = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name


class Contact1(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name
#mpesa api
class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"

