import requests, json
from common.model import Account
BASE_URL = "http://localhost:5000/"

if __name__ == "__main__":
    while True:
        try:
            account_num = int(input("Enter the number of account: "))
        except ValueError:
            print("Input must be an integer")
            continue
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        r = requests.get(BASE_URL + "accounts/" + str(account_num))
        data = json.loads(r.text)
        acc = Account(**data)
        print(r.status_code, acc, sep="\n")