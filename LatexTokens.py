import pandas as pd

tokens_df = pd.read_csv("im2latex_formulas.norm.csv")

tokens_list = list(tokens_df["formulas"])

print(tokens_list[0])
