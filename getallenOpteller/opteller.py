number = -1

def sumNumbers(number):
  string = str(number)
  sum = 0
  for n in string:
    sum += int(n)
    
  
  if sum <=9:
    return sum
  else:
    return sumNumbers(sum)
  

result = sumNumbers(number)

print("The result is", result)