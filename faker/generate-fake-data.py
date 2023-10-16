from faker import Faker
import pandas as pd

fake = Faker()
for _ in range(10):
  print(fake.name())
  print(fake.text())

# create a dataset with the following column names First Name, Age, Gender, Phone Number, Address, State, Pincode, Father Name using Faker library and save as csv file in the same directory

df = pd.DataFrame(columns=['First Name', 'Age', 'Gender', 'Phone Number', 'Address', 'State', 'Pincode', 'Father Name'])
for _ in range(10):
    df = df.append({'First Name': fake.first_name(), 'Age': fake.random_int(min=18, max=100), 'Gender': fake.random_element(elements=('Male', 'Female')), 'Phone Number': fake.phone_number(), 'Address': fake.address(), 'State': fake.state(), 'Pincode': fake.zipcode(), 'Father Name': fake.last_name()}, ignore_index=True)
    df.to_csv('fake_data.csv', index=False)