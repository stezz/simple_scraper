import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import inquirer
import fontstyle

text1 = fontstyle.apply("Made 23/10/2022 Stefano and Tommi",
                        'bold/Italic/red/GREEN_BG')

text2 = fontstyle.apply("If you get an error it means that there are NO data or you made an error",
                        'bold/Italic/red/GREEN_BG')

text3 = fontstyle.apply("Thank you",
                        'bold/Italic/red/GREEN_BG')

print(text1)
print(text2)
print(text3)

gender_list = {'Male': '1', 'Female': '2'}
style_list = {
            'Kaikki': '1000',
            '25m Vapaauinti': '4',
            '50m Vapaauinti': '11',
            '100m Vapaauinti': '13',
            '200m Vapaauinti': '15',
            '400m Vapaauinti': '17',
            '800m Vapaauinti': '19',
            '1500m Vapaauinti': '21',
            '25m Rintauinti': '5',
            '50m Rintauinti': '31',
            '100m Rintauinti': '33',
            '200m Rintauinti': '35',
            '25m Selkäuinti': '6',
            '50m Selkäuinti': '41',
            '100m Selkäuinti': '43',
            '200m Selkäuinti': '45',
            '25m Perhosuinti': '7',
            '50m Perhosuinti': '51',
            '100m Perhosuinti': '53',
            '200m Perhosuinti': '55',
            '100m Sekauinti': '61',
            '200m Sekauinti': '63',
            '400m Sekauinti': '65'
}

