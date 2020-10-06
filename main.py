import pandas as pd
# Math functions, we'll only need the sqrt function so let's import only that
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

movies_df = pd.read_csv('./ml-latest/movies.csv')
ratings_df = pd.read_csv('./ml-latest/ratings.csv')
movies_df['year'] = movies_df.title.str.extract('(\(\d\d\d\d\))', expand=False)


print(movies_df.head())
# print(ratings_df.head())
