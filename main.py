from modules import crud

def main():
    print("CRUD Application")
    while True:
        print("\nMenu:")
        print("1. Create Record")
        print("2. Read Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            crud.create_record()
        elif choice == '2':
            crud.read_records()
        elif choice == '3':
            crud.update_record()
        elif choice == '4':
            crud.delete_record()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
