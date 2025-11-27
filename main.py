file= open('doc.txt' ,'r')
print(file.read())
file.close()

file = open('doc.txt', 'r')
print("\n read in parts \n")
print(file.read(8))
file.close()

file = open('doc.txt', 'a')

file.write("hi i am a penguin and iam 1year old")
file.close()