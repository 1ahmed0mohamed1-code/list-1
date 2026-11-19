students = []

def add_id():
    name = input("enter your name: ")
    code = input("enter your code: ")
    specialty = input("enter your specialty: ")
    students.append({"name": name, "code": code, "specialty": specialty})
    print("Saved!\n")

def show_list():
    print("\n--- Your Students ---")
    if not students:
        print("No students saved yet.")
    else:
        for student in students:
            print(f"Name: {student['name']} | Code: {student['code']} | Specialty: {student['specialty']}")
    print("---------------------\n")

def main():
    print("--- list_id---")
    while True:
        print("1. add_list")
        print("2. show_list")
        print("3. exit")
        choice = input("choose (1/2/3): ")
        if choice == "1":
            add_id()
        elif choice == "2":
            show_list()
        elif choice == "3":
            print("goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

main()