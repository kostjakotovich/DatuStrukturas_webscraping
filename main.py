import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import os
import time

addres = "https://www.visidarbi.lv"

levels = {
    'junior': ['junior', 'jaunākais'],
    'middle': ['middle', 'vidējais'],
    'senior': ['senior', 'vecākais', 'eksperta līmeņa']
}

all_vacances = []
website_filters = {}
personal_filters = {}

seen_links = set()

def build_url(speciality, location, keywords,  page_number):
    base_url = "https://www.visidarbi.lv/darba-sludinajumi/"
    url = base_url
    if speciality:
        url += f"kas:{quote(speciality.strip())}/"
    if location:
        url += f"kur:{quote(location.strip())}"

    query_params = []
    if keywords:
        query_params.append(f"keywords={quote(keywords.strip())}")
    if page_number > 1:
        query_params.append(f"page={page_number}")

    if query_params:
        url += "?" + "&".join(query_params)

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
    experience_level = input(
        "Ievadiet Jūsu pieredzes līmeni, piem.: prakse, junior, mid, senior, full-stack, lead\n"
        "(⚠️ Meklēšana tiek veikta tikai pēc title, nevis apraksta, tāpēc ievadiet tikai tos vārdus, "
        "kas bieži parādās virsrakstos.)\n"
        "Ja nevēlaties norādīt, nospiediet 'ENTER' bez teksta: \n"
    )
    print("")
    personal_filters["experience_level"] = experience_level
    return personal_filters

def find_vacancies(page_number):
    search_url = build_url(
        website_filters.get("speciality"),
        website_filters.get("location"),
        website_filters.get("keywords"),
        page_number
    )

    html_page = requests.get(search_url)

    if html_page.status_code == 200:
        page_content = BeautifulSoup(html_page.text, "html.parser")
        print(f"\n🔍 {page_number}. Searching: {search_url}\n")
        vacancies = page_content.find_all('div', class_ = ['item', 'item big-item'])

        new_vacancy_found = False

        for vacancy in vacancies:

            if 'premium' in vacancy.get('class', []):
                continue # ignoret reklamu
            # print(vacancies)

            if vacancy:
                company = vacancy.find('li', class_ = 'company')

                title = vacancy.find('div', class_='title')
                if title:
                    h3 = title.find('h3')
                    vacancy_link = h3.find('a')

                if vacancy_link:
                    vacancy_full_link = vacancy_link['href']

                    if vacancy_full_link.startswith('/'):
                        vacancy_full_link = addres + vacancy_full_link
                
                if seen_links:
                    if vacancy_full_link in seen_links:
                        break
                                        
                seen_links.add(vacancy_full_link)

                if company:
                    vacancy_title = title.find('a').text.strip()
                    experience = personal_filters.get("experience_level", "").lower()
                    level_keywords = levels.get(experience, [experience]) if experience else []

                    if not level_keywords or any(keyword in vacancy_title.lower() for keyword in level_keywords):
                        company_name = company.text.strip()

                        salary_title = vacancy.find('li', class_='salary')
                        if salary_title:
                            salary = salary_title.text.strip() 
                        else: 
                            salary = "not mentioned"

                        print(f"Company Name: {company_name}\nVacancy Title: {vacancy_title}\nSalary: {salary} euro")
                        print(f"Link to vacancy: {vacancy_full_link}\n")

                        all_vacances.append({
                            'company': company_name,
                            'title': vacancy_title,
                            'salary': salary,
                            'link': vacancy_full_link
                        })


                new_vacancy_found = True


        return new_vacancy_found

if __name__ == "__main__":
    set_website_filters()
    set_personal_filters()
    while True:
        menu_number = input("Menu (write the corresponding number of the command you want to execute):\n"
                            "1) Change job parameters\n"
                            "2) Find\n"
                            "3) Clear screen (clears everything until the last output)"
                            "\n4) Show saved vacancies\n"
                            "5) Exit \n")

        match menu_number:
            case "1":
                set_website_filters()
                set_personal_filters()
                all_vacances.clear()
                seen_links.clear()
                page_number = 1
                while True:
                    has_next_page = find_vacancies(page_number)
                    if has_next_page:
                        page_number += 1
                    else:
                        break
            case "2":
                wait_time = 2
                all_vacances.clear()
                seen_links.clear()
                print(f"Waiting {wait_time} seconds for vacancies refreshing...\n")
                time.sleep(wait_time)
                page_number = 1
                while True:
                    has_next_page = find_vacancies(page_number)
                    if has_next_page:
                        page_number += 1
                    else:
                        break
            case "3":
                os.system('cls' if os.name == 'nt' else 'clear')
            case "4":
                if not all_vacances:
                    print("No saved vacancies.")
                else:
                    for vacancy in all_vacances:
                        print(f"Company: {vacancy['company']}\nTitle: {vacancy['title']}\nSalary: {vacancy['salary']}\nLink: {vacancy['link']}\n")
            case "5":
                break
            case "6":
                break
            case _: 
                print("Unknown command, please type 1 or 2")
