import pandas as pd
import json

excel_data_df = pd.read_csv('currency_codes_csv.csv')
currency_dict = {}
currency_dict_2 = {}
i=0
for index, row in excel_data_df.iterrows():
    temp_dict = {}
    currency_dict[row['country']] = row['currency_code']
    i=i+1
    temp_dict[row['country']] = row['currency_code']
    currency_dict_2[i] = temp_dict

with open("currency_dict_2.json", "w") as jsonFile:
    json.dump(currency_dict_2, jsonFile)

with open("currency_dict.json", "w") as jsonFile:
    json.dump(currency_dict, jsonFile)

json_str = excel_data_df.to_json()

print('Excel Sheet to JSON:\n', json_str)