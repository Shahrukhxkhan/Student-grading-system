def load_data(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, grade = line.strip().split(',')
                students.append((name, grade))
    except FileNotFoundError:
        pass  # File will be created on save
    return students

def save_data(filename, students):
    with open(filename, 'w') as file:
        for name, grade in students:
            file.write(f"{name},{grade}\n")

def display_menu():
    print("\nStudent Grade Manager")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Edit Student Grade")
    print("5. Delete Student")
    print("6. Exit")

def is_valid_grade(grade):
    return grade.upper() in ['A', 'B', 'C', 'D', 'F']

def add_student(students):
    name = input("Enter student name: ").strip()
    grade = input("Enter grade (A, B, C, D, F): ").strip().upper()

    if not name or not grade:
        print("❌ Name and grade cannot be empty.")
        return
    if not is_valid_grade(grade):
        print("❌ Invalid grade. Please enter A, B, C, D, or F.")
        return

    students.append((name, grade))
    print("✅ Student added.")

def view_students(students):
    if not students:
        print("No student records found.")
    else:
        print("\n--- Student Records ---")
        for name, grade in students:
            print(f"{name}: {grade}")

def search_student(students):
    query = input("Enter student name to search: ").strip()
    found = False
    for name, grade in students:
        if name.lower() == query.lower():
            print(f"✅ Found: {name} - Grade: {grade}")
            found = True
            break
    if not found:
        print("❌ Student not found.")

def edit_student(students):
    query = input("Enter student name to edit: ").strip()
    for i, (name, grade) in enumerate(students):
        if name.lower() == query.lower():
            new_grade = input(f"Enter new grade for {name} (A, B, C, D, F): ").strip().upper()
            if not is_valid_grade(new_grade):
                print("❌ Invalid grade. Must be A, B, C, D, or F.")
                return
            students[i] = (name, new_grade)
            print("✅ Grade updated.")
            return
    print("❌ Student not found.")

def delete_student(students):
    query = input("Enter student name to delete: ").strip()
    for i, (name, grade) in enumerate(students):
        if name.lower() == query.lower():
            del students[i]
            print("✅ Student deleted.")
            return
    print("❌ Student not found.")

def main():
    filename = "grades.txt"
    students = load_data(filename)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)
            save_data(filename, students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            edit_student(students)
            save_data(filename, students)
        elif choice == "5":
            delete_student(students)
            save_data(filename, students)
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
