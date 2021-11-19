movies = [["Monty Python and the Holy Grail", 1975],
          ["Cat on a Hot Tin Roof", 1958],
          ["On the Waterfront", 1954]]

import csv

with open('C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python\\Movie List 2.0 program(Textbook Example)/movies.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(movies)