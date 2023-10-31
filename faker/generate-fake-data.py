import calendar

from faker import Faker
import random
import csv

fake = Faker()


def generate_random_aadhar_data():
    # Generate random name
    name = fake.name()

    # Generate random address
    address = fake.address()

    # Generate random date of birth
    dob = fake.date_of_birth(minimum_age=18, maximum_age=60)

    # Generate random gender
    gender = random.choice(['Male', 'Female'])

    # Generate random Aadhar number
    aadhar_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])

    # Create a dictionary with the generated data
    aadhar_data = {
        'Name': name,
        'Address': address,
        'Date of Birth': dob,
        'Gender': gender,
        'Aadhar Number': aadhar_number
    }

    return aadhar_data


def generate_random_driving_license_data():
    # Generate random name
    name = fake.name()

    # Generate random address
    address = fake.address()

    # Generate random date of birth
    dob = fake.date_of_birth(minimum_age=18, maximum_age=80)

    # Generate random driving license number
    license_number = ''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(15)])

    # Generate random license issue date
    issue_date = fake.date_between(start_date='-5y', end_date='today')

    # Generate random license expiry date
    expiry_date = fake.date_between(start_date='today', end_date='+5y')

    # Create a dictionary with the generated data
    license_data = {
        'Name': name,
        'Address': address,
        'Date of Birth': dob,
        'License Number': license_number,
        'Issue Date': issue_date,
        'Expiry Date': expiry_date
    }
    return license_data


# Generate random payslip data
def generate_random_payslip_data():
    # Generate random name
    name = fake.name()

    # Generate random employeed ID
    employee_id = ''.join([str(random.randint(0, 9)) for _ in range(6)])

    # Generate random job title
    job_title = random.choice(['Software Engineer', 'Data Analyst', 'Project Manager', 'Sales Manager'])

    # match the job title to appropriate department
    def get_department(job_title: str) -> str:
        if job_title == 'Software Engineer':
            return 'Information Technology'
        elif job_title == 'Data Analyst':
            return 'Data Analyst'
        elif job_title == 'Project Manager':
            return 'Human Resources'
        elif job_title == 'Sales Manager':
            return 'Sales'
        else:
            return 'Marketing'

    # Generate random department name
    department_name = get_department("job_title")

    # Generate random location
    location = random.choice(['Bangalore', 'Mumbai', 'Pune', 'Chennai'])

    # Generate random date of joining
    date_of_joining = fake.date_between(start_date='-5y', end_date='today')

    # Generate random bank name
    bank_name = random.choice(['HDFC', 'ICICI', 'SBI', 'BOB', 'PNB', 'KOTAK', 'AXIS', 'YES BANK'])

    # Generate random account number
    account_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])

    #  Generate random PAN number and it should be unique
    pan_number = ''.join([random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(10)])

    # Generate random PF number
    pf_account_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])

    # Generate random UAN number
    uan_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])

    # Salary Status
    salary_status = 'credited'

    # Generate a value of no of days in month for example if the current month is October then the value will be 31
    days_in_month = calendar.monthrange(2023, 12)[1]

    # Generate no of available days
    available_days = random.randint(1, days_in_month)

    # Generate no of paid days
    paid_days = random.randint(1, available_days)

    # Generate no of leave days
    leave_days = available_days - paid_days


    # Generate a dictionary with the generated data
    payslip_data = {
        'Name': name,
        'Employee ID': employee_id,
        'Job Title': job_title,
        'Department Name': department_name,
        'Location': location,
        'Date of Joining': date_of_joining,
        'Bank Name': bank_name,
        'Account Number': account_number,
        'PAN Number': pan_number,
        'PF Account Number': pf_account_number,
        'UAN Number': uan_number,
        'Salary Status': salary_status,
        'Available Calendar Days': available_days,
        'Paid Days': paid_days,
        'Leave Days': leave_days
    }
    return payslip_data


# Example usage and CSV writing
with open('random_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Gender', 'Date of Birth', 'Address', 'Aadhar Number', 'License Number', 'Issue Date', 'Expiry Date',
                  'Employee ID', 'Job Title', 'Department Name', 'Location', 'Date of Joining', 'Bank Name', 'Account Number', 'PAN Number', 'PF Account Number', 'UAN Number', 'Salary Status', 'Available Calendar Days', 'Paid Days', 'Leave Days']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write CSV header
    writer.writeheader()

    # Write 20 rows of data
    for _ in range(20):
        random_aadhar_data = generate_random_aadhar_data()
        random_license_data = generate_random_driving_license_data()
        random_payslip_data = generate_random_payslip_data()

        # Merge both datasets
        merged_data = {**random_aadhar_data, **random_license_data, **random_payslip_data}

        # Write row to CSV
        writer.writerow(merged_data)

print("CSV file 'random_data.csv' generated successfully.")
