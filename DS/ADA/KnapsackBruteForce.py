def knapSack(W, wt, val, n):
   
    # initial conditions
   if n == 0 or W == 0 :
      return 0
   # If weight is higher than capacity then it is not included
   if (wt[n-1] > W):
      return knapSack(W, wt, val, n-1)
  
   else:
      return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                 knapSack(W, wt, val, n-1))


# To test above function
val = [160, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print (knapSack(W, wt, val, n))