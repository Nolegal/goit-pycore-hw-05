from functools import wraps



def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner



def phone_error(func):
    @wraps(func)
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Give me name of contact please."

    return inner


def change_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Please input right contact."

    return inner



@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts.update({name : phone})
   
    return "Contact added."


@change_error
def change_contact(args, contacts):
    name, phone = args
    contacts.update({name : phone})
    return "Contact updated."

@phone_error
def show_phone(args,contacts): 
    #name, = args
    name=args[0]
    res = contacts.get(name)
    return res



def show_all(contacts):
    return  contacts




def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
                print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts)) 
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()