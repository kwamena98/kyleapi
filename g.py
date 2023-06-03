import re

# def validate_email(email):
#     pattern = r'^[\w.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return re.match(pattern, email) is not None

def validate_email(message):
    pattern = r'[\w.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(pattern, message)
    if match:
        email = match.group()
        return email
    else:
        return None


def validate_name(name):
    if name== "Derrick Dadson":
        return True
    # pattern = r'^[A-Za-z\s]{1,50}$'
    # return re.match(pattern, name) is not None

def validate_phone_number(message):
    pattern = r'(?:\+|0)?[0-9]{10,15}'
    match = re.search(pattern, message)
    if match:
        phone_number = match.group()
        return phone_number
    else:
        return None
    




phone=validate_phone_number("Hi my number is +23327884328")
print(phone)