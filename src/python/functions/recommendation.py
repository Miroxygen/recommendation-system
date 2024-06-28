from functions.euclidean_distance import euclidean_distance
from functions.pearson import pearson

def recommend_movie(data, person, method="euclidean") :
  weights = {}
  sim_sums = {}
  if(method == 'pearson') :
    method = pearson
  else :
    method = euclidean_distance
  for other_people in data:
    if other_people != person:
      similarity = method(data, person, other_people)
      if(similarity > 0):
        for movie_scores in data[other_people]:
          if(movie_scores not in data[person]) or (data[person][movie_scores] == 0):
            weights.setdefault(movie_scores, 0) 
            weights[movie_scores] += (similarity * data[other_people][movie_scores])
            sim_sums.setdefault(movie_scores, 0)
            sim_sums[movie_scores] += similarity
  rankings = [(total / sim_sums[movie_scores], movie_scores) for movie_scores, total in weights.items()]
  rankings.sort()
  rankings.reverse()
  return rankings