import requests
from bs4 import BeautifulSoup
import time

adress = "https://www.visidarbi.lv"

all_vacances = []
website_filters = {}
personal_filters = {}

def set_website_filters():
    print("")
    speciality = input("Ievadiet vēlamo specializāciju (ja nevēlaties norādīt, nospiediet 'ENTER' bez teksta): \n")
    print("")
    website_filters["speciality"] = speciality
    return website_filters

def set_personal_filters():
    experience_level = input("Ievadiet Jūsu pieredze līmeni (ja nevēlaties norādīt, nospiediet 'ENTER' bez teksta): \n")
    print("")
    personal_filters["experience_level"] = experience_level
    return personal_filters

def find_vacancies():
    html_page = requests.get(adress)

    if html_page.status_code == 200:
        page_content = BeautifulSoup(html_page.text, "html.parser")
        vacancies = page_content.find_all('div', class_ = ['item', 'item big-item'])

        for vacancy in vacancies:
            # print(vacancies)
            if vacancy:
                company = vacancy.find('li', class_ = 'company')
                if company:
                    vacancy_title = vacancy.find('div', class_='title').find('a').text.strip()
                    if personal_filters['experience_level'].lower() in vacancy_title.lower():
                        company_name = company.text.strip()
                        vacancy_link = vacancy.find('a', class_='long-title')['href']
                        if vacancy_link.startswith('/'):
                            vacancy_link = adress + vacancy_link
                        print(f"Company Name: {company_name}\nVacancy Title: {vacancy_title}")
                        print(f"Link to vacancy: {vacancy_link}\n")
                    
                else:
                    print("Comapny not found")
            else:
                print("Vacancy not found")

if __name__ == "__main__":
    set_website_filters()
    set_personal_filters()
    while True:
        find_vacancies()
        menu_number = input("Menu (write the corresponding number of the command you want to execute):\n1) Change job parameters\n2) Refresh all vacancies\n3) Exit \n")
        match menu_number:
            case "1":
                set_website_filters()
                find_vacancies()
            case "2":
                wait_time = 5
                print(f"Waiting {wait_time} seconds for vacancies refreshing...\n")
                time.sleep(wait_time)
                find_vacancies()
            case "3":
                break
            case _: 
                print("Unknown command, please type 1 or 2")
 
        