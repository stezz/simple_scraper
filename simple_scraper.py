import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import string
BASE_URL = "https://www.tempusopen.fi"
FIRST_PAGE = "/index.php?r=result/index&Result%5Bresult_date%5D={year}&Result%5Bclass%5D={gender}&Result%5Bevent_code%5D={event_code}&Result%5Bpooltype%5D=1&Result%5Bcompetition_group%5D=&Result%5Bdate_first%5D={age_start}&Result%5Bdate_last%5D={age_end}&Result%5Bclub_group%5D=&Result%5Bswim_club%5D=&Result%5Bbesttimes%5D=1&ajax=result-grid&Result_sort=fina_p.desc"


year = "2022"
age_start = "14"
age_end = "14"
# 1: male, 2: female
gender = "1"
# 1000: all, 
event_code = "1000"
#year = request_input()
#print(type(year))
#print('you said year: %s' % year)
formatter = {'year': year,
            'age_start': age_start,
            'age_end': age_end,
            'gender': gender,
            'event_code': event_code
        }
FIRST_PAGE = FIRST_PAGE.format(**formatter)

#FIRST_PAGE = "/index.php?r=result/index&Result[result_date]=2022&Result[class]=1&Result[event_code]=1000&Result[pooltype]=1&Result[competition_group]=&Result[date_first]=14&Result[date_last]=14&Result[club_group]=&Result[swim_club]=&Result[besttimes]=1&ajax=result-grid"
# first page


def main():
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
        next_page = get_page_data(url, results_list)
        next_url = BASE_URL + next_page

    table = PrettyTable()

    keys = results_list[0].keys() 
    table.field_names = keys

    for res in results_list:
        table.add_row([res.get(key) for key in keys])

    print(table)

def request_input():
    year = input('What year are you interested in?')
    return year


def get_page_data(url, results_list):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    # get next page url
    next_url = soup.find("div", {"class":"pager"}).find("li", {"class":"next"}).a.get("href")

    # get table data
    table = soup.find('table')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
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
        results_list.append(result_data)
    return next_url



# start main app
main()