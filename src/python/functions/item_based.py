from functions.euclidean_distance import euclidean_distance
from functions.generate_itemset import movie_table

#Makes itembased recommendations
def item_based_recommendation(data, user) :
  user_ratings = data[user]
  weights = {}
  sim_sum = {}
  for(movie, rating) in user_ratings.items() :
    for(sim, other_movie) in movie_table[movie]:
      if other_movie in user_ratings: continue
      weights.setdefault(other_movie, 0)
      weights[other_movie] += sim * rating
      sim_sum.setdefault(other_movie, 0)
      sim_sum[other_movie] += sim
  rankings = [(total / sim_sum[movie], movie) for movie, total in weights.items()]
  rankings.sort()
  rankings.reverse()
  return rankings