text1 = '''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''


text2 = '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.'''


text3 = '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''


data = {
        "User" :  "Password",
        "bob" : "123",
        "ann" : "pas123",
        "mike" : "password123",
        "liz" : "pass123",
}


separate = "_" * 25

#Četnost délek slov v textu:

data_1 = [["LEN", "OCCURENCES", "NR."]]
data_2 = [["1", "*","1"],
          ["2", "*********", "9"],
          ["3", "******", "6"],
          ["4", "***********","11"],
          ["5", "***********","11"],
          ["6","***","3"],
          ["7", "*****","5"],
          ["8", "***","3"],
          ["9", "***","3"],
          ["10", "*","1"],
          ["11", "*","1"]]

#password + user
user = input("insert the name of user: ")
#podminky
for i in range(3):
    pwd = input("Enter the password: ")
    j=3
    if data.get(user) == pwd:
        print("Welcome to the app", str(user))
        print("We have 3 texts to be analyzed: ")
        print(separate)
        break

    else:
        print("The password is wrong, try again and chances left!!!",j-i)


slovnik_textu = dict(text1=dict(), text2=dict(), text3=dict())
list_slov = []
list_slov_1 = []
list_znaku = []
list_velke_pismena = []
b=[]
cislo = int(input("Enter a number btw. 1 and 3 to select: "))

for cislo in range(1):
  if cislo == 1:
      pocet_slov.append()
      print("There are" , len(text1.split()), "words in the selected text.")
print(separate)

for slovo in text1.split():
  if slovo.islower():
    list_slov.append(slovo.strip(".',:?!"))
print("There are",len(list_slov),"lowercase words.")

for slovo in text1.split():
  if slovo.istitle():
    list_slov_1.append(slovo.strip(".,?!"))
print("There are", len(list_slov_1),"titlecase words.")

for slovo in text1.split():
  if slovo.isupper():
    list_velke_pismena.append(slovo.strip(".,' '!:?'30N''"))
print("There are",len(list_velke_pismena),"uppercase words.")

for znak in text1.split():
  if znak.isdigit():
    list_znaku.append(znak)
print("There are",len(list_znaku),"numeric strings.")

for i in text1.split():
  if i.isnumeric():
    b.append(int(i))
print("The sum of all the numbers: ", sum(b))
print(separate)


#členení textu do tabulky:
for len, occurences, nr in data_1:
  print(f"{len:>5}|{occurences:^15}|{nr:<10}")
  print(separate)
for len, occurences, nr in data_2:
  print(f"{len:>5}|{occurences:<15}|{nr:<5}")