import csv

FILE = "students.csv"


def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    with open(FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, name, marks])

    print("Student added successfully!")


def view_students():
    try:
        with open(FILE, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("No student records found.")


def main():
    while True:
        print("\nStudent Record Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                print("Program ended.")
                break
            else:
                print("Invalid choice.")

        except Exception as e:
            print("Error:", e)


main()
