'''
outfile = open("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python/text.txt", "w")
outfile.write("Test")
outfile.close()

with open ("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python/members.txt", "a") as file:
    file.write('Eric Idle\n')

with open ("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python/members.txt") as file:
    for line in file:
        print(line, end='')
        print()


with open ("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python/members.txt") as file:
    contents = file.read()
    print(contents)
    
with open ("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python/members.txt") as file:
    members = file.readlines
    print(members()[0], end="")
    print(members()[1]) #   print(members()[1]) IndexError: list index out of range#


with open ("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python/members.txt") as file:
    member1 = file.readline()
    print(member1, end="")
    member2 = file.readline()
    print(member2)
    
members = ["John Cleese", "Eric Idle"]
with open("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python/memberstest.txt", "w") as file:
    for m in members:
        file.write(f'{m}\n')
        
members = []
with open("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python/memberstest.txt") as file:
    for line in file:
        line =line.replace('\n', '')
        members.append(line)
print(members)
'''
'''
years = [1975, 1979, 1983]
with open("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python/years.txt", "w") as file:
    for year in years:
        file.write(f"{year}\n")
'''
'''
years = []
with open("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python/years.txt") as file:
    for line in file:
        line = line.replace('\n', '')
        years.append(int(line))
print(years)

'''
'''
movies = [["Monty Python and the Holy Grail", 1975],
          ["Cat on a Hot Tin Roof", 1958],
          ["On the Waterfront", 1954]]

import csv

with open('C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python/movies.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(movies)
'''
'''
import csv
with open('C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python/movies.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(f'{row[0]} ({row[1]})')
'''
# moved to tests folder, so all above code need to add \\tests to path
'''
'''
movies = [["Monty Python and the Holy Grail", 1975],
          ["Cat on a Hot Tin Roof", 1958],
          ["On the Waterfront", 1954]]

import pickle

with open("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python\\tests/movies.bin", "wb") as file:  # write binary
    pickle.dump(movies, file)

with open("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python\\tests/movies.bin", "rb") as file: # read binary
    movie_list = pickle.load(file)
    print(movie_list)