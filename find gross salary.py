# Function to calculate gross salary
def calculate_gross_salary(basic_salary, hra, da):
    gross_salary = basic_salary + hra + da
    return gross_salary

# Input basic salary, HRA(House Rent Allowance), and DA(Dearness Allowance)
basic_salary = float(input("Enter the basic salary: "))
hra = float(input("Enter the HRA: "))
da = float(input("Enter the DA: "))

# Calculate gross salary
gross_salary = calculate_gross_salary(basic_salary, hra, da)

# Display the gross salary
print(f"The gross salary is: {gross_salary}")