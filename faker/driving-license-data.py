# create a dataset in a csv format for driving license which should contain column names firstname, lastname, email, phone, address, city, state, zipcode, country, dob, gender, license_no, license_type, license_expiry_date, license_issue_date, license_issue_place, license_issue_country, license_issue_state, license_issue
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 10), columns=list('abcdefghij'))
print(df)
df.to_csv('driving-license-data.csv')


