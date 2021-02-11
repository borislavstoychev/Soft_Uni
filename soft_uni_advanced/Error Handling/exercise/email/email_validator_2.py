from custom_exeption import NameTooShortError, MustContainAtSymbolError, InvalidDomainError
from helper import VALID_DOMAINS


def valid_email(e):
    try:
        name, domain = e.split("@")
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")
    try:
        name, extension = e.split(".")
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org,.net")
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org,.net")
    if len(name) < 4:
        raise NameTooShortError("Name must be more than 4 characters")
    return True


email = input()

while not email == "End":
    if valid_email(email):
        print("Email is valid")
    email = input()