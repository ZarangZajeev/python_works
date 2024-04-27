import re

def is_email(email):
    pattern="[a-z0-9_.]+@[a-z]{2,}.com"
    return bool(re.fullmatch(pattern,email))

print(is_email("zarangzajeev@gmail.com"))