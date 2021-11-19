years = ['a wooden staff','a wizard hat','a cloak of invisibility','some elven bread','an unknown potion','a scroll of uncursing','a scroll of invisibility','a crossbow',"a wizard's cloak"]
with open("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python\\Lab7-2/wizard_all_items.txt", "w") as file:
    for year in years:
        file.write(f"{year}\n")