class StringUtility:
  def __init__(self, string):
    '''
    Initilize the object
	args: takes a string as a parameter and stores it as an instance variable..
	return: None
    '''
    self.string = string
    
  def __str__(self):
    '''
    Returns the internal string itself
	args: None
	return: the string value of the object
    '''
    return self.string
    
  def vowels(self):
    '''
    Checks if there are any vowels in the string
	args: None
	return: (str) a string that contains the number of vowels in the given string
    '''
    return str(len([i for i in self.string if i.lower() in {"a", "e", "i", "o", "u"}])) if len([i for i in self.string if i.lower() in {"a", "e", "i", "o", "u"}]) < 5 else "many"
    
  def bothEnds(self):
    '''
    Takes the frist and last two letter of a string and put them into a new string
	args: None
	return: (str) a new string that is the frist and last two letter of a given string
    '''
    return "" if len(self.string) <= 2 else self.string[0:2] + self.string[-2] + self.string[-1]
    
  def fixStart(self):
    '''
    Changes the letter that's the same as the first letter to a *
	args: None
	return: (str) a new string that got every letter that's the same as the first letter to *
    '''
    return self.string if len(self.string) <= 1 else self.string[0] + self.string.replace(self.string[0], "*")[1:]
    
  def asciiSum(self):
    '''
    Gives the sum of ascii numbers of a string
	args: None
	return: (int) a interger that is the sum of the ascii numbers
    '''
    return sum([ord(i) for i in self.string])
    
  def cipher(self):  
    '''
    Return an encoded string by incrementing all letters by the length of the string
	args: None
	return: (str) a new string that is shifted
    '''
    newString = ""
    for i in self.string:
      alphaBook = {("a", "A"): 0, ("b", "B"): 1, ("c", "C"): 2, ("d", "D"): 3, ("e", "E"): 4, ("f", "F"): 5, ("g", "G"): 6, ("h", "H"): 7, ("i", "I"): 8, ("j", "J"): 9, ("k", "K"): 10, ("l", "L"): 11, ("m", "M"): 12, ("n", "N"): 13, ("o", "O"): 14, ("p", "P"): 15, ("q", "Q"): 16, ("r", "R"): 17, ("s", "S"): 18, ("t", "T"): 19, ("u", "U"): 20, ("v", "V"): 21, ("w", "W"): 22, ("x", "X"): 23, ("y", "Y"): 24, ("z", "Z"): 25}
      key = list(alphaBook.keys())
      if i.isalpha():
        case = i.isupper()
        newNum = -1
        for h in range(len(key)): 
          if i in key[h]:
            newNum = (alphaBook[key[h]] + len(self.string)) % 26
        if case == True: #If upper case
          newString += key[newNum][1]
        else: 
          newString += key[newNum][0]
      else:
        newString += i
    return newString