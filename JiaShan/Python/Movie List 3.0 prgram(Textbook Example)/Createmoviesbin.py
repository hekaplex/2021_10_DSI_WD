movies = [["Monty Python and the Holy Grail", 1975],
          ["Cat on a Hot Tin Roof", 1958],
          ["On the Waterfront", 1954]]

import pickle

with open("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python\\Movie List 3.0 prgram(Textbook Example)/movies.bin", "wb") as file:  # write binary
    pickle.dump(movies, file)