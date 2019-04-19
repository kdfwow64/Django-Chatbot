from random import choice
from .constants import *
from .models import Joke
from .text_processing import unigram, get_partial_match, remove_no_need, check_inside

def get_joke(user_info):
    """Takes in context dictionary
       updates the context
       returns a joke question string
       uses the database of jokes"""
    joke = choice(Joke.objects.all())
    user_info['last_intent'] = INTENT_GET_JOKE
    user_info['expected_intent'] = INTENT_ANSWER_JOKE
    user_info['info'] = joke.id
    return joke.question

def get_answer(user_info):
    joke_id = user_info['info']
    joke = Joke.objects.get(id = joke_id)
    user_info['last_intent'] = INTENT_ANSWER_JOKE
    user_info['expected_intent'] = INTENT_REPEAT_ACTION
    user_info['info'] = None
    return joke.answer

snickersnicker = ["🎉Good Job! It was: **{}**",
                  "Yep! Fantastic! How did you do it? I always have to rack my poor brain for this one! It was: **{}** 💻🙂",
                  "OMG! Future riddler in the making! Congratulations, **{}** is right! 😎😉"]

bommy = ["😜 Bom bom bom! Wrong! One day if you memorise the following... who knows? You could come be my star joker! Pleeeeese?!? They will tell tales of me - I mean you!☺︎😀 It was: **{}**",
            "Congratulations! A gold medal for... **flunking**  Which is good! You can practice more! Lessons for 1,000,000 dollars _only_! I'm gonna be rich! It was **{}** See how good I am! Come apply!🎉",
            "Nice try, but it was **{}**.. good luck with the toughest!😆",
            "Ooooooooooo-no. Sorry! It's actually **{}** Better luck next time!😎",
            "Too bad - try harder! But still,  I'm positive you'll get it next time if you memorise this as the answer: **{}** See! Star already! ⭐️"]
giveups = ["Oh, you give up? Well, this is quite a tricky one. :c Still, I can see if I can get you an easy one! :D It was... **{}**",
           "Don't give up so easily! The answer was: **{}** I know you can do it next time!👊🏾",
           "If you give up so easily, how can you be a riddler next time! Oh well, it was **{}** �"]
giveup_keyphrases = ["give up", "dunno", "what is it", "dont know", "donno", "idk"]

no_need = [
"this",
"a",
'an',
"because",
"is",
"am",
"the",
"it",
"its",
"im",
"of",
"and",
"the",
]

def get_joke_reply(user_answer, real_answer):
    real_answer_words = remove_no_need(real_answer, no_need) # get rid of all common words
    # matches at least 2 non trivial words UNLESS you only have 1 keyword
    threshold = min(2, len(real_answer_words))
    rm_list = unigram(user_answer)
    if len(get_partial_match(rm_list, real_answer_words)) >= threshold:
        return choice(snickersnicker).format(real_answer)
    elif check_inside(giveup_keyphrases, rm_list): # if they give up
        return choice(giveups).format(real_answer)
    else: # if they give the wrong answer
        return choice(bommy).format(real_answer)
