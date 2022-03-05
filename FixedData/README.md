This data contains the correct number of tickers at each moment in time.

Note: 
- stocks are referenced by **PERMNO**.
- The data now runs from 2000-01 to 2021-11

You can use **df_NeuralNetworks.csv** as is.

For **df_Merge.csv**, after finishing data processing (i.e. calculating returns), you need to run the following code:
- df_Merge = df_Merge[df_Merge["is_member"] == True]
- df_Merge = df_Merge.drop_duplicates(subset = ["PERMNO","month"])

Alternatively, you can use the 1/3/6/9/12-month returns from **df_NeuralNetworks.csv** directly.
