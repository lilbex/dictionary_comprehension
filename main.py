import string

#letter=string.ascii_letters
#print(letter)

def Letter_count():
  my_dict ={"a": 2, "e":5,
  "h":5,"b":4}
  #letters=my_dict.keys()
  letter_input = input("enter letter:")
  for key, value in my_dict.items():
    if letter_input == key:
      print (letter_input + " "+"appear " + str(value) + " times")
  
Letter_count()
