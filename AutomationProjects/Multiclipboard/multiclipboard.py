import sys
import json
import clipboard

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}



if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    if command == "save":
        key = input("Enter a key for the current clipboard data: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data has been saved.")
    elif command == "load":
        key = input("Enter a key for the saved clipboard data: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data has been copied to the clipboard")
        else:
            print("Invalid key!")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass in just one command")
