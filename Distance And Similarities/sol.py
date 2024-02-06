class Metrics():
   def euclidean_distance(self, X, Y):
       euclidean = 0
       for x in range(0, len(X) if len(X) >= len(Y) else len(Y)):
           if x < len(Y) and x < len(X):
               euclidean += (X[x] - Y[x])**2
       return euclidean**(1/2)

   def manhattan_distance(self, X, Y):
       manhattan = 0
       for x in range(0, len(X) if len(X) >= len(Y) else len(Y)):
           if x < len(Y) and x < len(X):
               manhattan += abs(X[x] - Y[x])
       return manhattan

   def cosine_similarity(self, X, Y):
       sum = sqrt_term_a = sqrt_term_b = 0
       for x in range(0, len(X) if len(X) >= len(Y) else len(Y)):
           if x < len(Y):
               sqrt_term_b += Y[x]**2
           if x < len(X):
               sqrt_term_a += X[x]**2
           if x < len(Y) and x < len(X):
               sum += X[x] * Y[x]
       cosine = sum/((sqrt_term_a**(1/2))*(sqrt_term_b**(1/2)))
       return cosine
     
   def jaccard_similarity(self, X, Y):
       union = count = 0
       hash = [0] * 2000
       find = [0] * 2000
       for x in range(0, len(X) if len(X) >= len(Y) else len(Y)):
           if x < len(X):
               if X[x] < 0:
                   if find[X[x]*-1000] < 2:
                       find[X[x]*-1000] += 1
                   if hash[X[x]*-1000] == 0:
                       hash[X[x]*-1000] += 1
                       count += 1
                   if find[X[x]*-1000] > 1:
                       union += 1
                       find[X[x]*-1000] = 0
               if X[x] >= 0:
                    if find[X[x]] < 2:
                        find[X[x]] += 1
                    if hash[X[x]] == 0:
                        hash[X[x]] += 1
                        count += 1
                    if find[X[x]] > 1:
                        union += 1
                        find[X[x]] = 0
           if x < len(Y):
                if Y[x] < 0:
                    if find[Y[x]*-1000] < 2:
                        find[Y[x]*-1000] += 1
                    if hash[Y[x]*-1000] == 0:
                        hash[Y[x]*-1000] += 1
                        count += 1
                    if find[Y[x]*-1000] > 1:
                        union += 1
                        find[Y[x]*-1000] = 0
                if Y[x] >= 0:
                    if find[Y[x]] < 2:
                        find[Y[x]] += 1
                    if hash[Y[x]] == 0:
                        hash[Y[x]] += 1
                        count += 1
                    if find[Y[x]] > 1:
                        union += 1
                        find[Y[x]] = 0
       jaccard = union/count
       return jaccard if count > 1 else count
      
def distances_and_similarities(X, Y):
   metrics = Metrics()
   return [metrics.euclidean_distance(X, Y),
           metrics.manhattan_distance(X, Y),
           metrics.cosine_similarity(X, Y),
           metrics.jaccard_similarity(X, Y)]
