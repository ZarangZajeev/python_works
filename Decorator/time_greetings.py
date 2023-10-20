from datetime import datetime


def capitalise(fn):
    def wrapper():
        res=fn()
        res=res.upper()
        return res
    return wrapper

@capitalise
def greetings_bytime():
    current_time=datetime.now()
    current_hour=current_time.hour

    if(5<=current_hour<12):
        return ("Good Morning")
    elif(12<=current_hour<18):
        return ("Good Afternoon")
    else:
        return ("Good evening")

print(greetings_bytime())