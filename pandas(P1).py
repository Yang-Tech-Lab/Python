import pandas as pd

#raw_data=pd.read_excel('./salarydata.xlsx')
#print(raw_data)

#DataFrame
data={'Name':['Jack','John','Madison','Yang'],'Salary':[1500,2100,2200,2400]}
mydata=pd.DataFrame(data)
mydata.to_excel('./mydata.xlsx',index=False)