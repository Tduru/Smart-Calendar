from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    universityID = models.CharField(max_length=10, blank=False, default= "xxxx")
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    department = models.CharField(max_length=60)
    email = models.EmailField()
    eventID = models.ManyToManyField('Event')
    roomID = models.ManyToManyField('Room')

class Room(models.Model):
    building = models.CharField(max_length=30, blank=False)
    site = models.CharField(max_length=30, blank=False)


class Event(models.Model):
    roomID = models.ForeignKey(Room, on_delete=models.CASCADE)
    eventTitle = models.CharField(max_length=30, blank=False)
    catergory = models.CharField(max_length=30, blank=False)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    description = models.TextField(blank=False)
    priorityLevel = models.CharField(max_length=10, blank=False)


class Course(models.Model):
    courseTitle = models.CharField(max_length=30, blank=False)
    module = models.ManyToManyField('Module')


class StudentAccount(Account):
    studyLevel = models.CharField(max_length=1, blank=False)
    coursePrograme = models.ForeignKey(Course, on_delete=models.CASCADE)

class Module(models.Model):
    moduleCode = models.CharField(max_length=9, blank=True)
    moduleTitle = models.CharField(max_length=30, blank=False)


class FriendsList(models.Model):
    first_friend = models.ManyToManyField('Account')


class ExtraCurricularEvent(Event):
    coordinator = models.CharField(max_length=30, blank=False)
    streetName = models.CharField(max_length=30, blank=False)
    postcode = models.CharField(max_length=30, blank=False)
    capacity = models.CharField(max_length=4, blank=False)
    contactEmail = models.EmailField()
    bookingRequired = models.BooleanField()
    restriction = models.CharField(max_length=4, blank=False)


class AcademicEvent(Event):
    eventType = models.CharField(max_length=30, blank=False)

