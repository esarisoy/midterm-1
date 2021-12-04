echo "Honour Code: I hereby certify that I have completed this exam on my own without any help from anyone else. I understand that the only sources of authorized information in this exam are (i) the course textbook, (ii) the material that is posted on Blackboard or on repl.it lecture notes for this class, and (iii) any study notes handwritten by myself. I agree to follow the rules specified in _Rules.md file and cite any unauthorized source in taking this exam. The effort in this exam thus belongs completely to me."

echo "Hüseyin Erhan Göktanır"

def print_s():
    s = "Inside"
    
    for i in range(0,3):
        print(s)
        
def increment_printer(start = 0):
  i = start

  def increment():
      for i in range(5):
          i += 1
          print(i)

  return increment

if __name__ == "__main__":
  s = "1"
  print_s()

  s = "2"
  print_s()

  print("=========")
  printer = increment_printer(0)
  for i in range(5):
    printer()
