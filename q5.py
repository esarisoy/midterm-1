echo "Honour Code: I hereby certify that I have completed this exam on my own without any help from anyone else. I understand that the only sources of authorized information in this exam are (i) the course textbook, (ii) the material that is posted on Blackboard or on repl.it lecture notes for this class, and (iii) any study notes handwritten by myself. I agree to follow the rules specified in _Rules.md file and cite any unauthorized source in taking this exam. The effort in this exam thus belongs completely to me."

echo "Elif Sude Arısoy"

def print_operation(num1, num2, operation, ret=False):
  """
  num1: first input number as a string
  num2: second input number as a string
  operation: an arithmetic operation as a string
             one of +, -, *, or /
  
  applies the operation to num1 and num2 and
  returns the result as a String if ret is True, 
  prints it otherwise
  """
  ##################################
  ### START OF YOUR CODE: Part 1 ###
  ##################################
  
  a, b = float(num1), float(num2)
  res = 0
  if operation == "+":
    res = a + b
  elif operation == "-":
    res = a - b
  elif operation == "*":
    res = a * b
  elif operation == "/":
    res = a / b
  
    a, b = float(num1), float(num2)
  res = 0
  if operation == "+":
    res = a + b
  elif operation == "-":
    res = a - b
  elif operation == "*":
    res = a * b
  elif operation == "/":
    res = a / b
  
  if not a, b:
    try:
      a = int(a)
      b = int(b)
      except ZeroDivisionError:
        print("No number can divided by zero.")
        return print_operation()
      

  if ret:
    return str(res)
  else:
    print(str(int(a)) + " " + operation + " " + str(int(b)) + " = " + str(int(res))) 
  
  
  if ret:
    return str(res)
  else:
    print(str(int(a)) + " " + operation + " " + str(int(b)) + " = " + str(int(res))) 

  ##################################
  ### END OF YOUR CODE: Part 1 #####
  ##################################


##################################
### START OF YOUR CODE: Part 2 ###
##################################
def print_chain_operation_iterative(chain):
  """
  chain: a list representing a sequence of numbers and operations as a string
  [num, num, operation, num, operation, num, operation, ..., num, operation].
  iterates over the chain and applies operations to numbers, 
  computes the total and prints the expression with the total.
  using print_operation() function
  """
##################################
### END OF YOUR CODE: Part 2 #####
##################################
pass


##################################
### START OF YOUR CODE: Bonus ####
##################################
# Uncomment it for solving the Bonus
# def print_chain_operation_recursive(...):


##################################
### END OF YOUR CODE: Bonus ######
##################################    

if __name__ == "__main__":
  # test your solutions for each part here

  # Part 1
  print_operation("5", "2", "+")  # should print "5 + 2 = 7"
  print_operation("3", "4", "-")  # should print "3 - 4 = -1"
  print_operation("4", "2", "*")  # should print "4 * 2 = 8"
  print_operation("6", "3", "/")  # should print "6 / 3 = 2"
  print_operation("1a", "2", "+") # should throw "Cannot convert to a number."
  print_operation("1", "bc", "*") # should throw "Cannot convert to a number."
  print_operation("4", "0", "/")  # should throw "Cannot divide by zero."
  print_operation("4", "0", "%")  # should assert "Unknown operation."

  print("\n====================================\n")

  # Part 2
  print_chain_operation_iterative(["5","2","+","3","+","2","*"]) # should print "5 + 2 + 3 * 2 = 20.0"
  print_chain_operation_iterative(["5","2","/","3","*","2.5","+"]) # should print "5 / 2 * 3 + 2.5 = 10.0"
  print_chain_operation_iterative(["2","6","-","-1","*","4","*"]) # should print "2 - 6 * -1 * 4 = 16.0"
  print_chain_operation_iterative(["3","3","*","1","+","2","/","3","*","5","+"]) # should print "3 * 3 + 1 / 2 * 3 + 5 = 20.0"
  print_chain_operation_iterative(["7","-10","-","17","-","13","-","-1","*","-13","/"]) # should print "7 - -10 - 17 - 13 * -1 / -13 = -1.0"
  print_chain_operation_iterative(["-3","-10","-","3","+","10","*","4","/","3.5","*"]) # should print "-3 - -10 + 3 * 10 / 4 * 3.5 = 87.5"

  print("\n====================================\n")

  # Bonus
  # Uncomment for testing the Bonus
  # print_chain_operation_recursive(["5","2","+","3","+","2","*"]) # should print "5 + 2 + 3 * 2 = 20.0"
  # print_chain_operation_recursive(["5","2","/","3","*","2.5","+"]) # should print "5 / 2 * 3 + 2.5 = 10.0"
  # print_chain_operation_recursive(["2","6","-","-1","*","4","*"]) # should print "2 - 6 * -1 * 4 = 16.0"
  # print_chain_operation_recursive(["3","3","*","1","+","2","/","3","*","5","+"]) # should print "3 * 3 + 1 / 2 * 3 + 5 = 20.0"
  # print_chain_operation_recursive(["7","-10","-","17","-","13","-","-1","*","-13","/"]) # should print "7 - -10 - 17 - 13 * -1 / -13 = -1.0"
  # print_chain_operation_recursive(["-3","-10","-","3","+","10","*","4","/","3.5","*"]) # should print "-3 - -10 + 3 * 10 / 4 * 3.5 = 87.5"
