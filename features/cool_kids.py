from .models import CoolKid, City, CoolKidQuestion
from random import choice
from .constants import EMOJIS

def get_cool_kids_by_city(city_name):
    city = City.objects.filter(name = city_name).order_by('-population')[0]
    coolKids = list(CoolKid.objects.filter(city = city.id).values_list('name', flat = True).distinct())
    return coolKids

def get_cool_kid_questions(user_info, received_message):
    return CoolKidQuestion.objects.filter(coolKid_id=user_info["id"]).filter(question__iexact=received_message)

def get_introduction(user_info):
    name = user_info["first_name"]
    return "Hi {}, my name is Sasha. I live in Islamabad (Pakistan). I’m a 10 year old girl who loves making things, horse riding, reading and 3d printing.".format(name)


L1 = ["Sorry, I'm currently interviewing cool kids from **{}**, ",
"Sadly, I'm still in the process of interviewing cool kids from **{}**, ",
"Oops, I'm still working on interviewing cool kids from **{}**, "]

L2 = ["but come back and check soon because I will try and have some epic kids for you!",
"so come back soon to check!",
"but we will have some soon!",
"butttt.... never fear, recruters are here! ... Soon!"
]

def get_no_cool_kid_reply(user_info):
    return choice(L1).format(user_info['city'])+choice(L2)+choice(EMOJIS)
