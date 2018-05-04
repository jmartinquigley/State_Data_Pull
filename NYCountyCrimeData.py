import ijson
import matplotlib.pyplot as plt

filename = "/Users/josephquigley/Downloads/nydata.json"
with open(filename, 'r') as f:
    objects = ijson.items(f, 'meta.view.columns.item')
    columns = list(objects)

column_names = [col["fieldName"] for col in columns]

good_columns = [
        "county",
        "year",
        "population",
        "index_count",
        "index_rate",
        "violent_count",
        "violent_rate",
        "property_count",
        "property_rate",
        "firearm_count",
        "firearm_rate"]

data = []
with open(filename, 'r') as f:
    objects = ijson.items(f, 'data.item')
    for row in objects:
        selected_row = []
        for item in good_columns:
            selected_row.append(row[column_names.index(item)])
        data.append(selected_row)
        
import pandas as pd

df = pd.DataFrame(data)
df.columns = good_columns
#df.to_csv('NYStateData.csv')

#the function below allows you to select specific rows depending on cell content
countydata = df.loc[df['county'] == 'Schoharie']
#issue: index is being used as the x axis
yearpop = countydata[['year','population']]
yearpop = yearpop.astype(float)
yearpop = yearpop.sort_values(by = ['year'],ascending = 1)
yearpop = yearpop.set_index('year', inplace = False)
print(yearpop)
yearpop.plot()
plt.show()


