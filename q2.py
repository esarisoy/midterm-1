echo "Honour Code: I hereby certify that I have completed this exam on my own without any help from anyone else. I understand that the only sources of authorized information in this exam are (i) the course textbook, (ii) the material that is posted on Blackboard or on repl.it lecture notes for this class, and (iii) any study notes handwritten by myself. I agree to follow the rules specified in _Rules.md file and cite any unauthorized source in taking this exam. The effort in this exam thus belongs completely to me."

echo "Hüseyin Erhan Göktanır"

# input table
tl_vs_usd = [
(('March', 2001), 1),
(('August', 2013), 2),
(('August', 2015), 3),
(('April', 2018), 4),
(('July', 2018), 5),
(('August', 2018), 6),
(('April', 2020), 7),
(('October', 2020), 8),
(('October', 2021), 9),
(('November', 2021), 10),
(('November', 2021), 11),
(('November', 2021), 12)
]

# months in English ordered
indexed_months = {
	'January': 1,
	'Februray': 2,
	'March': 3,
	'April': 4,
	'May': 5,
	'June': 6,
	'July': 7,
	'August': 8,
	'September': 9,
	'October': 10,
	'November': 11,
	'December': 12	
}

##################################
### START OF YOUR CODE: Part 1 ###
##################################
def how_long(...):
  """
  takes two date tuples date1 and date2 as input 
  each in the following format: (month, year)
  where month is a string and year is an integer
  computes and returns the distance between them in months as an int
  """

##################################
### END OF YOUR CODE: Part 1 #####
##################################

if __name__ == "__main__":
  # test your solution to Part 1 here
  print(how_long(('April', 2018), ('July', 2018)))
  print(how_long(('August', 2018), ('April', 2020)))
  print(how_long(('April', 2020), ('August', 2018)))

  print("\n====================================\n")
  
  # implement and test your solution to Part 2 here
  ##################################
  ### START OF YOUR CODE: Part 2 ###
  ##################################


  ##################################
  ### END OF YOUR CODE: Part 2 #####
  ##################################


##################################
### START OF YOUR ANSWER: Bonus ##
##################################
#
#
#
#
##################################
### END OF YOUR ANSWER: Bonus ####
##################################