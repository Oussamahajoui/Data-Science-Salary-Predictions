import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint


def extract(page):
    headers = {'UserAgent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
    url = f'https://www.indeed.com/jobs?q=Data%20Science&l=United%20States&start={page}'
    request = requests.get(url, headers)
    soup = BeautifulSoup(request.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_='job_seen_beacon')
    for a in divs:
        title = a.find(class_='jobTitle').text.strip()
        company = a.find('span', class_='companyName').text.strip()
        company_location = a.find('div', class_='companyLocation').text.strip()
        try:
            salary = a.find(class_ = 'metadata salary-snippet-container').text.strip()
        except:
            salary=''
        summary = a.find('div', class_='job-snippet').text.strip().replace('\n', '')

        jobs = {'title': title,
        'company': company,
        'location(s)': company_location,
        'salary': salary,
        'summary': summary
        }
        joblist.append(jobs)
    return


joblist = []
for i in range(0,600,10):
    print(f'Page {i}')
    sleep(randint(45,324))
    c = extract(i)
    transform(c)

df = pd.DataFrame(joblist)
print(df.head(10))

df.to_csv('DS_Jobs_indeed.csv')

