# Password Security Rater
# Checks a password and shows its points, total score and security rating

MIN_LENGTH = 8
MAX_LENGTH = 15
SPECIAL_CHARACTERS = "!%&*+="
BONUS_LENGTH = 10
BONUS_POINTS = 20


def is_lower(character):
    # A range check is used because islower() also allows letters with accents
    return character >= "a" and character <= "z"


def is_upper(character):
    return character >= "A" and character <= "Z"


def is_number(character):
    return character >= "0" and character <= "9"


def find_invalid_characters(password):
    invalid = []
    for character in password:
        allowed = is_lower(character) or is_upper(character) or is_number(character) or character in SPECIAL_CHARACTERS
        if not allowed and character not in invalid:
            invalid.append(character)
    return invalid


def check_password(password):
    if password == "":
        print("No password was entered")
        return False
    valid = True
    length = len(password)
    if length < MIN_LENGTH:
        print("Length is", length, "characters which is too short")
        print("The minimum is", MIN_LENGTH)
        valid = False
    elif length > MAX_LENGTH:
        print("Length is", length, "characters which is too long")
        print("The maximum is", MAX_LENGTH)
        valid = False
    else:
        print("Length is", length, "characters which is OK")
    invalid = find_invalid_characters(password)
    if len(invalid) > 0:
        print("These characters are not allowed")
        for character in invalid:
            if character == " ":
                print("space")
            else:
                print(character)
        valid = False
    return valid


def get_password():
    while True:
        print()
        password = input("Enter a password to be rated ")
        if check_password(password):
            return password
        print("Please try again")


def calculate_score(password):
    lower = 0
    upper = 0
    numbers = 0
    specials = 0
    for character in password:
        if is_lower(character):
            lower = lower + 1
        elif is_upper(character):
            upper = upper + 1
        elif is_number(character):
            numbers = numbers + 1
        else:
            specials = specials + 1
    length = len(password)
    total = lower * 5 + upper * 5 + numbers * 10 + specials * 10
    print()
    print("Points Breakdown")
    if lower > 0:
        print("Lower case letters", lower, "x 5 is", lower * 5)
    if upper > 0:
        print("Upper case letters", upper, "x 5 is", upper * 5)
    if numbers > 0:
        print("Numbers", numbers, "x 10 is", numbers * 10)
    if specials > 0:
        print("Special characters", specials, "x 10 is", specials * 10)
    if length >= BONUS_LENGTH:
        print("Bonus for", BONUS_LENGTH, "or more characters is", BONUS_POINTS)
        total = total + BONUS_POINTS
    # elif is used because a password can only be made of one type
    if lower == length:
        print("Lower case letters only", length, "x 3 taken off is", length * 3)
        total = total - length * 3
    elif upper == length:
        print("Upper case letters only", length, "x 3 taken off is", length * 3)
        total = total - length * 3
    elif numbers == length:
        print("Numbers only", length, "x 5 taken off is", length * 5)
        total = total - length * 5
    return total


def get_rating(total):
    # <= is used because each rating in the brief includes its top number
    if total <= 20:
        return "Very low"
    elif total <= 40:
        return "Low"
    elif total <= 70:
        return "Medium"
    elif total <= 80:
        return "High"
    return "Very high"


def get_yes_no():
    while True:
        print()
        answer = input("Would you like to rate another password Y or N ").strip().upper()
        if answer == "Y" or answer == "N":
            return answer == "Y"
        print("Please enter Y or N")


print("Password Security Rater")
print()
print("Passwords must be", MIN_LENGTH, "to", MAX_LENGTH, "characters long")
print("They can only use lower case letters, upper case letters, numbers")
print("and these special characters", SPECIAL_CHARACTERS)
again = True
while again:
    total = calculate_score(get_password())
    print()
    print("Total score", total)
    print("Security rating", get_rating(total))
    again = get_yes_no()
print("Thank you for using the Password Security Rater")
