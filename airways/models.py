from django.db import models


# Create your models here.


class Country(models.Model):
    country_code = models.CharField(max_length=10)
    continent = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Plane(models.Model):
    name = models.CharField(max_length=50)
    production_date = models.DateField('Date of production')
    passenger_capacity = models.IntegerField('Number of seats')

    def __str__(self):
        return self.name + " " + str(self.id)


class Airport(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pilot(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.TextField(max_length=200)

    def __str__(self):
        return self.firstname + " " + self.surname


class Flight(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.DO_NOTHING)
    plane = models.ForeignKey(Plane, on_delete=models.DO_NOTHING)

    # related names are used for getting the Flight-Airport relationship backwards
    # they might not be used in the project but since there are two different fields
    # they had to be set or disabled
    departure_airport = models.ForeignKey(Airport, on_delete=models.DO_NOTHING, related_name='departure')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.DO_NOTHING, related_name='arrival')
    departure_time = models.DateTimeField('Departure time')
    base_price = models.FloatField('Base ticket price')

    def __str__(self):
        return str(self.departure_time) + " " + str(self.departure_airport) + " - " + str(self.arrival_airport)


class Customer(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    firstname = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.TextField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + " " + self.surname


class Ticket(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    flight = models.ForeignKey(Flight, on_delete=models.DO_NOTHING)
    price = models.FloatField('Ticket price')

    def __str__(self):
        return str(self.flight) + " " + str(self.price)
