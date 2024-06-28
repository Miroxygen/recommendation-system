from functions.euclidean_distance import euclidean_distance
from functions.movie_data import ratingsItemBased


#Gets one movies best matches of other movies
def getTopMatches(data, movie) :
  scores = [(euclidean_distance(data, movie, other_item), other_item) 
            for other_item in data if other_item != movie]
  scores.sort()
  scores.reverse()
  return scores

#Makes a table of all movies similarity to each other
def getSimilarMovies(data) :
  result = {}
  for movie in data:
    scores = getTopMatches(data, movie)
    result[movie] = scores
  return result

movie_table = getSimilarMovies(ratingsItemBased)



