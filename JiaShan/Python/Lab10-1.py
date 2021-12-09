'''
Create a program that reads an HTML file and converts it to plain text.

Console
HTML Converter
Grocery List
* Eggs
* Milk
* Butter
Specifications

 Store the following data in a file named groceries.html:
<h1>Grocery List</h1>
<ul>
<li>Eggs</li>
<li>Milk</li>
<li>Butter</li>
</ul>
 When the program starts, it should read the contents of the file, remove the HTML
tags, remove any spaces to the left of the tags, add asterisks (*) before the list items,
and display the content and the HTML tags on the console as shown above.
'''

with open ("C:\\Users\\jiash\\Desktop\\DSI DATA\\2021_10_DSI_WD\\2021_10_DSI_WD\\JiaShan\\Python\\groceries.html") as file:
    grocerilist = file.readlines()
print('HTML Converter\n')
newlist = grocerilist.remove('<ul>')
newerlist = newlist.remove('</ul>')
nospace = newerlist.strip()
for i in enumerate(nospace):
    if i == 0:
        headnopre = nospace.removeprefix('<h1>')
        headnopresuf = headnopre.removesuffix('</h1>')
        print(f'{headnopresuf}')
    else:
        bodynopre = nospace.removeprefix('<li>')
        bodynopresuf = bodynopre.removesuffix('</li>')
        print(f'* {bodynopresuf}')