'''
A package filled with every logic gate you could need.
'''

def nand(a,b):
 '''
 To use the function write it where you need it to be and then write,"== True"
 '''
 if not a and not b:
  return True
 else:
  return False

def nor(a,b):
 '''
 To use the function write it where you need it to be and then write,"== True"
 '''
 if not a or not b:
  return True
 else:
  return False

#exclusive gates

def xnor(a,b):
 '''
 To use the function write it where you need it to be and then write,"== True"
 '''
 if a == False and b == False:
  return True
 if a == False and b == True:
  return False
 if a == True and b == False:
  return False
 if a == True and b ==True:
  return True

def xor(a,b):
 '''
 To use the function write it where you need it to be and then write,"== True"
 '''
 if a == False and b == False:
  return False
 if a == False and b == True:
  return True
 if a == True and b == False:
  return True
 if a == True and b == True:
  return False