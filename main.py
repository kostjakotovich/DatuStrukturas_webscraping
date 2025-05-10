import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import os
import time

addres = "https://www.visidarbi.lv"

all_vacances = []
website_filters = {}
personal_filters = {}

def build_url(speciality, location, keywords):
    base_url = "https://www.visidarbi.lv/darba-sludinajumi/"
    url = base_url
    if speciality:
        url += f"kas:{quote(speciality.strip())}/"
    if location:
        url += f"kur:{quote(location.strip())}/"
    url = url.rstrip('/')
    if keywords:
        url += f"?keywords={quote(keywords.strip())}"
    url += "#results"
    return url

def set_website_filters():
    print("")
    speciality = input("Ievadiet vēlamo specializāciju (piem. Programmētājs): \n")
    location = input("Norādiet pilsētu (piem. Riga, bez garumzīmēm un mīkstinājumiem):\n").lower()
    keywords = input("Atslēgvārdi (piem. sql html, atdaliet ar atstarpēm):\n").strip()
    if keywords:
        keywords = keywords.replace(" ", "+")
    else:
        keywords = ""
    print("")
    website_filters["speciality"] = speciality
    website_filters["location"] = location
    website_filters["keywords"] = keywords
    return website_filters

def set_personal_filters():
    experience_level = input("Ievadiet Jūsu pieredzes līmeni, piem: junior, mid, senior, full-stack, lead\n(ja nevēlaties norādīt, nospiediet 'ENTER' bez teksta): \n")
    print("")
    personal_filters["experience_level"] = experience_level
    return personal_filters

def find_vacancies():
    search_url = build_url(
        website_filters.get("speciality"),
        website_filters.get("location"),
        website_filters.get("keywords")
    )

    print(f"\n🔍 Searching: {search_url}\n")
    html_page = requests.get(search_url)

    if html_page.status_code == 200:
        page_content = BeautifulSoup(html_page.text, "html.parser")
        vacancies = page_content.find_all('div', class_ = ['item', 'item big-item'])

        for vacancy in vacancies:
            if 'premium' in vacancy.get('class', []):
                continue # ignoret reklamu
            # print(vacancies)

            if vacancy:
                company = vacancy.find('li', class_ = 'company')
                if company:
                    vacancy_title = vacancy.find('div', class_='title').find('a').text.strip()
                    experience = personal_filters.get("experience_level", "")
                    if not experience or experience.lower() in vacancy_title.lower():
                        company_name = company.text.strip()
                        vacancy_link = vacancy.find('a', class_='long-title')
                        if vacancy_link:
                            vacancy_full_link = vacancy_link['href']
                            if vacancy_full_link.startswith('/'):
                                vacancy_full_link = addres + vacancy_full_link

                            print(f"Company Name: {company_name}\nVacancy Title: {vacancy_title}")
                            print(f"Link to vacancy: {vacancy_full_link}\n")
                    
                else:
                    continue
            else:
                continue

if __name__ == "__main__":
    set_website_filters()
    set_personal_filters()
    while True:
        find_vacancies()
        menu_number = input("Menu (write the corresponding number of the command you want to execute):\n1) Change job parameters\n2) Refresh all vacancies\n3) Clear screen (clears everything until the last output)\n4) Exit \n")
        match menu_number:
            case "1":
                set_website_filters()
                set_personal_filters()
                find_vacancies()
            case "2":
                wait_time = 2
                print(f"Waiting {wait_time} seconds for vacancies refreshing...\n")
                time.sleep(wait_time)
            case "3":
                os.system('cls' if os.name == 'nt' else 'clear')
            case "4":
                break
            case _: 
                print("Unknown command, please type 1 or 2")
 
        