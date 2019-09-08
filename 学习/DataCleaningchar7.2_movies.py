import pandas as pd
import numpy as np

#   处理movies数据  分类变量(categorical)
#   DataFrame中的某行属于 多重分类

mnames = ['movie_id', 'title', 'genres']

movies = pd.read_csv('datasets/movielens/movies.dat', sep='::',
                       header=None, names=mnames)
print(movies.head(10))

#取出所有genre的集合
all_genres= []
for x in movies.genres:
    all_genres.extend(x.split('|'))
genres=pd.unique(all_genres)
print(genres)

zero_matrix = np.zeros(len(movies),len(genres)) #行数是movies，列数是genres，的ndarray对象
dummies = pd.DataFrame(zero_matrix,columns=genres) #构成了全0的DataFrame

