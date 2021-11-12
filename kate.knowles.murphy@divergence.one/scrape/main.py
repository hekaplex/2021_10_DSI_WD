from bs4 import BeautifulSoup

def scrape_countries():
    with open ('./Nation_Rankings_by_Military_Strength_from_Military_Watch.html', 'r') as fp:
        soup = BeautifulSoup(fp, 'html.parser')

    tags = soup.find_all('li', class_='countryitem')
    print(tags)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scrape_countries()