club_list = {
            "Kaikki": "",
            "Äänekosken Uimaseura": "1958",
            "Åbo Simklubb": "1987",
            "Aboa Watersports": "2081",
            "Ålands Simförening": "2070",
            "Alavuden Urheilijat": "1961",
            "Aquatics Hyvinkää": "2084",
            "Aurajoen Uinti Ry": "1997",
            "Borgå simmare - Porvoon uimarit": "1873",
            "Brahean Uimarit": "1925",
            "Cetus Espoo": "1906",
            "Club Natacion Ciudad Alta": "2075",
            "Club Natación Las Palmas": "2051",
            "Dolphins Swim Club": "2030",
            "Dynamo Swim Club": "2022",
            "Ekenäs Simsällskap": "1903",
            "Elite Uinti ry": "2090",
            "Espoon Kilpauinti": "2088",
            "Eura Swimming Team": "2019",
            "Euran Työväen Urheilijat": "1964",
            "Finland": "2083",
            "Forellit": "1874",
            "Friitalan Yritys": "1965",
            "Gamla Polare urheiluseura": "2039",
            "Gladius Kirkkonummi": "2040",
            "Glenalbyn Swimming Club": "2045",
            "Golden Horseshoe Aquatic Club": "2021",
            "H.O.T.": "1901",
            "Haapajärven Kiilat": "1939",
            "Hämeenlinnan Mastersuimarit": "1991",
            "Hämeenlinnan Uimaseura": "1966",
            "Haminan Uimaseura": "1908",
            "Harjavallan Uimaseura": "2073",
            "Haukiputaan Heitto": "2013",
            "Heinolan Isku": "1909",
            "Helsingborgs Simsällskap": "2041",
            "Helsingfors Simsällskap": "1875",
            "Helsingin Uimarit": "1877",
            "HTU Stadi": "1876",
            "Hydra Platypus": "2048",
            "Hyvinkään Uimaseura": "1878",
            "IF Åland": "1967",
            "Iisalmen Uimarit": "1910",
            "Ilmajoen Kisailijat": "1940",
            "Ilouimarit": "1911",
            "Imatran Uimarit": "1912",
            "Jakobstads Simmare - Pietarsaaren Uimarit": "1941",
            "Jämsänkosken Ilves": "1946",
            "Jämsänkosken Jyry": "1947",
            "Järvenpään Uintiklubi ry": "1880",
            "Joensuun Uimaseura ry": "1913",
            "Jyväskylän Aalto": "2089",
            "Jyväskylän Saukot": "1942",
            "Jyväskylän Taitouimarit Ja U": "1944",
            "Jyväskylän uimaseura": "2024",
            "Jyvässeudun taitouimarit ja ui": "2018",
            "JyväsSeudun Uinti": "2087",
            "Kaarinan Ura": "1968",
            "Kajaanin Kuhat": "1998",
            "Kajaanin Uimaseura": "1999",
            "Kalajoen Uimarit": "1963",
            "Kampuksen Plaani": "2065",
            "Kangasalan Urheilijat KU-68": "2036",
            "Kankaanpään Uimarit": "1969",
            "Kannuksen Ura": "1962",
            "Kauhajoen Karhu": "1959",
            "Kemijärven Kaiku": "2000",
            "Kemin Työväen Uimarit": "2001",
            "Kemin Uimaseura": "2002",
            "Kempeleen Pyrintö": "2012",
            "Keravan Uimarit": "1881",
            "Keuruun Toverit": "1948",
            "Kimito Sportförening": "2078",
            "Kirkkonummen Uimarit KirU": "1898",
            "Kirkkonummen Uimaseura": "1899",
            "Kiteen Kisa-Toverit": "1914",
            "Kiteen Urheilijat": "1938",
            "Kiuruveden Jänne": "1915",
            "Kokkolan Työväen Urheilijat": "1949",
            "Kokkolan Uimaseura - Gamlakarleby Simsällskap": "1950",
            "KOOVEE": "1970",
            "Kotkan Uimaseura": "1916",
            "Kouvolan Uimarit": "1918",
            "Kristiinan Urheilijat": "2037",
            "Kuhmon Kiva Uintiseura": "2003",
            "Kuopion Työväen Uimarit": "1919",
            "Kuopion Uimaseura": "1920",
            "Kurikan Ryhti": "2059",
            "Kuusamon Erä-Veikot": "2014",
            "Kuusijärven Jääkarhut ": "2031",
            "Laaksonlahden Viri ": "1907",
            "Lahden Kaleva ": "1921",
            "Lahden Uimaseura ": "1922",
            "Laitilan Jyske ": "1993",
            "Lambertseter SK ": "2028",
            "Lane 4 Swimming Triathlon Club ": "2079",
            "Lapin Vedenkävijät ": "2015",
            "Lapin Veikot": "2082",
            "Lappeenrannan Kisa-Toverit ": "1923",
            "Lappeenrannan Uimarit r.y. ": "1924",
            "Lapuan Virkiä": "1951",
            "Lohjan Uimarit ": "1882",
            "Loimaan Uimaseura ": "2055",
            "Lojo Delfiner-Lohjan Delfiinit ": "1883",
            "Loyola Blakefield Aquatics": "2034",
            "Mansen Molskis ": "2066",
            "Marjaniemen uimarit ": "2069",
            "Marjaniemen Uimarit ": "1884",
            "Mikkelin Uimaseura ": "1926",
            "Muhoksen Voitto ": "2005",
            "Napapiirin Uimaseura ": "2004",
            "Närpes Simmare ": "1996",
            "Nivalan Saukot ": "1960",
            "Nokian Pyry ": "1995",
            "Nummelan Kisaajat ": "1885",
            "Nurmijärven Kunto ": "1886",
            "Nurmijärven Uinti ": "2064",
            "Oakland Live Yers ": "2023",
            "Octopus Lohja ": "2032",
            "ORCA Helsinki ": "2043",
            "Orimattilan Jymy ": "1935",
            "Oulun Lohet ": "2006",
            "Oulun Uimarit 73 ": "2007",
            "Oulun Uinti 1906 ": "2008",
            "Outokummun Uimarit ": "1927",
            "Pargas Simmare-Paraisten Uimar ": "1971",
            "Pieksän Kuutit ": "1928",
            "Pihlavan Työväen Urheilijat ": "1972",
            "Pikku Delfiinit ": "2076",
            "Poli Waterpolo Team ": "1887",
            "Porin Pyrintö ": "1973",
            "Porin Uimaseura ": "1974",
            "Poseidon ": "1888",
            "Punkaharjun Urheilijat ": "1929",
            "Raahen Seudun Uimarit ": "2009",
            "Race Club Sveitsi ": "2085",
            "Raision Urheilijat ": "1975",
            "Rauman Uimaseura ": "1976",
            "Riihimäen Uimaseura ": "1889",
            "Riihimäen Vesi ja Liikunta Aquana ": "2017",
            "Rovaniemen Uimarit ": "2010",
            "Rovaniemen Uimaseura ": "2058",
            "S.C. Pingviinit ": "1978",
            "Saarijärven Uimaseura ": "1957",
            "Salon Uimarit ": "1977",
            "Savonlinnan Uimaseura ": "1930",
            "Schwimmclub Kreuzlingen ": "2056",
            "Seinäjoen Uimarit -58 ry ": "1952",
            "Seuraton ": "2038",
            "Simmis Grani ": "1890",
            "Simmis Hyvinge-Hyvinkää ": "1891",
            "Simmis United ": "1892",
            "Simmis Wanda ry ": "1900",
            "Someron Esa ": "1979",
            "Speedo Masters Finland ": "2054",
            "Stadin Delfiinit ": "2020",
            "SUH ": "2049",
            "Suomussalmen Rasti ": "1934",
            "SV Detmold 06/21 ": "2042",
            "Swim Club Raseborg ": "2033",
            "Swimming Club Nurmijärvi ": "2044",
            "Swimming Club Rovaniemi ": "2016",
            "Swimming Club Vuokatti ": "2026",
            "Swimming Jyväskylä ": "1943",
            "Swimming Team Rauma ": "2068",
            "Swimming Team Riksu ": "2027",
            "Tampereen NMKY:n Urheilijat ": "1980",
            "Tampereen seurayhtymä ": "2046",
            "Tampereen Uimaseura ": "1982",
            "Tapiolan Uimarit ": "2025",
            "TaTU Tampere ": "1981",
            "Tikkurilan Lohet ": "1893",
            "Tornion Uimaseura ": "2011",
            "Turun NMKY ": "1983",
            "Turun Työväen Uimarit ": "1984",
            "Turun Uimarit ": "1985",
            "Turun Uimaseura ": "1986",
            "Turun Uinti ": "1994",
            "Turun Urheiluliitto ": "2086",
            "Tuusulan Uimaseura ry ": "1904",
            "Uimahyppääjien Kerho Härveli ": "1879",
            "Uimahyppyseura Silakat ": "2067",
            "Uimahyppyseura Tiirat ": "1902",
            "Uimahyppyseura Vantaa Diving ": "2053",
            "Uimaseura Aquila ": "2063",
            "Uimaseura Helsinki ": "2062",
            "Uimaseura Kaarina ": "2029",
            "Uimaseura Kangasalan Kuohu ": "2035",
            "Uimaseura KoVe-Ve ": "1917",
            "Uinti Espoo-Esbo Sim ": "1905",
            "Uinti Hyvinkää ": "2074",
            "Uinti Imatra ": "2060",
            "Uinti Tampere ": "2052",
            "Uinti-Vakka ": "1988",
            "Uintiklubi Nereus ": "2050",
            "Uintiseura Härmän Hylkeet ": "2071",
            "Uintiseura Kuhat ": "1894",
            "UPOT ": "2047",
            "Vaajakosken Uimaseura ": "1953",
            "Vaasan Uimarit -96 ": "1954",
            "Vaasan Uimaseura - Vasa Simsällskap ": "1955",
            "Valkeakosken Uimaseura ": "1989",
            "Valkealan Kajo ": "1936",
            "Vanders ": "2061",
            "Vantaan Pyörre ": "2080",
            "Vantaan Uimarit ": "1895",
            "Vantaan Vesikot ": "1896",
            "Varkauden Uimarit ": "1931",
            "Vesihelmen Uimaseura ": "1992",
            "Vesipalloseura Sentterit ": "1990",
            "Vesiveijarit ": "1932",
            "Vetehiset ": "1897",
            "Vieskan Uimarit ": "1956",
            "Voikkaan Viesti": "1933",
            "Vuoksen Uimaseura": "1937",
            "Wire": "2072",

}

