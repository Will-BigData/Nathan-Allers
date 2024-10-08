import requests, json
from common.model import Account
BASE_URL = "http://localhost:5000/"

def get_user_int(prompt: str, requirements: str="Invalid input.", valid_func=lambda x: True) -> int:
    valid = False
    result = None
    while not valid:
        try:
            result = int(input(prompt))
            valid = valid_func(result)
            if not valid:
                print(requirements)
        except ValueError:
            print("Input must be an integer.\n")
    return result

def get_user_account() -> Account:
    account = {
        "_account_number": get_user_int("Enter the account number: ", "Number must be positive.", lambda x: x > 0),
        "_routing_number": get_user_int("Enter the routing number: ", "Number must be positive.", lambda x: x > 0),
        "_balance": get_user_int("Enter the balance: ")
        }
    return Account(**account)

def add_account():
    account = get_user_account()
    print()
    r = requests.post(BASE_URL + "accounts", json=vars(account))
    if r.status_code == 200:
        print("Account added successfully.\n")
    else:
        print("Failed to add account.\n" + r.text)

def get_all_accounts():
    r = requests.get(BASE_URL + "accounts")
    accounts = [Account(**account) for account in json.loads(r.text)]
    print("All accounts:\n")
    for account in accounts:
        print(account, end="\n\n")

def get_account_by_id():
    account_id = get_user_int("Enter the account number: ", "Account number must be positive.", lambda x: x > 0)
    r = requests.get(BASE_URL + "accounts/" + str(account_id))
    if r.status_code == 200:
        print(Account(**json.loads(r.text)))
    else:
        print(r.text)

OPTION_NAME_FUNC = [
    ("Add account", add_account),
    ("Get all accounts", get_all_accounts),
    ("Get account by ID", get_account_by_id),
]

OPTION_LISTING_FUNC = [(str(i) + ". " + option_name, func) for i, (option_name, func) in enumerate(OPTION_NAME_FUNC, start=1)]

if __name__ == "__main__":
    print(dir(Account(0, 0, 0)))
    print("Welcome to the banking app.")
    while True:
        try:
            print("\nOptions:")
            for option_listing, _ in OPTION_LISTING_FUNC:
                print(option_listing)
            print()
            option = get_user_int("Enter number of your choice (CTRL+C to exit): ", "Option not in option list.", lambda x: x > 0 and x <= len(OPTION_LISTING_FUNC))
            print()
            OPTION_LISTING_FUNC[option-1][1]()
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except IndexError:
            print("Unknown option.")