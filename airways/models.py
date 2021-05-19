from django.db import models


# Create your models here.


class Country(models.Model):
    country_code = models.CharField(max_length=10)
    continent = models.CharField(max_length=50)
    name = models.CharField(max_length=50)


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)


class Plane(models.Model):
    name = models.CharField(max_length=50)
    production_date = models.DateField('Date of production')
    passenger_capacity = models.IntegerField('Number of seats')


class Airport(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)


class Pilot(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.TextField(max_length=200)


class Flight(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.DO_NOTHING)
    plane = models.ForeignKey(Plane, on_delete=models.DO_NOTHING)
    departure_airport = models.ForeignKey(Airport, on_delete=models.DO_NOTHING)
    arrival_airport = models.ForeignKey(Airport, on_delete=models.DO_NOTHING)
    departure_time = models.DateTimeField('Departure time')


class Customer(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.TextField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Ticket(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    flight = models.ForeignKey(Flight, on_delete=models.DO_NOTHING)
    price = models.FloatField('Ticket price')
