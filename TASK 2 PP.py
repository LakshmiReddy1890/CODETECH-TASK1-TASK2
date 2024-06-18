def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def calculate_letter_grade(average_grade):
    if average_grade >= 90:
        return 'A'
    elif average_grade >= 80:
        return 'B'
    elif average_grade >= 70:
        return 'C'
    elif average_grade >= 60:
        return 'D'
    else:
        return 'F'

def main():
    print("Welcome to the Student Grade Tracker!")

    grades = []

    while True:
        print("\nOptions:")
        print("1. Add a grade")
        print("2. Calculate average grade")
        print("3. Calculate letter grade")
        print("4. View all grades")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            try:
                grade = float(input("Enter the grade: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                else:
                    print("Invalid grade entered. Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '2':
            average = calculate_average(grades)
            print(f"The average grade is: {average:.2f}")

        elif choice == '3':
            if not grades:
                print("No grades entered yet.")
            else:
                average = calculate_average(grades)
                letter_grade = calculate_letter_grade(average)
                print(f"The letter grade is: {letter_grade}")

        elif choice == '4':
            if not grades:
                print("No grades entered yet.")
            else:
                print("All grades entered:")
                for index, grade in enumerate(grades, start=1):
                    print(f"Grade {index}: {grade}")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
