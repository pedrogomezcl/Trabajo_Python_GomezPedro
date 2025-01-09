import json
import os

DATA_FILE = "data/records.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def create_record():
    records = load_data()
    record = {
        "id": input("Enter ID: "),
        "name": input("Enter Name: "),
        "email": input("Enter Email: ")
    }
    records.append(record)
    save_data(records)
    print("Record created successfully.")

def read_records():
    records = load_data()
    if not records:
        print("No records found.")
    else:
        for record in records:
            print(record)

def update_record():
    records = load_data()
    record_id = input("Enter the ID of the record to update: ")
    for record in records:
        if record["id"] == record_id:
            record["name"] = input("Enter new Name: ") or record["name"]
            record["email"] = input("Enter new Email: ") or record["email"]
            save_data(records)
            print("Record updated successfully.")
            return
    print("Record not found.")

def delete_record():
    records = load_data()
    record_id = input("Enter the ID of the record to delete: ")
    for record in records:
        if record["id"] == record_id:
            records.remove(record)
            save_data(records)
            print("Record deleted successfully.")
            return
    print("Record not found.")
