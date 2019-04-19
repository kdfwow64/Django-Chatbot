import json, requests, re

dictonaryOfWeather ={
"thunderstorm with light rain": "Don't bother with the unbrella, just stay indoors for a thunderstorm",
"thunderstorm with rain": "Don't bother with the unbrella, just stay indoors for a thunderstorm",
"thunderstorm with heavy rain": "Don't bother with the unbrella, just stay indoors for a thunderstorm",
"light thunderstorm": "Don't bother with the unbrella, just stay indoors for a thunderstorm",
"thunderstorm": "Don't bother with the unbrella, just stay indoors for a thunderstorm",
"heavy thunderstorm": "heavy thuderstorm...maybe start inching towards the bomb shelter",
"ragged thunderstorm": "ragged thunderstorm- not the best weather for a holiday",
"thunderstorm with light drizzle": "No problem, but stay indoors",
"thunderstorm with drizzle": "No problem, but stay indoors",
"thunderstorm with heavy drizzle": "No problem, but stay indoors",
"light intensity drizzle": "Remember to bring your unbrella☔️",
"drizzle": "Remember to bring your unbrella☔️",
"heavy intensity drizzle": "Remember to bring your unbrella☔️",
"light intensity drizzle rain": "Remember to bring your unbrella☔️",
"drizzle rain": "Remember to bring your unbrella☔️",
"heavy intensity drizzle rain": "Remember to bring your unbrella☔️",
"shower rain and drizzle": "Remember to bring your unbrella☔️",
"heavy shower rain and drizzle": "Remember to bring your unbrella☔️",
"shower drizzle": "Remember to bring your unbrella☔️",
"light rain": "Remember to bring your unbrella☔️",
"moderate rain": "Remember to bring your unbrella☔️",
"heavy intensity rain": "Remember to bring your unbrella☔️",
"very heavy rain": "Remember to bring your unbrella☔️",
"extreme rain": "A ton of rain",
"freezing rain": "berrr-freezing rain",
"light intensity shower rain": "Just plain old rain",
"shower rain": "Just plain old rain",
"heavy intensity shower rain": "Just plain old rain",
"ragged shower rain": "Just plain old rain-but ragged",
"light snow": "Snow!! ⛄️",
"snow": "Snow everywhere!⛄️",
"heavy snow": "A lot of heavy snow🌨",
"sleet": "Rain with snow-stick to the house.",
"shower sleet": "Rain with snow-stick to the house.",
"light rain and snow": "Rain with snow-stick to the house.",
"rain and snow": "Rain with snow-stick to the house.",
"light shower snow": "Rain with snow-stick to the house.",
"shower snow": "Rain with snow-stick to the house.",
"heavy shower snow": "Rain with snow-stick to the house.",
"mist": "Mist - humid!",
"smoke": "Smoky - where are the masks?",
"haze": "Silly haze! - where are the masks?",
"sand, dust whirls": " TAKE COVER- DUST WHIRLS!",
"fog": "Don't go out unless you have x-ray vision and can see through fog!",
"sand": "Close your eyes, or wear your goggles! Don't want sand getting into your eyes, theres sand, sand, everywhere!",
"dust": "Get the cough medicine -  a ton of dust.",
"volcanic ash": "I wouldn't remain in the city if I were you! VOLCANO ASH!!",
"squalls": "Sqalls-A sudden violent gust of wind or localized storm, especially one bringing rain, snow, or sleet... that does it... RUN!",
"tornado": "Wondering why it's dark outside? Cause of a tornado! Bye and now RUN! 🏃🏾😱",
"clear sky": "A nice clear sky ☀️",
"few clouds": "Only a few clouds, good time to pack your bags and go out! ⛅️",
"scattered clouds": "Only a few scattered clouds, good time to pack your bags and go out! ☀️",
"broken clouds": "Only a few broken clouds, good time to pack your bags and go out! 🎒",
"overcast clouds": "Looks like it's gonna rain! Stick to the shelter!",
"tropical storm": "No problem, but stay indoors",
"hurricane": "Wondering why it's dark outside? Cause of a hurricane! Bye and now RUN! 🏃🏾💨",
"cold": "brrr-turn off the a/c!",
"hot": "Hot -turn on the a/c!",
"windy": "Windy - nice if you live on the eqator.",
"hail": "No need to ask for ice in your drinks today! Just stick your cup out of the windows! Or just stay indoors for hail is comming!"
}

def load_weather_database(filename):
    import csv, os
    filepath = os.path.join(os.path.dirname(os.path.dirname(__file__)),"features/"+filename)
    with open(filepath, encoding="ISO-8859-1") as f:
        myreader = csv.reader(f)
        data = []
        for row in myreader:
            data.append(row)
    # drop header
    data = data[1:]
    WEATHER_DATABASE = {}
    # sort by population
    data.sort(key = lambda row: float(row[4]))
    for _, name, lat, long, _, _, _, _, _ in data:
        WEATHER_DATABASE[name.lower()] = [ lat, long ]
    return WEATHER_DATABASE

def get_weather(user_info):
    try:
        city = user_info["city"]
        latitude, longitude = WEATHER_DATABASE[city.lower()]
        url = 'http://api.openweathermap.org/data/2.5/weather?' \
            'lat={}&lon={}&appid={}&units={}&lang={}'.format(latitude, longitude, WEATHER_API_KEY, 'metric', 'en')
        r = requests.get(url)
        data = r.json()
        weather_descript = data["weather"][0]["description"]
        temperature = round(float(data["main"]["temp"]))
        reply = "The weather for {} is {}!!! The temperature is {}°C! {}".format(city.title(), weather_descript, temperature, dictonaryOfWeather[weather_descript])
        return reply
    except KeyError:
        return "You don't have a city set!"

WEATHER_API_KEY = "0c4f222801bb854a7932489dabb4daeb"
WEATHER_DATABASE = load_weather_database("city_.csv")
