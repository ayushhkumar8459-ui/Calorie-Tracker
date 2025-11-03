# gradebook.py
# Made by:Tushar Chand
# Date: 03-Nov-2025
# Title: GradeBook Analyzer - CLI Tool

def print_menu():
    print("\nWelcome to GradeBook Analyzer 📊")
    print("Choose input method:")
    print("1. Manual Entry")
    print("2. Load from CSV")
    print("3. Exit")

print_menu()


import csv

def manual_entry():
    marks = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        name = input("Student Name: ")
        score = float(input("Marks: "))
        marks[name] = score
    return marks

def load_csv(filename):
    marks = {}
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            name, score = row[0], float(row[1])
            marks[name] = score
    return marks



import statistics

def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(marks_dict.values())

def find_max_score(marks_dict):
    return max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict.values())




def assign_grades(marks_dict):
    grades = {}
    for name, score in marks_dict.items():
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades[name] = grade
    return grades

def grade_distribution(grades_dict):
    dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    for grade in grades_dict.values():
        dist[grade] += 1
    return dist


def pass_fail_lists(marks_dict):
    passed = [name for name, score in marks_dict.items() if score >= 40]
    failed = [name for name, score in marks_dict.items() if score < 40]
    return passed, failed

def print_results(marks_dict, grades_dict):
    print("\nName\t\tMarks\tGrade")
    print("-" * 30)
    for name in marks_dict:
        print(f"{name}\t\t{marks_dict[name]}\t{grades_dict[name]}")

def main():
    while True:
        print_menu()
        choice = input("Enter choice (1/2/3): ")
        if choice == '1':
            marks = manual_entry()
        elif choice == '2':
            filename = input("Enter CSV filename: ")
            marks = load_csv(filename)
        elif choice == '3':
            print("Exiting GradeBook Analyzer. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")
            continue

        avg = calculate_average(marks)
        med = calculate_median(marks)
        max_score = find_max_score(marks)
        min_score = find_min_score(marks)
        grades = assign_grades(marks)
        dist = grade_distribution(grades)
        passed, failed = pass_fail_lists(marks)

        print(f"\nAverage: {avg:.2f}, Median: {med}, Max: {max_score}, Min: {min_score}")
        print("Grade Distribution:", dist)
        print(f"Passed ({len(passed)}): {passed}")
        print(f"Failed ({len(failed)}): {failed}")
        print_results(marks, grades)

if __name__ == "__main__":
    main()