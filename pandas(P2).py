import pandas as pd
data={"Name":["Jack","John","Mike"],"Age":[25,27,30]}
df=pd.DataFrame(data,index=["Employee 1","Employee 2","Employee 3"])
#Add a new column
df["Job"]=["cook","N/A","cashier"]
#Add a new row
new_row=pd.DataFrame([{"Name":"Sandy","Age":28,"Job":"Engineer"},
                     {"Name":"Yang","Age":20,"Job":"Manager"}],
                   index=["Employee 4","Employee 5"])
df=pd.concat([df,new_row])
print(df)

