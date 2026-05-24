import json
from colorama import Fore, Style, init

init(autoreset=True)


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def is_valid_phone(phone):
    return phone.lstrip("+").isdigit()


def add_contact(args, contacts):
    if len(args) != 2:
        return "Please provide both name and phone number."
    name, phone = args

    if any(name_rew["name"] == name for name_rew in contacts):
        return f"Contact {name} already exists."

    if not is_valid_phone(phone):
        return "Phone number must contain only digits."

    contact_id = len(contacts) + 1
    contacts.append({"id": contact_id, "name": name, "phone": phone})

    with open("contact_db.json", "w", encoding="utf-8") as file:
        json.dump(contacts, file, ensure_ascii=False, indent=4)
    return f"Contact {name} added with phone number {phone}."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Please provide both name and phone number."
    name, phone = args
    if not is_valid_phone(phone):
        return "Phone number must contain only digits."
    for contact in contacts:
        if contact["name"] == name:
            contact["phone"] = phone
            with open("contact_db.json", "w", encoding="utf-8") as file:
                json.dump(contacts, file, ensure_ascii=False, indent=4)
            return f"Contact {name} updated with new phone number {phone}."
    return f"Contact {name} not found."


def show_contact(args, contacts):
    if not args:
        return "Please provide a contact name."
    name = args[0]
    try:
        with open("contact_db.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)
            for contact in contacts:
                if contact["name"] == name:
                    return f"Contact {name} has phone number {contact['phone']}."
            return f"Contact {name} not found. "
    except (FileNotFoundError, json.JSONDecodeError):
        return f"Contact {name} not found. "


def show_all_contacts(contacts):
    try:
        with open("contact_db.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)
        if contacts:
            return "\n".join([
                f"{c['id']}. {c['name']}: {c['phone']}"
                for c in contacts
            ])
        else:
            return "No contacts found."
    except (FileNotFoundError, json.JSONDecodeError):
        return "No contacts found."


def main():
    try:
        with open("contact_db.json", "r", encoding="utf-8") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []

    print(Fore.CYAN + "Welcome to the assistant bot!")
    print(Fore.GREEN + "Available commands: \n-> hello \n-> add <name> <phone> \n-> change <name> <phone> \n-> phone <name> \n-> all \n-> close/exit")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.YELLOW + "Good bye!")
            break

        elif command == "hello":
            print(Fore.GREEN + "How can I help you?")

        elif command == "add":
            print(Fore.GREEN + add_contact(args, contacts))

        elif command == "change":
            print(Fore.GREEN + change_contact(args, contacts))

        elif command == "phone":
            print(Fore.GREEN + show_contact(args, contacts))

        elif command == "all":
            print(Fore.GREEN + show_all_contacts(contacts))

        else:
            print(Fore.RED + "Invalid command.")


if __name__ == "__main__":
    main()
