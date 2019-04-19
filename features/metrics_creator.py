from features.external.country_fetcher import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_user_agent(request):
    return request.META.get('HTTP_USER_AGENT')

def create_user_source_metric(user_info, request):
    if "user_id" not in user_info or "session_id" not in user_info: #beginning a chat with Octa
        ip_address = get_client_ip(request)
        print("getting user_id")
        user_id = get_user_id(user_info)
        session_id = get_session_id(user_info)
        print("got user_id", user_id)
        user_agent = get_user_agent(request)
        print("got user_agent", user_agent)
        country_name = get_country_name(ip_address)
        print("got country_name", country_name)
        metric = UserSourceMetric.objects.create(user_id=user_id,
                                                 session_id=session_id,
                                                 ip_address=ip_address,
                                                 user_agent=user_agent,
                                                 country=country_name
                                                )
        print("created metric", metric)

def create_user_city_metric(user_info):
    user_id = user_info['user_id']
    session_id = user_info['session_id']
    city_name = user_info['city']
    city_id = (City.objects.filter(name = city_name).distinct()[0]).id
    metric = UserCityMetric.objects.create(city_id=city_id, user_id=user_id, session_id=session_id)

def create_user_attraction_metric(user_info):
    user_id = user_info['user_id']
    session_id = user_info['session_id']
    attraction_id = user_info['attraction_id']
    metric = UserAttractionMetric.objects.create(attraction_id=attraction_id, user_id=user_id, session_id=session_id)

def create_user_playground_metric(user_info):
    user_id = user_info['user_id']
    session_id = user_info['session_id']
    playground_id = user_info['playground_id']
    metric = UserPlaygroundMetric.objects.create(playground_id=playground_id, user_id=user_id, session_id=session_id)

def create_user_message_metric(user_info):
    user_id = user_info['user_id']
    session_id = user_info['session_id']
    UserMessageMetric.objects.create(user_id=user_id, session_id=session_id)

def create_user_event_metric(user_info):
    user_id = user_info['user_id']
    session_id = user_info['session_id']
    event_id = user_info['event_id']
    metric = UserEventMetric.objects.create(event_id=event_id, user_id=user_id, session_id=session_id)

def get_user_id(user_info):
    if "user_id" not in user_info:
        try:
            user = User.objects.get(email=user_info['email'])
        except ObjectDoesNotExist:
            user = User.objects.create(email=user_info['email'], first_name=user_info["first_name"], last_name=user_info["last_name"])
        user_info["user_id"] = user.id
    return user_info["user_id"]

def get_session_id(user_info):
    if "session_id" not in user_info:
        session = Session.objects.create()
        user_info["session_id"] = session.id
    return user_info["session_id"]