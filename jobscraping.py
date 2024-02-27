from bs4 import BeautifulSoup
import requests
import  time
import lxml

#Allows the user to input their own url.
url = input('Please copy and paste a http://www.jobs.ac.uk/search/... link to track: ')
#Allows user to select the frequency of refresh.
refresh_raw = input('Please input how many hours per refresh: ')
#converts input to integer and converts to seconds for later use.
rt = int(refresh_raw)
refresh = rt*60


def job_check():
    
    response = requests.get(url)
    if response.status_code == 200:
        jobshtml = response.text
    else:
        print('Error, Status Code ', response.status_code) #Checks if the response is valid to continue.

    soup = BeautifulSoup(jobshtml, 'lxml') #Use beautifulsoup on the htmltext

    jobs = soup.find_all('div', class_='j-search-result__text') #Scraping all the ads from the html using div and class
    
    deadline = soup.find_all('span', class_='j-search-result__date-span j-search-result__date--blue') #scrapes the closing date data.

    for ads in jobs:
        jobtitle = ads.find('a').text.strip() #Searches for a tags
            
        employers = ads.find('div', class_='j-search-result__employer').text.strip() #scrapes university name
            
        salary_raw = ads.find('div', class_='j-search-result__info').text.strip() #grabs text for salary
        salary = ' '.join(salary_raw.split()) #cleans salary text
    

        for dates in deadline:
            duedate = dates.text.strip()

        print(f'JOB TITLE: {jobtitle}\nInstitution: {employers}\n{salary}\nDeadline: {duedate}\n')

if __name__ == '__main__': #means when run from CMD, program runs every x hours.
    while True:
        job_check()
        print(f'Waiting {refresh_raw} hours')
        time.sleep(refresh)