import pandas as pd
import numpy as np
json_df = pd.read_json("bitly.json", lines=True)
json_df.isnull().any(axis = 0) 
json_df = json_df.replace([np.nan, "Missing"], [" ", "Unknown"])
json_df_tz = json_df['tz'].value_counts().head(10)
tz_count = json_df['tz'].value_counts()
json_df_tz.plot.bar()
tokens_df = json_df['a'].str.split(n = 1, expand = True).add_prefix("Token_")
tokens_frequency = tokens_df['Token_0'].value_counts()
tokens_frequency.head().plot.bar()
tokens_df = tokens_df.replace(np.nan, 'Missing')
tokens_df["os"] = 'Not Windows'
tokens_df["os"][tokens_df["Token_1"].str.find("Windows") != -1] = "Windows"


