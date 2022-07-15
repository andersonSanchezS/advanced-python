# Decorator

def my_decorator(func):
    def wrapper(greeting, emoji):
        print("------------1---------------")
        func(greeting, emoji)
        print("------------2---------------")

    return wrapper


@my_decorator
def hello(greeting: str, emoji: str):
    print(f'{greeting} {emoji}')


# Exercise

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            fn(*args, **kwargs)
        else:
            return 'User not authenticated'

    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


print(message_friends(user1))
