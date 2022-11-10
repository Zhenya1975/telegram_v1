import pandas as pd
import json

excel_data_df = pd.read_csv('currency_codes_csv.csv')
currency_dict = {}
for index, row in excel_data_df.iterrows():
    currency_dict[row['country']] = row['currency_code']

with open("currency_dict.json", "w") as jsonFile:
    json.dump(currency_dict, jsonFile)

json_str = excel_data_df.to_json()

print('Excel Sheet to JSON:\n', json_str)