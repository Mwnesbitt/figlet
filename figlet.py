class Figure(object):
  def __init__(self):
    self.height = 0
    self.width = 0
    
  def line(self, lineNumber):  #abstract method in Java, implemented differently for Box, Letter, and Phrase.
    result = ""
    for x in range(0,length):
      pass
  
  def draw(self, fileName):
    fileObject = open(fileName, "a")
    for x in range(self.height):
      fileObject.write(self.line(x)+"\n") #there is definitely a better way to do this-- I want to overwrite any existing file and print line by line.  how to do that?
      print(self.line(x))
    fileObject.close()
    
class Box(Figure):
  def __init__(self, interior, exterior, height, width):
    self.interior = interior
    self.exterior = exterior
    self.height = height
    self.width = width
    
  def line(self, rowNumber):
    result = ""
    if(rowNumber == 0 or rowNumber == (self.height -1)):
      for x in range(0, self.width): 
        result+=self.exterior
    else:
      result+=self.exterior
      for x in range(1, self.width-1): 
        result+=self.interior
      result+=self.exterior
    return result

class Space(Box):
  def __init__(self, char, width):
    super().__init__(char, char, 11, width)

class Phrase(Figure):
  
  def __init__(self, userPhrase, spaceChar, spaceSize):
    self.height=11
    self.phrase = []
    for x in range(2*len(userPhrase)-1):
      if(x%2==0): 
        try:
          self.letterIndex = self.alphabetPosition(userPhrase[int(x/2)])
          self.tempLetter = getLetter(self.letterIndex, LETTER)
          self.phrase.append(self.tempLetter) 
        except Exception:
          self.letterIndex = 26
          self.tempLetter = getLetter(self.letterIndex, LETTER)
          self.phrase.append(self.tempLetter)
      else:
        self.phrase.append(Space(spaceChar, spaceSize))
    
  def alphabetPosition(self, char):
    return (ord(char) - 97)
    
  def line(self, lineNumber):
    result = ""
    for x in range(len(self.phrase)):
      result+=self.phrase[x].line(lineNumber) #relies on the line functions of Letter and Space classes
    return result
    
  def getWidth(self):
    result = 0
    for x in range(len(self.phrase)):
      result += self.phrase[x].width
      #print(result)
    return result
    
class Letter(Figure):
  def __init__(self, char, height, width, shape):
    self.char = char
    self.height = height
    self.width = width
    self.shape = shape

  def line(self, lineNumber): 
    return self.shape[self.width*(lineNumber):self.width*(lineNumber+1)]
"""
Had to pull some stuff out of the letter class.  I'm not pleased with that-- seems very ineligant and hacky. 
"""   
def getLetter(position, LETTER):
  return LETTER[position]
   