ikmalue_list = {

                "Kaikki":"",
                "Etelä 1":"103",
                "Etelä 2":"116",
                "Häme/kaakkois":"104",
                "Keski/itä":"105",
                "Länsi":"107",
                "Muu":"117",
                "Pohjois":"108",
                "Varsinais":"106"
}

pool_type = {"25m":"1", "50m":"2"}

competition_group = {

                    "Kaikki":"",
                    "js-cup":"64",
                    "Masters kilpailut 2011":"12",
                    "Masters kilpailut 2012":"41",
                    "Masters kilpailut 2013":"40",
                    "Masters kilpailut 2014":"18",
                    "Masters kilpailut 2015":"39",
                    "Masters kilpailut 2016":"45",
                    "Masters kilpailut 2017":"49",
                    "Masters kilpailut 2018":"59",
                    "Suomen mestaruusuinnit":"11"

}



BASE_URL = "https://www.tempusopen.fi"


def main():
    FIRST_PAGE = "/index.php?r=result/index&Result%5Bresult_date%5D={year}&Result%5Bclass%5D={gender}&Result%5Bevent_code%5D={event_code}&Result%5Bpooltype%5D={pool}&Result%5Bcompetition_group%5D={competition}&Result%5Bdate_first%5D={age_start}&Result%5Bdate_last%5D={age_end}&Result%5Bclub_group%5D={ikmalue}&Result%5Bswim_club%5D={club}&Result%5Bbesttimes%5D=1&ajax=result-grid&Result_sort=fina_p.desc"

    gender, age_start, age_end, event_code, year, club, ikmalue, pool, competition = request_input()
    formatter = {'year': year,
                 'age_start': age_start,
                 'age_end': age_end,
                 'gender': gender,
                 'event_code': event_code,
                 'club': club,
                 'ikmalue': ikmalue,
                 'pool': pool,
                 'competition': competition

                 }
    FIRST_PAGE = FIRST_PAGE.format(**formatter)
    results_list = []
    url = BASE_URL + FIRST_PAGE
    next_url = ""
    first_loop = True

    while next_url != url:
        if not first_loop:
            url = next_url
            print('.', end='', flush=True)
        else:
            first_loop = False
            print("Scraping %s ." % BASE_URL, end='', flush=True)
        #print('%s' % url)
        next_page = get_page_data(url, event_code, year, results_list)
        next_url = BASE_URL + next_page

    table = PrettyTable()

    keys = results_list[0].keys()
    table.field_names = keys

    for res in results_list:
        table.add_row([res.get(key) for key in keys])

    print('\n')
    print(table)


