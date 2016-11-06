#number of test cases
t = input()
fibArr = []

#loop through each line t to add fiboseries
for i in xrange(t):
  fibArr.append(input())
  currFib = 2
  lastFib = 1
  nextFib = 0
  fiboEvenSum = 0


  while(currFib <= fibArr[i]):
    #add even fibs
    if(currFib % 2 == 0):
      fiboEvenSum += currFib
    
    #create fibo sequence
    nextFib = currFib + lastFib
    lastFib = currFib
    currFib = nextFib

  print fiboEvenSum
