from .constants import *
from .common_phrases import *
from .text_processing import *
from .city import set_city, get_change_city_reply
from .jokes import get_joke, get_answer, get_joke_reply
from .weather import *
from .contract import Contract
from .cool_kids import *
from .models import *
from random import choice, sample
from .metrics_creator import *
from datetime import date

explore_menu_list = ["Attractions", "Play Areas","Events",] # TODO: PUT THIS IN WHEN MUMMY SAYS TO!!!!!!! "Events"

attractions_img_list = [
  "https://static1.squarespace.com/static/5850baa5e4fcb5b420581f92/5bebb13e4ae2378e0c95cb6f/5ca1f0964785d3b98ad2e53e/1554116771429/Octa-Airplane-01.gif",
  "https://static1.squarespace.com/static/5850baa5e4fcb5b420581f92/5bebb13e4ae2378e0c95cb6f/5ca1f0961905f45415ff7faa/1554116774286/Octa-Airplane-02.gif",
  "https://static1.squarespace.com/static/5850baa5e4fcb5b420581f92/5bebb13e4ae2378e0c95cb6f/5ca1f09ff9619a0cc69c8285/1554116779144/Octa-Airplane-03.gif",
]

intent_dict = {}

intent_dict[INTENT_SAY_HELLO]         = list_of_all_greetings + ["justenteredpage"]
intent_dict[INTENT_SAY_BYE]           = list_of_all_byes
intent_dict[INTENT_GET_WEATHER]       = ["weather", "forecast", "sky", "rain", "raining", "sun", "sunny",("is","raining")]
intent_dict[INTENT_IS_SET_CITY]       = ["is setting city"]
intent_dict[INTENT_WANT_SET_CITY]     = [("change", "city"), ("choose", "city"), ("set", "city"), ("setting", "city"), ("change", "sataaaaaaaay")]
intent_dict[INTENT_GET_MENU]          = ["menu", "help", ("give", "options"), "what next", "what now", "totally lost", ("repeat last action", "no")]

intent_dict["explore city"]           = ["wander"]
intent_dict["attractions"]            = ["attractions"]
intent_dict["play areas"]             = ["play areas"]
intent_dict["event"]                  = ["events"]
intent_dict["description"]            = [("why", "epic"), ("why", "awesome"), ("description",)]
intent_dict["timings"]                = ["timings"]
intent_dict["tickets"]                = ["tickets"]
intent_dict["link"]                   = ["websites","website","link","links","linkies"]

intent_dict["answer joke"]            = ["answer joke"]
intent_dict["tell a joke"]            = ["joke", "jokes", ("make", "laugh"), "funny", "riddle"]

intent_dict["list cool kids"]         = [("meet", "cool", "kids"), ("back","cool","kids")]
intent_dict["get cool kids info"]     = ["get cool kids info"]
intent_dict["get cool kid answer"]    = ["get cool kid answer"]

intent_dict["repeat last action"]     = [("repeat last action", "yes"), ("next",), ("another","question")]


def get_intent(user_info, received_message):
    #logging = Logging.objects.get(user__email=user_info["email"])
    """takes in user_info and a received_message
       parses the intent and returns the intent as a string"""
    if "expected_intent" not in user_info:
        user_info["expected_intent"] = None
    expected_intent = "" if user_info["expected_intent"] == None else " " + user_info["expected_intent"]
    user_info["expected_intent"] = None
    parsed_intents = list(filter(lambda intent: contains_key(received_message + expected_intent, intent_dict[intent]),
                                 intent_dict))
    if len(parsed_intents) > 0:
        return parsed_intents[0]
    return "cannot understand intent"

def getDaysOfTheWeek():
    return "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()

