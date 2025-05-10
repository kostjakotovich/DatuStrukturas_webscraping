import requests
from bs4 import BeautifulSoup

adress = "https://www.visidarbi.lv"

html_page = requests.get(adress)

if html_page.status_code == 200:
    page_content = BeautifulSoup(html_page.text, "html.parser")
    vacancies = page_content.find('div', class_ = ['item', 'item big-item'])
    # print(vacancies)
    if vacancies:
        company = vacancies.find('li', class_ = 'company')
        if company:
            company_name = company.text.strip()
            print(company_name)
        else:
            print("Comapny not found")
    else:
        print("Vacancy not found")