from math import sqrt


#Calculates Pearson correlations
def pearson(preferences, personA, personB) :
  sum1 = 0; sum2 = 0; sum1sq = 0; sum2sq = 0; pSum = 0
  n = 0
  for ratingA in preferences[personA] :
    for ratingB in preferences[personB] :
      if(ratingA == ratingB) :
        sum1 += preferences[personA][ratingA]
        sum2 += preferences[personB][ratingB]
        sum1sq +=  preferences[personA][ratingA]**2
        sum2sq += preferences[personB][ratingB]**2
        pSum += preferences[personA][ratingA] * preferences[personB][ratingB]
        n += 1
  if n == 0:
    return 0
  num = pSum - (sum1 * sum2 / n)
  den = sqrt((sum1sq - sum1**2 / n) * (sum2sq - sum2**2 / n))
  return num / den