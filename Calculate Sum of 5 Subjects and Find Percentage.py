#Calculate Sum of 5 Subjects and Find Percentage
# Input marks of 5 subjects
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))
subject5 = float(input("Enter marks for subject 5: "))

# Calculate the sum of the marks
total_marks = subject1 + subject2 + subject3 + subject4 + subject5

# Calculate the percentage
percentage = (total_marks / 500) * 100

# Print the total marks and percentage
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}%")