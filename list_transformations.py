# Problem Statement: You've been given a list of grades from an exam. You need to process and analyze these grades.
# Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the grades in descending order and print the sorted list.

grades.sort(reverse=True)
print("Grades in descending order:", grades)


# Task 2: Calculate the average grade and print it.

average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)