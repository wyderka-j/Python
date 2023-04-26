#In Fibonacci sequence, a number is equal to the sum of its preceeding numbers

def Fibonacci(n):
  ### Starting numbers
  number1 = 0
  number2 = 1

  if(n == number1):
    print("The first term in Fibonacci is: ", number1)
  elif(n == number2):
    print("The second term in Fibonacci is: ", number2)
  else:
    for counter in range(n):
      print("Fibonacci(", counter, ") = ", number1)
      n = number1 + number2
      number1 = number2
      number2 = n

if __name__ == "__main__":
  ### Prompt user for input
  while True:
    try:
      n = int(input("Enter the length of the Fibonacci sequence: "))
      Fibonacci(n)
      break
    except:
      print("Invalid input. Please try again.")