import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import string
import inquirer

gender_list = {'Male': '1', 'Female': '2'}
style_list = {
            'Kaikki': '1000',
            '25m Vapaauinti': '4',
            '50m Vapaauinti' : '11',
            '100m Vapaauinti' : '13',
            '200m Vapaauinti' : '15',
            '400m Vapaauinti' : '17',
            '800m Vapaauinti' : '19',
            '1500m Vapaauinti' : '21',
            '25m Rintauinti' : '5',
            '50m Rintauinti' : '31',
            '100m Rintauinti' : '33',
            '200m Rintauinti' : '35',
            '25m Selkäuinti' : '6',
            '50m Selkäuinti' : '41',
            '100m Selkäuinti' : '43',
            '200m Selkäuinti' : '45',
            '25m Perhosuinti' : '7',
            '50m Perhosuinti' : '51',
            '100m Perhosuinti' : '53',
            '200m Perhosuinti' : '55',
            '100m Sekauinti' : '61',
            '200m Sekauinti' : '63',
            '400m Sekauinti' : '65'
            }

BASE_URL = "https://www.tempusopen.fi"


def main():
    
    FIRST_PAGE = "/index.php?r=result/index&Result%5Bresult_date%5D={year}&Result%5Bclass%5D={gender}&Result%5Bevent_code%5D={event_code}&Result%5Bpooltype%5D=1&Result%5Bcompetition_group%5D=&Result%5Bdate_first%5D={age_start}&Result%5Bdate_last%5D={age_end}&Result%5Bclub_group%5D=&Result%5Bswim_club%5D=&Result%5Bbesttimes%5D=1&ajax=result-grid&Result_sort=fina_p.desc"


    year = "2022"
    age_start = "14"
    age_end = "14"
    # 1: male, 2: female
    gender = "1"
    # 1000: all, 
    event_code = "1000"
    gender, age_start, age_end, event_code, year = request_input()
    formatter = {'year': year,
                'age_start': age_start,
                'age_end': age_end,
                'gender': gender,
                'event_code': event_code
            }
    FIRST_PAGE = FIRST_PAGE.format(**formatter)
    results_list = []
    url = BASE_URL + FIRST_PAGE
    next_url = ""
    first_loop = True

    

    while next_url != url:
        if not first_loop:
            url = next_url
        else:
            first_loop = False
        print("Scraping: %s" % url)
        next_page = get_page_data(url, event_code, results_list)
        next_url = BASE_URL + next_page

    table = PrettyTable()

    keys = results_list[0].keys() 
    table.field_names = keys

    for res in results_list:
        table.add_row([res.get(key) for key in keys])

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
                             message = 'What style? ',
                             choices = style_list.keys())
    ]   
    answers = inquirer.prompt(questions)
    gender = gender_list[answers['gender']]
    style = style_list[answers['style']]
    year = answers['year']
    age_start = answers['age_start']
    age_end = answers['age_end']
    
    return gender.strip(), age_end.strip(), age_start.strip(), style.strip(), year.strip()
    


def get_page_data(url, event_code, results_list):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # get next page url
    pager = soup.find("div", {"class":"pager"})
    if pager:
        next_url = pager.find("li", {"class":"next"}).a.get("href")
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
            date = data[4]
            time = data[5]
            fina = data[6]
            style = data[7]
            result_data = {
                        'pos': pos.text,
                        'name': name.text, 
                        'born': born.text,
                        'date': date.text,
                        'time': time.text.strip(),
                        'fina': fina.text,
                        'style': style.text}
        else:
            data = row.find_all("td")
            pos = data[0]
            name = data[1]
            name.div.clear()
            born = data[2]
            date = data[5]
            time = data[6]
            fina = data[7]
            result_data = {
                        'pos': pos.text,
                        'name': name.text, 
                        'born': born.text,
                        'date': date.text,
                        'time': time.text.strip(),
                        'fina': fina.text,}
        results_list.append(result_data)
    return next_url



# start main app
main()