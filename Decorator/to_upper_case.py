def capitalise(fn):
    def wrapper():
        res=fn()
        res=res.upper()
        return res
    return wrapper

@capitalise
def morning_greetings():
    return "good morning"

@capitalise
def afternoon_greetings():
    return "good afternoon"

print(morning_greetings())
print(afternoon_greetings())