class Metrics():
   def euclidean_distance(self, X, Y):
       euclidean = 0
       mx = len(X) if len(X) >= len(Y) else len(Y) 
       for x in range(0, mx):
           if x < len(Y) and x < len(X):
               euclidean += (X[x] - Y[x])**2
       return euclidean**(1/2)

   def manhattan_distance(self, X, Y):
       manhattan = 0
       mx = len(X) if len(X) >= len(Y) else len(Y) 
       for x in range(0, mx):
           if x < len(Y) and x < len(X):
               manhattan += abs(X[x] - Y[x])
       return manhattan

   def cosine_similarity(self, X, Y):
       cosine = 0
       mx = len(X) if len(X) >= len(Y) else len(Y)
       sum = 0
       sqrt_term_a = 0
       sqrt_term_b = 0
       for x in range(0, mx):
           if x < len(Y):
               sqrt_term_b += Y[x]**2
           if x < len(X):
               sqrt_term_a += X[x]**2
           if x < len(Y) and x < len(X):
               sum += X[x] * Y[x]
       cosine = sum/((sqrt_term_a**(1/2))*(sqrt_term_b**(1/2)))
       return cosine
     
   def jaccard_similarity(self, X, Y):
       jaccard = 0
       plus = 0
       minus = 0
       union = 0
       find_X = [0] * 2000
       find_Y = [0] * 2000
       for x in range(0, len(X)):
           if X[x] < 0:
               find_X[X[x]*-1000] += 1
           else:
               find_X[X[x]] += 1
       for x in range(0, len(Y)):
           if Y[x] < 0:
               find_Y[Y[x]*-1000] += 1
           else:
               find_Y[Y[x]] += 1
       for x in range(0, len(find_X)):
           if find_X[x] >= 1 and find_Y[x] >= 1:
               plus += find_X[x]
               union += 1
       jaccard = union/(len(X)+len(Y)-plus)
       return jaccard if union > 1 else union
     
def distances_and_similarities(X, Y):
   metrics = Metrics()
   return [metrics.euclidean_distance(X, Y),
           metrics.manhattan_distance(X, Y),
           metrics.cosine_similarity(X, Y),
           metrics.jaccard_similarity(X, Y)]
