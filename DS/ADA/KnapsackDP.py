def knapSack(W, wt, val, n): 
    #K = [[0 for x in range(W + 1)] for x in range(n + 1)] 

    K=[]
    for x in range (n+1):
        L=[]
        for y in range(W+1):
            L.append(0)
        K.append(L)
    #print(K)
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            #print(w)
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
                          + K[i-1][w-wt[i-1]    ],   
                              K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
   
    return K[n][W] 
   
   
# Driver code 
val = [60, 100, 120] 
wt = [1, 2, 3] 
W = 6
n = len(val) 
print(knapSack(W, wt, val, n)) 
