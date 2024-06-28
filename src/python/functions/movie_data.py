import pandas

ratings_csv = pandas.read_csv('data/movies_large/ratings.csv', delimiter=';')

ratings = {}

ratingsItemBased = {}

for index, row in ratings_csv.iterrows():
  ratings.setdefault(int(row['UserId']), {})
  ratings[row['UserId']].setdefault(int(row['MovieId']))
  ratings[row['UserId']][row['MovieId']] = row['Rating']

for index, row in ratings_csv.iterrows():
  ratingsItemBased.setdefault(int(row['MovieId']), {})
  ratingsItemBased[row['MovieId']].setdefault(int(row['UserId']))
  ratingsItemBased[row['MovieId']][row['UserId']] = row['Rating']

users_csv = pandas.read_csv('data/movies_large/users.csv', delimiter=';')

users = {}

for index, row in users_csv.iterrows():
  users.setdefault(int(row['UserId']), row['Name'])

movies_csv = pandas.read_csv('data/movies_large/movies.csv', delimiter=';')

movies = {}

for index, row in movies_csv.iterrows():
  if int(row['MovieId']) not in movies:
    movies[int(row['MovieId'])] = []
  movies[int(row['MovieId'])].append((row['Title'], row['Year']))

