import random
from datetime import datetime
def greet_and_introduce():
    #declare some list of responses
    responses=[
        "Hi there ! I am multi talented bot. can help you to have some fun and help to do some calculations and give you some knowledge too.May I know your name",
        "Hello! It's good to meet you.Hope we can have a good time together .can you tell me your name please"
    ]
    #pick a response at random and return that
    print(random.choice(responses))

def get_timeofday_greeting():
    current_time=datetime.now()
    timeofday_greeting="Good Morning! Have a nice day\n"
    if current_time.hour > 12 and current_time.hour < 17:
        timeofday_greeting="Good Afternoon! hope you had your lunch\n"
    elif current_time.hour >= 17 and current_time.hour < 22:
        timeofday_greeting="Good Evening\n"
    elif current_time.hour >= 22:
        timeofday_greeting="Hi! it's too late\n"
    return timeofday_greeting


def welcome(name):
    messages=[
        "Nice to meet you",
        "Lets have a great time together"
    ]
    print( f"{get_timeofday_greeting()},{random.choice(messages)}")