def request_input():
    questions = [
        inquirer.Text('year',
                      message='What year are you interested in? [1900-2022]'),
        inquirer.Text('age_start',
                      message='What is the start age? [11-99]'),
        inquirer.Text('age_end',
                      message='What is the end age? [11-99]'),
        inquirer.List('gender',
                      message="What gender are you searching for? ",
                      choices=gender_list.keys()),
        inquirer.List('style',
                      message='What style? ',
                      choices=style_list.keys()),
        inquirer.List('club',
                      message='What swimming club? ',
                      choices=club_list.keys()),
        inquirer.List('ikmalue',
                      message='What ikm zone do you what? ',
                      choices=ikmalue_list.keys()),
        inquirer.List('pool',
                      message='What pool lenght do you want? ',
                      choices=pool_type.keys()),
        inquirer.List('competition',
                      message='What competition group do you what? ',
                      choices=competition_group.keys())

    ]
    answers = inquirer.prompt(questions)
    gender = gender_list[answers['gender']]
    style = style_list[answers['style']]
    year = answers['year']
    age_start = answers['age_start']
    age_end = answers['age_end']
    club = club_list[answers['club']]
    ikmalue = ikmalue_list[answers['ikmalue']]
    pool = pool_type[answers['pool']]
    competition = competition_group[answers['competition']]

    return gender.strip(), age_start.strip(), age_end.strip(), style.strip(), year.strip(), club.strip(), ikmalue.strip(), pool.strip(), competition.strip()


def get_page_data(url, event_code, year, results_list):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # get next page url
    pager = soup.find("div", {"class": "pager"})
    if pager:
        next_url = pager.find("li", {"class": "next"}).a.get("href")
    else:
        next_url = url.replace(BASE_URL, '')

    # get table data
    table = soup.find('table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        if event_code == '1000':
            data = row.find_all("td")
            pos = data[0]
            name = data[1]
            name.div.clear()
            born = data[2]
            competitionplace = data[3]
            date = data[4]
            time = data[5]
            fina = data[6]
            style = data[7]
            pooltype = data[8]
            age = int(year) - int(born.text)
            result_data = {
                'pos': pos.text,
                'name': name.text,
                'born': born.text,
                'competition in finland': competitionplace.text,
                'age': age,
                'date': date.text,
                'time': time.text.strip(),
                'fina': fina.text,
                'style': style.text,
                "pool": pooltype.text
                }
        else:
            data = row.find_all("td")
            pos = data[0]
            name = data[1]
            name.div.clear()
            born = data[2]
            competitionplace = data[4]
            date = data[5]
            time = data[6]
            fina = data[7]
            pooltype = data[8]
            age = int(year) - int(born.text)
            result_data = {
                'pos': pos.text,
                'name': name.text,
                'born': born.text,
                'competition in finland': competitionplace.text,
                'age': age,
                'date': date.text,
                'time': time.text.strip(),
                'fina': fina.text,
                "pool": pooltype.text
                }
        results_list.append(result_data)
    return next_url


# start main app
main()
