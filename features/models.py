from django.db import models
from decimal import Decimal
import datetime
import uuid

# Create your models here.
class Joke(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    answer = models.TextField()
    def __str__(self):
        return self.question + ": " + self.answer

class Attraction(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.TextField(default="")
    image = models.TextField(default="")
    description = models.TextField(default="")
    monday = models.CharField(max_length=500, null=True)
    tuesday = models.CharField(max_length=500, null=True)
    wednesday = models.CharField(max_length=500, null=True)
    thursday = models.CharField(max_length=500, null=True)
    friday = models.CharField(max_length=500, null=True)
    saturday = models.CharField(max_length=500, null=True)
    sunday = models.CharField(max_length=500, null=True)
    tickets = models.TextField(default="")
    link = models.CharField(default="",max_length=2048)
    #  Max length of URLs is 2048: https://stackoverflow.com/a/33733386

class Playground(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.TextField(default="")
    image = models.TextField(default="")
    description = models.TextField(default="")
    monday = models.CharField(max_length=500, null=True)
    tuesday = models.CharField(max_length=500, null=True)
    wednesday = models.CharField(max_length=500, null=True)
    thursday = models.CharField(max_length=500, null=True)
    friday = models.CharField(max_length=500, null=True)
    saturday = models.CharField(max_length=500, null=True)
    sunday = models.CharField(max_length=500, null=True)
    tickets = models.TextField(default="")
    link = models.CharField(default="",max_length=2048)

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    name = models.CharField(default="",max_length=100)
    description = models.TextField(default="")
    short_description = models.CharField(default="",max_length=2048)
    link = models.CharField(default="",max_length=2048)
    image = models.TextField(default="")
    location = models.TextField(default="")
    tickets = models.TextField(default="")
    timing = models.CharField(default="",max_length=2048)

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=1024, unique=True)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)

class Session(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=7, default=Decimal(0.00))
    longitude = models.DecimalField(max_digits=10, decimal_places=7, default=Decimal(0.00))
    population = models.IntegerField(null=False, default=0)
    country = models.CharField(max_length=100, null=True)
    iso2 = models.CharField(max_length=2, null=True)
    iso3 = models.CharField(max_length=3, null=True)
    province = models.CharField(max_length=100, null=True)

class CoolKid(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(default="")
    image = models.CharField(default="",max_length=2048)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class CoolKidQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    coolKid = models.ForeignKey(CoolKid, on_delete=models.CASCADE)
    image = models.CharField(default="",max_length=2048)
    question = models.CharField(default="",max_length=2048)
    answer = models.CharField(default="",max_length=2048)

class UserCityMetric(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

class UserSourceMetric(models.Model):
    id = models.AutoField(primary_key=True) #optional
    timestamp = models.DateTimeField(auto_now_add=True, blank=True) #optional
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    ip_address = models.CharField(default="",max_length=128)
    user_agent = models.TextField(default="")
    country = models.CharField(db_index=True,default="",max_length=500)

class UserAttractionMetric(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

class UserMessageMetric(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

class UserPlaygroundMetric(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    playground = models.ForeignKey(Playground, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

class UserEventMetric(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)


class ChatLogs(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, null=True, blank=True)
    bot_reply = models.TextField(verbose_name='Bot Reply', null=True, blank=True)
    user_input = models.CharField(max_length=256, verbose_name='User Input', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return '{0}'.format(self.user_input)


class NoMatch(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    bot_message = models.TextField(verbose_name='Bot Reply', null=True, blank=True)
    
    anything_else = models.TextField(verbose_name='User Input', null=True, blank=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    def __str__(self):
        return '{0}'.format(self.bot_message)
