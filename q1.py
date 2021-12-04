run = run.q1.py
echo "Honour Code: I hereby certify that I have completed this exam on my own without any help from anyone else. I understand that the only sources of authorized information in this exam are (i) the course textbook, (ii) the material that is posted on Blackboard or on repl.it lecture notes for this class, and (iii) any study notes handwritten by myself. I agree to follow the rules specified in _Rules.md file and cite any unauthorized source in taking this exam. The effort in this exam thus belongs completely to me."

echo "Elif Sude Arısoy"

num_str = input("Type your Turkish Identification number")

#BONUS PART

if len(num_str) != 11:
    num_str = input("Type your Turkish Identification number")
else:
    break
for i in range(len(str(num_str))):
    if i not int:
        num_str = input("Type your Turkish Identification number")
    else:
        break

 
def check_tr_id_number(num_str):
  """
  num_str: an 11-digit ID as input
  returns True if num_str is a valid ID 
  and False otherwise
  according to the conditions defined in q1.md
  """
  sum_of_idnumbers = 0
    for figure in str(num_str):
      if figure == str(num_str)[-1]:
          continue
      else:
          sum_of_idnumbers += int(figure)
    return sum_of_idnumbers
  

if sum_of_idnumbers % 10 == str(num_str)[-1]:
    print("Your id is valid.")
else: 
    print("Your id is not valid. Please check your id.")


if __name__ == "__main__":
  # test your solution here
  
  # print('256: ', check_tr_id_number('256')) # should assert "invalid length"
  # print('2566sb40858: ', check_tr_id_number('2566sb40858')) # should throw "invalid digit" error
  print('25661140858: ', check_tr_id_number('25661140858')) # should print "25661140858:  True"
  print('27768850937: ', check_tr_id_number('27768850937')) # should print "27768850937:  False"
