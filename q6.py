echo "Honour Code: I hereby certify that I have completed this exam on my own without any help from anyone else. I understand that the only sources of authorized information in this exam are (i) the course textbook, (ii) the material that is posted on Blackboard or on repl.it lecture notes for this class, and (iii) any study notes handwritten by myself. I agree to follow the rules specified in _Rules.md file and cite any unauthorized source in taking this exam. The effort in this exam thus belongs completely to me."

echo "Elif Sude Arısoy"

def print_halves(input_list):
  """ 
  takes a list input_list as input 
  and returns a new list output_list, the same size
  by halving the value of each element in the input_list
  input_list remains unchaged
  """
  output_list = input_list

  for i in range(len(input_list)):
    i // 2 = output_list[i]
  
  return output_list


def print_halves_2D(input_list_2):
  """ 
  takes a 2D list, i.e. list of lists, input_list as input 
  and returns a new 2D list output_list, the same size
  by halving the value of each element in each list in the input_list
  input_list remains unchaged
  """
  output_list_2 = input_list_2

  for i in range(len(input_list_2)):
    for j in range(len(input_list_2[i])):
      j // 2 = output_list_2[i][j] 
  
  return output_list_2


def remove_az(l):
  """ 
  takes a list l as input and mutates it
  by removing all occurences of character 'a' and 'z'
  no return, the input is modified directly
  """
  for i in range(len(l)):
    if "a" or "z" in l[i]:
      l.pop(i)


if __name__ == "__main__":
  # test your solutions for each part here

  # Part 1
  input_list = [2, 4, 6, 8, 10]
  output_list = print_halves(input_list)
  print("1) input_list:", input_list)
  print("1) output_list:", output_list)

  print("\n====================================\n")

  # Part 2
  input_list_2D = [[2, 4, 6, 8, 10], [20, 40, 60, 80, 100]]
  output_list_2D = print_halves_2D(input_list_2D)
  print("2) input_list:", input_list_2D)
  print("2) output_list:", output_list_2D)

  print("\n====================================\n")

  # Part 3
  input_list = ["f", "z", "b", "d", "z", "a"]
  print("3) The list before: ", input_list)
  remove_az(input_list)
  print("3) The list after: ", input_list)
