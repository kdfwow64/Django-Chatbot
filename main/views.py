from django.http import JsonResponse, HttpResponse
from rest_framework.request import *
from django.views.decorators.csrf import csrf_exempt
#from .controllers.conversation_logic import get_intent, get_reply
from features.message_parsing import *
import json
from time import time
import datetime
import traceback

from features.metrics_creator import *
from features.constants import *
from features.models import UserSourceMetric

@csrf_exempt
def chatterbox(request):
    # Template response according to contract
    response = {'reply': {'type':'text',
                          'content':'Something went wrong!'},
                 'prompt': {'type': 'text',
                          'content': "Type already!"},
                 'user_info': {'first_name': '',
                              'last_name': '',
                              'email': ''},
               }
    try:
        if request.method == "POST":
            data = json.loads(request.body.decode())

            print("=== This is the data receieved ===")
            print(data)
            print("=== End of data received ===")
            uncooked_message = data['message'] if data['message'] else ""
            user_info = data['user_info'] #first_name, last_name, email, token
            create_user_source_metric(user_info, request)
            response.update({'user_info': user_info}) # initial update in case error
            create_user_message_metric(user_info)
            #Go through list of intents/keywords and match it to the correct INTENT
            intent = get_intent(user_info, uncooked_message) #TODO: add user_info
            # uncooked_message
            print("=== This is the intent ===")
            print(intent)
            print("==")
            
            # import pdb
            # pdb.set_trace()
            chat_log = ChatLogs.objects.create(
                user_id = user_info['user_id'],
                user_input = data['message'],
                session_id = user_info['session_id']

                )

            print("=== Intent over and out ===")
            #get the right reply and assign to cooked_message
            cooked_message = get_botui_reply(user_info, uncooked_message, time(), intent)

            chat_log = ChatLogs.objects.create(
                user_id = user_info['user_id'],
                bot_reply = cooked_message['reply']['content'],
                session_id = user_info['session_id']
                )

            print("=== Reply start ===")
            print(cooked_message)
            print("=== Reply end ===")



            if intent == INTENT_IS_SET_CITY:
                create_user_city_metric(user_info)
            response.update(cooked_message)
            response.update({'user_info': user_info})
    except Exception as e :
        print("\n=== There was an error ===")
        traceback.print_tb(e.__traceback__)
        print(e)
        print("=== End of error ===\n")
    response = JsonResponse(response)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST'
    response['Access-Control-Allow-Headers'] = 'Accept, Accept-Language, Content-Language, Last-Event-ID, Content-Type'
    return response

def dbapi(request):
    # Template response according to contract
    response = {'numbers': 123, 'alphabets': 'ijk',}
    response = JsonResponse(response)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST'
    response['Access-Control-Allow-Headers'] = 'Accept, Accept-Language, Content-Language, Last-Event-ID, Content-Type'
    return response


def get_user_message_statistics(request):
    start_date = request.GET.get('startDate', datetime.date.today().replace(datetime.date.today().year - 1).strftime("%Y-%B-%d"))
    end_date = request.GET.get('endDate', datetime.date.today().strftime("%Y-%B-%d"))
    print(start_date)
    print(end_date)
    response = JsonResponse({
    "2019-03-01": 10,
    "2019-03-02": 11,
    "2019-03-03": 11,
    "2019-03-04": 11,
    "2019-03-05": 11,
    "2019-03-06": 11,
    "2019-03-07": 11,
    "2019-03-08": 11,
    "2019-03-09": 11,
    "2019-03-10": 11,
    "2019-03-11": 11,
    "2019-03-12": 11})
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'GET'
    response['Access-Control-Allow-Headers'] = 'Accept, Accept-Language, Content-Language, Last-Event-ID, Content-Type'
    return response

def rand(request):
    # Template response according to contract
    response = {"random number":randint(1,10**6)}
    response = JsonResponse(response)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST'
    response['Access-Control-Allow-Headers'] = 'Accept, Accept-Language, Content-Language, Last-Event-ID, Content-Type'
    return response

def get_cities_searched_absent_statistics(request):
    # Template response according to contract
    response = {"Yoo hooo!":"I'm get_cities_searched_absent_statistics™ The Epic!"}
    response = JsonResponse(response)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST'
    response['Access-Control-Allow-Headers'] = 'Accept, Accept-Language, Content-Language, Last-Event-ID, Content-Type'
    return response

def get_countries_statistics(request):
    # Template response according to contract
    response = {"Yello!":"I'm get_countries_statistics ™ The Awesome"}
    response = JsonResponse(response)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST'
    response['Access-Control-Allow-Headers'] = 'Accept, Accept-Language, Content-Language, Last-Event-ID, Content-Type'
    return response

def get_cities_searched_present_statistics(request):
    # Template response according to contract
    response = {"Hi!":"I'm get_cities_searched_present_statistics ™ The Cool"}
    response = JsonResponse(response)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST'
    response['Access-Control-Allow-Headers'] = 'Accept, Accept-Language, Content-Language, Last-Event-ID, Content-Type'
    return response

def get_user_statistics(request):
    start_date = request.GET.get('startDate', None)
    end_date = request.GET.get('endDate', None)
    #TODO: LOGIC TO FILL UP DATES
    if start_date == end_date == None:
        start_date = end_date = (datetime.datetime.now() - datetime.timedelta(1)).strftime('%Y-%m-%d')
    elif start_date == None:
        start_date = end_date
    elif end_date == None:
        end_date = start_date

    print(f'start is: {start_date}')
    print(f'  end is: {end_date}')
    query_set = UserSourceMetric.objects.filter(timestamp__gte = start_date, timestamp__lte = end_date)
    print(query_set)

    response = {"Yo!":"I'm the user guy! ™ The Astounding"}
    response = JsonResponse(response)
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Methods'] = 'POST'
    response['Access-Control-Allow-Headers'] = 'Accept, Accept-Language, Content-Language, Last-Event-ID, Content-Type'
    return response