LETTER = [Letter('A',11,13,
"     ___     "+
"    /\\  \\    "+
"   /::\\  \\   "+
"  /:/\\:\\  \\  "+
" /:/ /::\\  \\ "+
"/:/_/:/\\:\\__\\"+
"\\:\\/:/  \\/__/"+
" \\::/__/     "+
"  \\:\\  \\     "+
"   \\:\\__\\    "+
"    \\/__/    "),
  Letter('B',11,13,
"             "+
"    _____    "+
"   /::\\  \\   "+
"  /:/\\:\\  \\  "+
" /:/ /::\\__\\ "+
"/:/_/:/\\:|__|"+
"\\:\\/:/ /:/  /"+
" \\::/_/:/  / "+
"  \\:\\/:/  /  "+
"   \\::/  /   "+
"    \\/__/    "),
  Letter('C',11,13,
"     ___     "+
"    /\\__\\    "+
"   /:/  /    "+
"  /:/  /     "+
" /:/  /  ___ "+
"/:/__/  /\\__\\"+
"\\:\\  \\ /:/  /"+
" \\:\\  /:/  / "+
"  \\:\\/:/  /  "+
"   \\::/  /   "+
"    \\/__/    "),
  Letter('D',11,13,
"             "+
"    _____    "+
"   /::\\  \\   "+
"  /:/\\:\\  \\  "+
" /:/  \\:\\__\\ "+
"/:/__/ \\:|__|"+
"\\:\\  \\ /:/  /"+
" \\:\\  /:/  / "+
"  \\:\\/:/  /  "+
"   \\::/  /   "+
"    \\/__/    "),
  Letter('E',11,13,
"     ___     "+
"    /\\__\\    "+
"   /:/ _/_   "+
"  /:/ /\\__\\  "+
" /:/ /:/ _/_ "+
"/:/_/:/ /\\__\\"+
"\\:\\/:/ /:/  /"+
" \\::/_/:/  / "+
"  \\:\\/:/  /  "+
"   \\::/  /   "+
"    \\/__/    "),
  Letter('F',11,13,
"     ___     "+
"    /\\__\\    "+
"   /:/ _/_   "+
"  /:/ /\\__\\  "+
" /:/ /:/  /  "+
"/:/_/:/  /   "+
"\\:\\/:/  /    "+
" \\::/__/     "+
"  \\:\\  \\     "+
"   \\:\\__\\    "+
"    \\/__/    "),
  Letter('F',11,13,
"     ___     "+
"    /\\__\\    "+
"   /:/ _/_   "+
"  /:/ /\\  \\  "+
" /:/ /::\\  \\ "+
"/:/__\\/\\:\\__\\"+
"\\:\\  \\ /:/  /"+
" \\:\\  /:/  / "+
"  \\:\\/:/  /  "+
"   \\::/  /   "+
"    \\/__/    "),
  Letter('G',11,13,
"     ___     "+
"    /\\  \\    "+
"    \\:\\  \\   "+
"     \\:\\  \\  "+
" ___ /::\\  \\ "+
"/\\  /:/\\:\\__\\"+
"\\:\\/:/  \\/__/"+
" \\::/__/     "+
"  \\:\\  \\     "+
"   \\:\\__\\    "+
"    \\/__/    "),
  Letter('I',11,11,
"           "+
"           "+
"   ___     "+
"  /\\__\\    "+
" /:/__/    "+
"/::\\  \\    "+
"\\/\\:\\  \\__ "+
"   \\:\\/\\__\\"+
"    \\::/  /"+
"    /:/  / "+
"    \\/__/  "),
  Letter('J',11,10,
"          "+			
"   ___    "+
"  /\\__\\   "+
" /:/__/   "+
"/::\\  \\   "+
"\\/\\:\\  \\  "+
"   \\:\\  \\ "+
"    \\:\\__\\"+
"    /:/  /"+
"   /:/  / "+
"   \\/__/  "),
  Letter('K',11,13,
"     ___     "+
"    /|  |    "+
"   |:|  |    "+
"   |:|  |    "+
" __|:|  |    "+
"/\\ |:|__|____"+
"\\:\\/:::::/__/"+
" \\::/~~/~    "+
"  \\:\\~~\\     "+
"   \\:\\__\\    "+
"    \\/__/    "),
  Letter('L',11,13,
"             "+
"             "+
"             "+
"             "+
" ___     ___ "+
"/\\  \\   /\\__\\"+
"\\:\\  \\ /:/  /"+
" \\:\\  /:/  / "+
"  \\:\\/:/  /  "+
"   \\::/  /   "+
"    \\/__/    "),
  Letter('M',11,13,
"     ___     "+
"    /\\  \\    "+
"   |::\\  \\   "+
"   |:|:\\  \\  "+
" __|:|\\:\\  \\ "+
"/::::|_\\:\\__\\"+
"\\:\\~~\\  \\/__/"+
" \\:\\  \\      "+
"  \\:\\  \\     "+
"   \\:\\__\\    "+
"    \\/__/    "),
  Letter('N',11,13,
"     ___     "+
"    /\\  \\    "+
"    \\:\\  \\   "+
"     \\:\\  \\  "+
" _____\\:\\  \\ "+
"/::::::::\\__\\"+
"\\:\\~~\\~~\\/__/"+
" \\:\\  \\      "+
"  \\:\\  \\     "+
"   \\:\\__\\    "+
"    \\/__/    "),
  Letter('O',11,13,
"     ___     "+
"    /\\  \\    "+
"   /::\\  \\   "+
"  /:/\\:\\  \\  "+
" /:/  \\:\\  \\ "+
"/:/__/ \\:\\__\\"+
"\\:\\  \\ /:/  /"+
" \\:\\  /:/  / "+
"  \\:\\/:/  /  "+
"   \\::/  /   "+
"    \\/__/    "),
  Letter('P',11,11,
"     ___   "+
"    /\\  \\  "+
"   /::\\  \\ "+
"  /:/\\:\\__\\"+
" /:/ /:/  /"+
"/:/_/:/  / "+
"\\:\\/:/  /  "+
" \\::/__/   "+
"  \\:\\  \\   "+
"   \\:\\__\\  "+
"    \\/__/  "),
  Letter('Q',11,13,
"             "+
"             "+
"     ___     "+
"    /\\  \\    "+
"   /::\\  \\   "+
"  /:/\\:\\  \\  "+
" /:/ /::\\  \\ "+
"/:/_/:/\\:\\__\\"+
"\\:\\/:/  \\/__/"+
" \\::/  /     "+
"  \\/__/      "),
  Letter('R',11,13,
"     ___     "+
"    /\\  \\    "+
"   /::\\  \\   "+
"  /:/\\:\\__\\  "+
" /:/ /:/  /  "+
"/:/_/:/__/___"+
"\\:\\/:::::/  /"+
" \\::/~~/~~~~ "+
"  \\:\\~~\\     "+
"   \\:\\__\\    "+
"    \\/__/    "),
  Letter('S',11,13,
"     ___     "+
"    /\\__\\    "+
"   /:/ _/_   "+
"  /:/ /\\  \\  "+
" /:/ /::\\  \\ "+
"/:/_/:/\\:\\__\\"+
"\\:\\/:/ /:/  /"+
" \\::/ /:/  / "+
"  \\/_/:/  /  "+
"    /:/  /   "+
"    \\/__/    "),
  Letter('T',11,13,
"             "+
"             "+
"     ___     "+
"    /\\__\\    "+
"   /:/  /    "+
"  /:/__/     "+
" /::\\  \\     "+
"/:/\\:\\  \\    "+
"\\/__\\:\\  \\   "+
"     \\:\\__\\  "+
"      \\/__/  "),
  Letter('U',11,13,
"     ___     "+
"    /\\  \\    "+
"    \\:\\  \\   "+
"     \\:\\  \\  "+
" ___  \\:\\  \\ "+
"/\\  \\  \\:\\__\\"+
"\\:\\  \\ /:/  /"+
" \\:\\  /:/  / "+
"  \\:\\/:/  /  "+
"   \\::/  /   "+
"    \\/__/    "),
  Letter('V',11,13,
"             "+
"     ___     "+
"    /\\  \\    "+
"    \\:\\  \\   "+
"     \\:\\  \\  "+
" ___  \\:\\__\\ "+
"/\\  \\ |:|  | "+
"\\:\\  \\|:|  | "+
" \\:\\__|:|__| "+
"  \\::::/__/  "+
"   ~~~~      "),
  Letter('W',11,13,
"     ___     "+
"    /\\  \\    "+
"   _\\:\\  \\   "+
"  /\\ \\:\\  \\  "+
" _\\:\\ \\:\\  \\ "+
"/\\ \\:\\ \\:\\__\\"+
"\\:\\ \\:\\/:/  /"+
" \\:\\ \\::/  / "+
"  \\:\\/:/  /  "+
"   \\::/  /   "+
"    \\/__/    "),
  Letter('W',11,14,
"     ___      "+
"    /|  |     "+
"   |:|  |     "+
"   |:|  |     "+
" __|:|__|     "+
"/::::\\__\\_____"+
"~~~~\\::::/___/"+
"    |:|~~|    "+
"    |:|  |    "+
"    |:|__|    "+
"    |/__/     "),
  Letter('Y',11,11,
"           "+
"           "+
"     ___   "+
"    /|  |  "+
"   |:|  |  "+
"   |:|  |  "+
" __|:|__|  "+
"/::::\\  \\  "+
"~~~~\\:\\  \\ "+
"     \\:\\__\\"+
"      \\/__/"),
  Letter('Z',11,13,
"     ___     "+
"    /\\__\\    "+
"   /::|  |   "+
"  /:/:|  |   "+
" /:/|:|  |__ "+
"/:/ |:| /\\__\\"+
"\\/__|:|/:/  /"+
"    |:/:/  / "+
"    |::/  /  "+
"    |:/  /   "+
"    |/__/    "),
  Letter(' ',11,13,
"             "+
"             "+
"             "+
"             "+
"             "+
"             "+
"             "+
"             "+
"             "+
"             "+
"             ")
]	
    
#Have dialog boxes prompt the user after double clicking on figlet.py.
fileName = input("Enter the output file name:\n")
phrase = input("Enter your phrase (lowercase):\n")
spaceSize = int(input("Enter how thick you want the spaces between letters to be:\n"))
spaceChar = input("Enter the char you want for the space:\n")
topBoxHeight = int(input("Enter the height of the top box:\n"))
bottomBoxHeight = int(input("Enter the height of the bottom box:\n"))
boxExterior = input("Enter the char for the box exterior:\n")
boxInterior = input("Enter the char for the box interior:\n")

myPhrase = Phrase(phrase, spaceChar, spaceSize)
phraseWidth = myPhrase.getWidth()
topBox = Box(boxInterior, boxExterior, topBoxHeight, phraseWidth)
bottomBox = Box(boxInterior, boxExterior, bottomBoxHeight, phraseWidth)

topBox.draw(fileName)
myPhrase.draw(fileName) 
bottomBox.draw(fileName)