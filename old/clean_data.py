import pandas as pd
import string
from numpy import savetxt
pd.set_option('max_colwidth', 200)


df = pd.read_csv('data/brute/games.csv', sep=',').dropna()

# Remove metacritic's in beginning/end of labels + remove numbers
df['summary'] = df['summary'].str.replace(r"(?:(\[.*\] )|( \[.*\]))", "")\
    .str.replace(r'[0-9]*', '')


def clean_text(txt):
    txt = "".join(v for v in txt if v not in string.punctuation).lower()
    txt = txt.encode("utf8").decode("ascii", 'ignore')
    return txt


corpus = [clean_text(x) for x in df['summary']]

savetxt("data/cleaned/summaries.txt", corpus, newline="\n", fmt="%s")