def get_botui_reply(user_info, received_message, timestamp, intent):
    global cool
    print("getting reply for intent: ", intent)
    contract = Contract("")

    ##############
    # SMALL TALK #
    ##############
    if intent == "repeat last action":
        intent = user_info["last_action"]
        print("Replaced with: ", intent)
    if intent == INTENT_SAY_HELLO:
        contract.add(get_greeting(user_info))
        contract.add("Which city are you interested in? 😃✈️")
        user_info["expected_intent"] = "is setting city"

    elif intent == INTENT_SAY_BYE:
        contract.add(get_bye(user_info))

    elif intent == INTENT_GET_WEATHER:
        contract.add(get_weather(user_info))
        contract.add('Whatchya want to do next?')
        contract.add_buttons({"primary": DEFAULT_MENU, "secondary": []})

    elif intent == INTENT_GET_MENU:
        contract.add(get_menu_reply(user_info))
        contract.add("What do you want to do?")
        contract.add_buttons({"primary": DEFAULT_MENU, "secondary": []})

    elif intent == "cannot understand intent":
        contract.add(get_confused_reply(user_info, received_message))
        contract.add_buttons({"primary": ["MENU!"], "secondary": []})

    ###############
    # ASSIGN CITY #
    ###############
    elif intent == INTENT_WANT_SET_CITY:
        contract.add(get_change_city_reply(user_info))

    elif intent == INTENT_IS_SET_CITY:
        contract.add(set_city(user_info, received_message))
        user_info['last_viewed_playground_ids'] = []
        user_info['last_viewed_attraction_ids'] = []
        user_info['last_viewed_event_ids'] = []
        contract.add("What do you want to do?")
        contract.add_buttons({"primary": DEFAULT_MENU, "secondary": []})
        #logging.count_cities += 1

    ########
    # JOKE #
    ########
    elif intent == "tell a joke":
        contract.add(get_joke(user_info))

    elif intent == "answer joke":
        answer = get_answer(user_info)
        contract.add(get_joke_reply(received_message, answer))
        contract.add("Do you want to hear more?")
        user_info["expected_intent"] = "repeat last action"
        user_info["last_action"] = "tell a joke"
        contract.add_buttons({"primary": ["Yes", "No"], "secondary": []})

    #######################
    # EXPLORE THE CITY #
    #######################
    elif intent == "explore city":
        attractions = Attraction.objects.filter(city__iexact = user_info["city"]).order_by('?')
        playareas = Playground.objects.filter(city__iexact = user_info["city"]).order_by('?')
        events = Event.objects.filter(city__iexact = user_info["city"]).order_by('?')
        explore_menu_list = []
        current_emoji_list = sample(EMOJIS_PLACES, 3)
        if len(attractions) > 0:
            explore_menu_list.append("Attractions " + current_emoji_list[0])
        if len(playareas) > 0:
            explore_menu_list.append("Play Areas " + current_emoji_list[1])
        if len(events) > 0:
            explore_menu_list.append("Events " + current_emoji_list[2])
        if len(explore_menu_list) > 0:
            contract.add("What kind of place are you in the mood for?")
            contract.add_buttons({"primary": explore_menu_list, "secondary": []})
        else:
            contract.add("Sorry {}! I currently don't have any information on the city {} yet! 'orry again!'".format(user_info['first_name'], user_info['city']))
            contract.add_buttons({"primary": ["MENU!"], "secondary": []})
        contract.add_image(choice(attractions_img_list))
    ##############
    # ATTRACTION #
    ##############
    elif intent == "attractions":
        attractions = Attraction.objects.filter(city__iexact = user_info["city"]).order_by('?')
        if len(attractions) == 0:
            contract.add("Sorry! There are no attractions here.")
            contract.add("How about you try to:")
            contract.add_buttons({"primary": ["Change the city", "MENU!"], "secondary": []})
        else:
            attraction = None
            for a in attractions:
              if a.id not in user_info['last_viewed_attraction_ids']:
                  attraction = a
                  break
            if attraction is None:
              user_info['last_viewed_attraction_ids'] = []
              attraction = attractions[0]
            contract.add_image(attraction.image)
            contract.add(attraction.name)
            contract.add(attraction.address)
            contract.add_buttons({"primary": ["Why is this epic?", "Tickets", "Timings", "Website"], "secondary": ["NEXT! >>", "MENU!"]})
            user_info["last_action"] = "attractions"
            user_info["attraction_id"] = attraction.id
            user_info['last_viewed_attraction_ids'].append(attraction.id)

    elif intent == "description"and user_info['last_action'] == "attractions":
        create_user_attraction_metric(user_info)
        attraction = Attraction.objects.get(id=user_info["attraction_id"])
        contract.add(attraction.description)
        contract.add_buttons({"primary": ["Tickets", "Timings", "Website"], "secondary": ["NEXT! >>", "MENU!"]})

    elif intent == "link" and user_info['last_action'] == "attractions":
        attraction = Attraction.objects.get(id = user_info["attraction_id"])
        contract.add(f'{choice(LINK_PROMPTS)}[{attraction.link}]({attraction.link})')
        contract.add_buttons({"primary":["Why is this epic?", "Tickets", "Timings"], "secondary": ["NEXT! >>", "MENU!"]})

    elif intent == "timings" and user_info['last_action'] == "attractions":
        create_user_attraction_metric(user_info)
        days_of_week = getDaysOfTheWeek()
        attraction = Attraction.objects.get(id = user_info["attraction_id"])
        data = [attraction.monday, attraction.tuesday, attraction.wednesday, attraction.thursday, attraction.friday, attraction.saturday, attraction.sunday]
        if attraction.monday == attraction.tuesday == attraction.wednesday == attraction.thursday == attraction.friday == attraction.saturday == attraction.sunday:
            if attraction.monday == "":
                contract.add("Sorry! I have no timing info on this!!😛")
            else:
                contract.add("Same timings, every day!😛")
                contract.add(attraction.monday)
        else:
            contract.add("These are the Timings for the week:")
            for day, timing in zip(days_of_week, data):
                if timing == "":
                    timing = "Sorry! I have no info on this!!😛"
                contract.add("**{}**: {}".format(day, timing))
        contract.add_buttons({"primary":["Why is this epic?", "Tickets", "Website"], "secondary": ["NEXT! >>", "MENU!"]})
    elif intent == "tickets" and user_info['last_action'] == "attractions":
        create_user_attraction_metric(user_info)
        attraction = Attraction.objects.get(id=user_info["attraction_id"])
        if attraction.tickets == "":
            contract.add("There is currently no information about ticket pricing for **{}**, so you may assume that it's free!".format(attraction.name))
        else:
            contract.add(attraction.tickets)
        contract.add_buttons({"primary":["Why is this epic?", "Timings", "Website"], "secondary": ["NEXT! >>", "MENU!"]})
    ##############
    # PLAY AREAS #
    ##############
    elif intent == "play areas":
        playareas = Playground.objects.filter(city__iexact = user_info["city"]).order_by('?')
        if len(playareas) == 0:
            contract.add("Sorry! There are no play areas here.")
            contract.add("How about you try to:")
            contract.add_buttons({"primary":["Change the city", "MENU!"], "secondary": []})
        else:
            playarea = None
            for p in playareas:
                if p.id not in user_info['last_viewed_playground_ids']:
                    playarea = p
                    break
            if playarea is None:
                user_info['last_viewed_playground_ids'] = []
                playarea = playareas[0]
            contract.add_image(playarea.image)
            contract.add(playarea.name)
            contract.add(playarea.address)
            contract.add_buttons({"primary": ["Why is this awesome?", "Tickets", "Timings", "Website"], "secondary": ["NEXT! >>", "MENU!"]})
            user_info["last_action"] = "play areas"
            user_info["playground_id"] = playarea.id
            user_info['last_viewed_playground_ids'].append(playarea.id)

    elif intent == "link" and user_info['last_action'] == "play areas":
        playarea = Playground.objects.get(id = user_info["playground_id"])
        contract.add(f'{choice(LINK_PROMPTS)}[{playarea.link}]({playarea.link})')
        contract.add_buttons({"primary": ["Why is this awesome?", "Tickets", "Timings"], "secondary": ["NEXT! >>", "MENU!"]})

    elif intent == "tickets" and user_info['last_action'] == "play areas":
        create_user_playground_metric(user_info)
        playarea = Playground.objects.get(id = user_info["playground_id"])
        if playarea.tickets == "":
            contract.add("There is currently no information about ticket pricing for **{}**, so you may assume that it's free!".format(playarea.name))
        else:
            contract.add(playarea.tickets)
        contract.add_buttons({"primary": ["Why is this awesome?", "Timings", "Website"], "secondary": ["NEXT >>", "MENU!"]})
    elif intent == "timings" and user_info['last_action'] == "play areas":
        create_user_playground_metric(user_info)
        days_of_week = getDaysOfTheWeek()
        playarea = Playground.objects.get(id = user_info["playground_id"])
        data = [playarea.monday, playarea.tuesday, playarea.wednesday, playarea.thursday, playarea.friday, playarea.saturday, playarea.sunday]
        if playarea.monday == playarea.tuesday == playarea.wednesday == playarea.thursday == playarea.friday == playarea.saturday == playarea.sunday:
            if playarea.monday == "":
                contract.add("Sorry! I have no timing info on this!!😛")
            else:
                contract.add("Same timings, every day!😛")
                contract.add(playarea.monday)
        else:
            contract.add("These are the Timings for the week:")
            for day, timing in zip(days_of_week, data):
                if timing == "":
                    timing = "Sorry! I have no info on this!!😛"
                contract.add("**{}**: {}".format(day, timing))
        contract.add_buttons({"primary":["Why is this awesome?", "Tickets", "Website"], "secondary":["NEXT >>", "MENU!"]})

    elif intent == "description" and user_info['last_action'] == "play areas":
        create_user_playground_metric(user_info)
        playarea = Playground.objects.get(id = user_info["playground_id"])
        contract.add("Here's why **{}** is awesome!".format(playarea.name))
        contract.add(playarea.description)
        contract.add_buttons({"primary":["Tickets", "Timings", "Website"], "secondary": ["NEXT >>", "MENU!"]})

    ##########
    # EVENTS #
    ##########

    elif intent == "event":
        today = date.today()
        events = Event.objects.filter(city__iexact = user_info["city"],
                                      end_date__gte = today).order_by('?')
        if len(events) == 0:
            contract.add("Sorry! There are no events here.")
            contract.add("How about you try to:")
            contract.add_buttons({"primary": ["Change the city", "MENU!"], "secondary":[]})
        else:
            event = None
            for e in events:
                if e.id not in user_info['last_viewed_event_ids']:
                    event = e
                    break
            if event is None:
                user_info['last_viewed_event_ids'] = []
                event = events[0]
            contract.add_image(event.image)
            contract.add("**"+event.name+"**")
            contract.add(event.location)
            contract.add(event.short_description)
            contract.add_buttons({"primary": ["Description!", "Tickets", "Timings", "Website"], "secondary":["NEXT >>", "MENU!"]})
            user_info["last_action"] = "event"
            user_info["event_id"] = event.id
            user_info['last_viewed_event_ids'].append(event.id)

    elif intent == "link" and user_info['last_action'] == "event":
        evento = Event.objects.get(id = user_info["event_id"])
        contract.add(f'{choice(LINK_PROMPTS)}[{evento.link}]({evento.link})')
        contract.add_buttons({"primary": ["Description!", "Tickets", "Timings"], "secondary": ["NEXT >>", "MENU!"]})

    elif intent == "tickets" and user_info['last_action'] == "event":
        create_user_event_metric(user_info)
        event = Event.objects.get(id = user_info["event_id"])
        if event.tickets == "":
            contract.add("There is currently no information about ticket pricing for **{}**, so think of it as free! But seriously, bring some money just in case.".format(event.name))
        else:
            contract.add(event.tickets)
        contract.add_buttons({"primary": ["Description!", "Timings", "Website"], "secondary": ["NEXT >>", "MENU!"]})

    elif intent == "timings" and user_info['last_action'] == "event":
        create_user_event_metric(user_info)
        event = Event.objects.get(id = user_info["event_id"])
        if event.timing == "":
            contract.add("Sorry! I have no timing info on this!!😛")
        else:
            contract.add("These are the opening timings! "+choice(EMOJIS))
            contract.add(event.timing)
            contract.add("\nAnd the event is held from {} to {}!".format(event.start_date, event.end_date))
        contract.add_buttons({"primary": ["Description!", "Tickets", "Website"], "secondary": ["NEXT >>", "MENU!"]})

    elif intent == "description" and user_info['last_action'] == "event":
        create_user_event_metric(user_info)
        event = Event.objects.get(id = user_info["event_id"])
        contract.add("Here's why **{}** is awesome!".format(event.name))
        contract.add(event.description)
        contract.add_buttons({"primary": ["Tickets", "Timings", "Website"], "secondary": ["NEXT >>", "MENU!"]})

    #############
    # Cool KIDS #
    #############
    elif intent == "list cool kids":
        cool_kids = get_cool_kids_by_city(user_info['city'])
        if len(cool_kids) == 0:
            contract.add(get_no_cool_kid_reply(user_info))
            contract.add_buttons({"primary": ["MENU!"], "secondary": []})
        else:
            user_info["expected_intent"] = "get cool kids info"
            contract.add("These are the cool😎 kids!😜")
            contract.add_buttons({"primary": cool_kids, "secondary": []})

    elif intent == "get cool kids info":
        user_info['last_action'] = 'list cool kids'
        coolKids = CoolKid.objects.filter(name__iexact = received_message)
        if len(coolKids) == 0:
            coolKids = CoolKid.objects.filter(name__iexact = user_info["cool_kid_name"])
        coolKid = coolKids[0]
        coolKidQuestions = CoolKidQuestion.objects.filter(coolKid_id = coolKid.id)
        print(coolKidQuestions)
        questions = []
        for question in coolKidQuestions:
            questions.append(question.question)
        contract.add(coolKid.description)
        contract.add("------------------------------")
        contract.add("Why not ask a question?")
        contract.add_image(coolKid.image)
        user_info["expected_intent"] = "get cool kid answer"
        user_info["id"] = coolKid.id
        user_info["cool_kid_name"] = coolKid.name
        contract.add_buttons({"primary": questions, "secondary": ["MENU!"]})

    elif intent == "get cool kid answer":
        if (received_message == "menu"):
            contract.add('Whatchya want to do next?')
            contract.add_buttons({"primary": DEFAULT_MENU, "secondary": []})
        else:
            questions = get_cool_kid_questions(user_info, received_message)
            if len(questions) != 0:
                question = questions[0]
                user_info["last_action"] = "get cool kids info"
                user_info["id"] = user_info["expected_intent"] = None
                contract.add(question.answer)
                contract.add_image(question.image)
                contract.add_buttons({"primary":["MENU!","Back to COOL KIDS!! 😎", "Ask {} another question!!! 😄".format(question.coolKid.name)], "secondary": []})
            else:
                contract.add("Sorry! That is not a question that we have an answer to! Here are some questions that are valid!")
                user_info["expected_intent"] = "get cool kid answer"
                allQuestionRows = CoolKidQuestion.objects.filter(coolKid_id = user_info["id"])
                allQuestions = []
                for questionRow in allQuestionRows:
                    allQuestions.append(questionRow.question)
                contract.add_buttons({"primary": allQuestions, "secondary": ["MENU!"]})
    return contract
