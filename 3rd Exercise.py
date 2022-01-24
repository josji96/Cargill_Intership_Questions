import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
pd.set_option('display.max_columns', None)

df1 = pd.read_excel('data.xlsx', sheet_name = 'Invoices')
df2 = pd.read_excel('data.xlsx', sheet_name = 'InvoiceLines')
df3 = pd.read_excel('data.xlsx', sheet_name = 'Stock')
DF_1 = df1[df1["InvoiceDateKey"].astype(str).str.contains("201501.*") |df1["InvoiceDateKey"].astype(str).str.contains("201502.*") |df1["InvoiceDateKey"].astype(str).str.contains("201503.*")]


DF_2 = df2.loc[:,["InvoiceID","StockID"]]


join= DF_1.merge(DF_2, on ='InvoiceID', how ='left')
DF_3 = df3.loc[:,["Maker","StockID"]]
join2=join.merge(DF_3, on = "StockID", how = "left")


print("The Top 3 most sold brands for Q1 are:" + "\n"+ str(join2["Maker"].value_counts().head(3)))

df4 = pd.read_excel('data.xlsx', sheet_name = 'Invoices')
df5 = pd.read_excel('data.xlsx', sheet_name = 'InvoiceLines')
df6 = pd.read_excel('data.xlsx', sheet_name = 'Stock')
DF_4 = df4[df4["InvoiceDateKey"].astype(str).str.contains("201507.*") |df4["InvoiceDateKey"].astype(str).str.contains("201508.*") |df4["InvoiceDateKey"].astype(str).str.contains("201509.*")]

DF_5 = df5.loc[:,["InvoiceID","StockID"]]


join3= DF_4.merge(DF_5, on ='InvoiceID', how ='left')
DF_6 = df6.loc[:,["Maker","StockID"]]
join4=join3.merge(DF_6, on = "StockID", how = "left")


print("The Top 3 most sold brands for Q3 are:" + "\n"+ str(join4["Maker"].value_counts().head(3)))


df7 = pd.read_excel('data.xlsx', sheet_name = 'Invoices')
df8 = pd.read_excel('data.xlsx', sheet_name = 'InvoiceLines')
df9 = pd.read_excel('data.xlsx', sheet_name = 'Stock')
df10 = pd.read_excel('data.xlsx', sheet_name = 'Colors')
DF_7 = df7[df7["InvoiceDateKey"].astype(str).str.contains("2012.*") |df7["InvoiceDateKey"].astype(str).str.contains("2013.*") |df7["InvoiceDateKey"].astype(str).str.contains("2014.*") | df7["InvoiceDateKey"].astype(str).str.contains("2015.*")]

DF_8 = df8.loc[:,["InvoiceID","StockID"]]

join5= DF_7.merge(DF_8, on ='InvoiceID', how ='left')

DF_9 = df9.loc[:,["Maker","StockID","ColorID"]]

join6 = join5.merge(DF_9, on = "StockID", how = "outer")

DF_10 = df10.loc[:,["ColorID","Color"]]

join7 = join6.merge(DF_10, on = "ColorID", how = "left")

print("The Top 3 most sold color for the years from 2012 to 2015 are:" + "\n"+ str(join7["Color"].value_counts().head(3)))

