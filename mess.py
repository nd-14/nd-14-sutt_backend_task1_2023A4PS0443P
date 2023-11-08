import pandas as pd
import json

file_path = "menu.xlsx"
df = pd.read_excel(file_path)

df.columns = ["2023-09-01", "2023-09-02", "2023-09-03", "2023-09-04", "2023-09-05", "2023-09-06", "2023-09-07", "2023-09-08", "2023-09-09", "2023-09-10", "2023-09-11", "2023-09-12", "2023-09-13", "2023-09-14", "2023-09-15"]
df.drop([0 , 11, 21], axis = 0, inplace = True)
df=df.rename(index= {1:'0',2:'1',3: '2',4: '3',5: '4',6: '5',7: '6',8: '7',9: '8',10: '9',12: '10',13: '11',14: '12',15: '13',16: '14',17: '15',18: '16',19: '17',20: '18',22: '19',23: '20',24: '21',25: '22',26: '23',27: '24',28: '25',29: '26'})

df = df.astype(str)

df.to_json('modified.json', orient='columns')

data = pd.read_json('modified.json')

new_data = {}

for date, items in data.items():
    date_str = date.strftime('%Y-%m-%d')

    breakfast = []
    lunch = []
    dinner = []

    for index, item in items.items():
        if item != 'nan' and item[0] != '*':
            if index<=9 and index>0:
                breakfast.append(item)
            elif index<=18 and index>10:
                lunch.append(item)
            elif index>19:
                dinner.append(item)
                
    new_data[date_str] = {
        "BREAKFAST": breakfast,
        "LUNCH": lunch,
        "DINNER": dinner
    }

with open("menu.json", "w") as json_file:
    json.dump(new_data, json_file, indent=2)