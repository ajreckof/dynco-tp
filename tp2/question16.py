#%%
import pandas as pd
import os 
import matplotlib.pyplot as plt

csv_folder = "results_VisitorOpenIssue/"

df = None
dates = []

for file in os.listdir(csv_folder):
    file_df = pd.read_csv(csv_folder + file)
    file_date = file.removesuffix(".csv").removeprefix("json-ld-syntax-")
    dates.append(file_date)
    file_df["date"] = file_date
    if df is None : 
        df= file_df
    else :
        df= pd.concat([df, file_df], ignore_index=True)

colors = ["red", "green", "purple", "blue", "brown"]
df.sort_values(by='names')
values = df.groupby(["date", "names"]).sum().unstack().fillna(0)
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(11,13))

values.plot(kind= "bar", ax=axes[0],y="contributors", color=colors, rot =0)
axes[0].set_title("Number of Contributors")

values.plot(kind= "bar", ax=axes[1],y="comments", color=colors, legend=False, rot=0)
axes[1].set_title("Number of Comments")

plt.subplots_adjust(hspace=0.2)
# %%
values
# %%
