import requests, functools
from common.model import Account
from common.config import ConfigManager
from common.util import handle_with_message, get_user_int

config = ConfigManager.get_config("frontend")
BASE_URL = f"http://{config["server_host"]}:{config["server_port"]}"
handle_connection_error = handle_with_message(requests.exceptions.ConnectionError, "Connection failed")
handle_bad_response = handle_with_message(requests.exceptions.JSONDecodeError, "Malformed response")

get_positive_user_int = functools.partial(get_user_int, requirements="Number must be positive.", valid_func=lambda x: x > 0)

def get_user_account() -> Account:
    account_number = get_positive_user_int("Enter the account number: ")
    routing_number = get_positive_user_int("Enter the routing number: ")
    balance = get_user_int("Enter the balance: ")

    return Account(account_number, routing_number, balance)

@handle_connection_error
@handle_bad_response
def get_server_account_by_id(account_id: int) -> Account | str:
    r = requests.get(BASE_URL + f"/accounts/{account_id}")
    if r.status_code == 200:
        return Account(**r.json())
    return r.text

@handle_connection_error
def add_account():
    account = get_user_account()
    print()
    r = requests.post(BASE_URL + "/accounts", json=vars(account))
    if r.status_code == 200:
        print("Account added successfully.\n")
    else:
        print("Failed to add account.\n" + r.text)

@handle_connection_error
@handle_bad_response
def get_all_accounts():
    r = requests.get(BASE_URL + "/accounts")
    if r.status_code == 200:
        accounts = [Account(**account) for account in r.json()]
        print("All accounts:\n")
        for account in accounts:
            print(account, end="\n\n")
    else:
        print(r.text)

def get_account_by_id():
    account_id = get_positive_user_int("Enter the account number: ")
    print()
    r = get_server_account_by_id(account_id)
    if isinstance(r, Account) or isinstance(r, str):
        print(r)

def update_account():
    account_id = get_positive_user_int("Enter the account number: ")
    new_routing_number = None
    new_balance = None
    try:
        new_routing_number = get_positive_user_int("Enter a new routing number (CTRL+C to skip): ")
    except KeyboardInterrupt:
        pass
    try:
        new_balance = get_positive_user_int("Enter a new balance (CTRL+C to skip): ")
    except KeyboardInterrupt:
        pass
    print()
    r = requests.patch(BASE_URL + f"/accounts/{account_id}", json=vars(Account(_routing_number=new_routing_number, _balance=new_balance)))
    print(r.text)
    
def delete_account():
    account_id = get_positive_user_int("Enter the account number: ")
    print()
    r = requests.delete(BASE_URL + f"/accounts/{account_id}")
    print(r.text)

OPTION_FUNCS = [
    add_account,
    get_all_accounts,
    get_account_by_id,
    update_account,
    delete_account
]

OPTION_LISTINGS = [(str(i) + ". " + func.__name__.replace('_', ' ').capitalize(), func) for i, func in enumerate(OPTION_FUNCS, start=1)]

def main():
    print("Welcome to the banking app.")
    while True:
        try:
            print("\nOptions:")
            for option_listing, _ in OPTION_LISTINGS:
                print(option_listing)
            print()
            option = get_user_int("Enter number of your choice (CTRL+C to exit): ", "Option not in option list.", lambda x: x > 0 and x <= len(OPTION_LISTINGS))
            print()
            OPTION_LISTINGS[option-1][1]()
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except IndexError:
            print("Unknown option.")

if __name__ == "__main__":
    main()