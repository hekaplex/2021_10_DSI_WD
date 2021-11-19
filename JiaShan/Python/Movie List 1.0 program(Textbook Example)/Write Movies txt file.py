members = ["Monty Python and the Holy Grail", "Cat on a Hot Tin Roof", "On the Waterfront"]
with open("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python\\Movie List 1.0 program/movies.txt", "w") as file:
    for m in members:
        file.write(f'{m}\n')