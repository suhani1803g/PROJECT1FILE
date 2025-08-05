# Sample student data
students = [
    {"name": "Atufa", "marks": [95, 88, 92]},
    {"name": "Ragini", "marks": [72, 65, 70]},
    {"name": "Zainab", "marks": [59, 60, 52]},
    {"name": "Saba", "marks": [45, 38, 52]}
]

def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

# Process each student
total_class_score = 0
topper = None
highest_total = 0

print("Student Summary:\n")
for student in students:
    total = sum(student["marks"])
    average = total / len(student["marks"])
    grade = assign_grade(average)
    total_class_score += average

    print(f"Name: {student['name']}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}\n")

    if total > highest_total:
        highest_total = total
        topper = student["name"]

# Class average
class_average = total_class_score / len(students)
print(f"Class Average: {class_average:.2f}")
print(f"Topper: {topper} with {highest_total} marks")

print("\nSummary:")
print("This program calculates total, average, and grade for each student,")
print("determines the class average, and identifies the topper based on total marks.")
print("This is my project1 of GuviHcl")