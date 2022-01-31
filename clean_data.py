import pandas as pd

# from pd_options import *
from utils import *


df = pd.read_csv('data/brute/booksummaries.csv', sep=';')
df.drop(columns=['0', '1', '4'], inplace=True)
df['book_genre'] = df.book_genre.apply(lambda x: extract_genre(x))

# df.to_csv('data/cleaned/booksummaries.csv', index=False)

nan_elems = df['book_summary'].isnull()
series = df['book_summary'][~nan_elems]
series = series.apply(remove_first_withespace)
print(series)
series.to_csv('data/cleaned/book_summaries.csv', index=False)

