#Calculates Euclidean Distance for recommendation system

def euclidean_distance(preferences, personA, personB) :
  similarities = 0
  n = 0
  for ratingA in preferences[personA]:
    for ratingB in preferences[personB]:
      if(ratingA == ratingB):
        similarities += (preferences[personA][ratingA] - preferences[personB][ratingB]) **2
        n += 1
  if n == 0: return 0
  return 1 / (1 + similarities)  

