import pandas as pd

xls = pd.ExcelFile("Road-Accident-Safety-Data-Guide.xls")

for sheet_name in xls.sheet_names[1:]:
    data = xls.parse(sheet_name)
    data.to_csv("./data/{0}.csv".format(sheet_name.lower().replace(" ","_") + "_2016"), index=False)
