from .text_processing import autocorrect
from random import choice

change_city_prompts = ["Cool. Which city would you like to explore next? 🗻 🗽",
                       "Soooooo..... which city did you have in mind then? ⛲️",
                       "Then which city do you want?? I mean, cities, cities, cities.. pick one!🌋"]

pompom = ["Great, **{}** is one of my favourite cities!😜 But then again, I like all cities.",
          "Oh, **{}** is a great place and I know it like the back of my hand! (Not to brag or anything! :D)",
          "**{0}** is great! Especially for whatever you wanted to do, even though I have no idea what you wanted to do. Anyway basically I'm saying that **{0}**'s great for everything!",
          "**{}** is a great choice! Let's start exploring **right NOW**!",
          "Congrats! Your city has offically been set to **{}**! 'have a nice day and I hope you had a pleasant flight on A3octa!' (That was my best imitation of the FX on a flight!)"]

def get_change_city_reply(user_info):
    user_info["expected_intent"] = "is setting city"
    return choice(change_city_prompts)

def get_city_reply(city):
    prompt = choice(pompom)
    return prompt.format(city)

def set_city(user_info, received_message):
    """
    takes in user_info and received_message
    identify the city in received_message,
    save the city in user_info
    returns a suitable reply
    """
    city = autocorrect(received_message, list_of_cities).title()
    print(city)
    print(city in list_of_cities)
    if city in list_of_cities:
        user_info["city"] = city
        reply = get_city_reply(city)
    else:
        user_info["city"] = choice(["Singapore", "Talinn", "New York", "Paris", "London", "Berlin"]) #TODO for sometime over the rainbow: choice(list_of_cities)
        reply = "Yeahhhhh... I'm not so sure **'{}'** is a city! ⬅️ I set you a cool city to explore instead, though! Welcome to **{}** 💁🌇".format(city, user_info["city"])
    return reply

def load_list_of_cities(filename):
    import csv, os
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)),"features/"+filename)
    with open(filepath, encoding="ISO-8859-1") as f:
        myreader = csv.reader(f)
        data = []
        for row in myreader:
            data.append(row)
    data = data[1:] # drop header
    return list(set(map(lambda row: row[1], data)))

list_of_cities = load_list_of_cities("city_.csv")
