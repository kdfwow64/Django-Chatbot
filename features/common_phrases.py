from random import *
from .constants import EMOJIS

language_based_greetings = {
    "en_US": ["hi", "hihi", "hello", "hey", "how are you", "hello bello"],
    "es_LA": ["hola", "hola", "gepasa"],
    "de_DE": ["hallo", "guten tag"],
    "fr": ["bonjour"],
    "hi": ["namaste"],
    "ar": ["salaam alaikum"] ,
    "ru": ["zdras-tvuy-te", "zdras tvuy te"],
    "zh_CN": ["你好"],
}

list_of_common_greetings = ['hi', 'hello', 'hey', 'hola', 'bonjour', 'hallo', 'guten tag', 'ciao', 'olà', 'namaste', 'salaam', 'zdras-tvuy-te']

list_of_all_greetings = []
for l in language_based_greetings.values():
    list_of_all_greetings.extend(l)

COMPLETE_GREETINGS = ["{0} {1}, how are you today?",
                      "{0} {1}, what do you want to know?",
                      "{1}, {0}! Hello! Really great to see you!",
                      "{1} {0}! Or hello? Oh, hello!",
                      "{0} {1}, how are you?",
                      "{0} {1}, how can I help you?",
                      "{0} {1}, {0} {1}, {0} {0}!",
                      "{0}, {1}! Hello hello hello! I was created in 2017 in Singapore by Zara."]

def get_greeting(user_info):
  """
  takes in user_info
  returns a localized greeting
  """
  name = user_info["first_name"]
  if "locale" not in user_info:
      user_info["locale"] = None
  locale = user_info["locale"]
  if locale in language_based_greetings:
    hello = choice(language_based_greetings[locale] + list_of_common_greetings).capitalize()
  else:
    hello =  choice(list_of_common_greetings).capitalize()
  return choice(COMPLETE_GREETINGS).format(hello, name)


from random import choice
list_of_all_byes = ["bye", "see ya", "seeya", "goodbye", "byebye", "toodles", "ciao", "I gotta go"]

byes = ["Bye {} {}!",
"See ya {} {}",
"Goodbye {} {}",
"Toodles {} {}",
"Bye, but it was great to see you again {}... {}",
"It was nice to see you again {} {}",
"Take care {} {}",
"Bye, take it easy... {} {}",
"Have a Good One {} {}",
"Have a nice day {} {}",
"Until next time {} {}",
"I’m out of here {} {}",
"I’ll catch you later {} {}",
"Catch You On The Flip Side {} {}",
"I gotta go too, {} {}!",
"I gotta get going as well {} {}",
"Then I Gotta Jet off {}{}!",
"I Gotta Take Off as well by rocket jets {}{}!",
"I Gotta Roll too {} {}",
"I Gotta Run, also, if ya don't mind {}{}",
"Alright let's split {} {}",
"Gotta Make Tracks too {} {}",
"I Gotta Hit The Road too {} {}",
"I Gotta Head Out too {} {}",
"I Gotta Bounce too {} {}",
"Sniff. Sooooo sad. Well then, bye {}!👋{}",
"Bye! See ya👋🏾 {}{}!",
"See you soon {}{}!",
"Look forward to chatting with you again {}{}!",
"I really enjoyed talking with you, see ya {}{}!",
"Byebye"]

def get_bye(user_info):
    """
    takes in user_info
    returns a farewell
    """
    bye = choice(byes)
    emoji = choice(["🙋🏾","🖐🏾","🔱","😎", "👸🏾","💎"])
    try:
        bye = bye.format(user_info["first_name"], emoji)
    except:
        pass
    return bye

confused_responses = [
"Ummm.....{0}⁉️ I think what you said is a little 🎇 out of my brain - or battery! 🔋 - box! 📦 Perhaps you might have meant something from this fantastic 👌🏾 deluxe travel menu 📜 which will appear like magic 🔮 if you type the magic word **menu**?",
"_{1}_ ⁉️ What do you mean by **{1}** If you click on my graciosly provided button ✌, you shall find what you seek! 💎",
"Uhh... Sorry {0}, I dunno what's _{1}_... just click on the button below and behold my menu so you can click on what you want!",
]

def get_confused_reply(user_info, received_message):
    return choice(confused_responses).format(user_info["first_name"], received_message)

menu_responses = [
"Alright! You asked for menu! So you get menu!",
"Yes...menu, menu, where is that menu - Aha!! All the real food items you need!",
"Hmm.. where is the menu... Ah! I found the menu! Here it is, real quick, like fast FOOD!",
"OK! Here is the menu for other stuff to do!",
'Remember! You can always write "menu" for options 📓',
]

marks = ["!","!!"," Ooh la la!"," #cool!"]

def get_menu_reply(user_info):
    return choice(menu_responses) + choice(EMOJIS)


# starter1 = [
# "So!!",
# "Well...",
# "Oh?",
# ]
#
# starter2 = [
# "You want to talk, {}!",
# "You would like to talk, {}!",
# "{}, really, talk talk talk talktalk talk talk TALK!",
# ]
#
# starter3 = [
# "Mind you, I'm a bit like a smart baby, I can only understand if you type in one of the buttons, hi, or bye!",
# "Okay start talking! But I can only understand the buttons, hi, or bye!",
# "Fine, you can carry on talking about other things.",
# "Oh, whatever: just talk.",
# ]
#
# def get_conversation_starter(user_info):
#     name = user_info["first_name"]
#     full_sentence = ' '.join([choice(starter1), choice(starter2).format(name), choice(starter3)])
#     return full_sentence + choice(emojis) + choice(marks)
