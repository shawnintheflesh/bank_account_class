panagram = """The quick brown
 fox jumps  over 
 the lazy dog"""

words = panagram.split()
print(words)

numbers = "9, 45, 63, 30, 703"


numbs = numbers.split()
print(numbs)

for index in range(len(numbs)):
    numbs[index] = int(numbs[index])

