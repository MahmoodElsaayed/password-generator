from random import choice
from string import ascii_letters, digits, punctuation
from clipboard import copy


def main():
    password = ''.join(generate_password())
    copy_or_retry((password))


def generate_password():
    password_length = password_length_picker()
    complexity = complexity_picker()
    return [choice(complexity) for _ in range(password_length)]


def password_length_picker():
    while True:
        try:
            password_length = int(input(f"Password length [minimum=8] : "))
            if password_length >= 8:
                return password_length
            else:
                raise ValueError            
        except ValueError:
            print(f"'{password_length}' is invalid. valid input must be a number and be above 8")
        

def complexity_picker():
    while True:
        try:
            complexity_level = int(input(f"complexity level [available: 1, 2, 3] : "))
            if complexity_level in [1, 2, 3]:
                return characters_picker(complexity_level)
            else:
                raise ValueError
        except ValueError:
            print(f"'{complexity_level}' is invalid. valid input must be a number and from this list [1, 2, 3]")
        
    
def characters_picker(complexity):
    if complexity == 1:
        return ascii_letters
    elif complexity == 2:
        return ascii_letters+digits
    else:
        return ascii_letters+digits+punctuation


def copy_or_retry(password):
    while True:
        user_choice = input(f"Password: {password}\nCopy(y) or Try again(n)? ").lower().strip()
        if user_choice == "y":
            copy(password)
            print("Password has been copied to clipboard!!")
            break
        elif user_choice == "n":
            main()
        else:
            print(f"'{user_choice}' is invalid. valid inputs are the 'letters' y or x")


if __name__ == "__main__":
    main()
