
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from time import sleep
from random import randint
import pandas as pd

def get_jobs(keyword, num_jobs, verbose):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    # Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    # Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    # Change the path to where chromedriver is in your home folder.
    driver = webdriver.Chrome(executable_path="C:/Users/Oussama/Google Drive/DS & ML projects/Data_Science_Salary_Predictions/Glassdoor Scraping/chromedriver", options=options)
    driver.set_window_size(1120, 1000)

    #url = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword='+keyword+'&sc.keyword='+keyword+'&locT=&locID=&jobType='
    url = 'https://www.glassdoor.com/Job/data-science-jobs-SRCH_KO0,12.htm?clickSource=searchBox' 
    driver.get(url)
    
    # Define a global variable so even if error happens the progress can still be saved
    global jobs
    jobs = []

    # Let the page load. Change this number based on your internet speed.
    # Maybe add extra sleeping at the steps you need for more loading time. 
    sleep(randint(10,25))

    # Click on the first job & Test for the "Sign Up" prompt and get rid of it.
    driver.find_element_by_xpath("//*[@id='MainCol']/div[1]/ul/li[1]").click()

    sleep(randint(10,25))
    
    # Clicking on the Close X button to close the "Sign Up" prompt.
    driver.find_element_by_xpath('//*[@id="JAModal"]/div/div[2]/span').click()  
    
    sleep(randint(10,20))
    
    # Clicking on the "Search" button to search for the job postings based on keywords entered. 
    driver.find_element_by_xpath('//*[@id="scBar"]/div/button/span').click()
    sleep(randint(10,20))

    while len(jobs) < num_jobs:
        
        # Going through each job in this page
        job_buttons = driver.find_elements_by_xpath("//*[@id='MainCol']/div[1]/ul/li")
        
        for job_button in job_buttons:  
            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                # When the number of jobs collected has reached the number we set. 
                break
            job_button.click()  
            sleep(randint(7,20))
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    sleep(randint(7,20))
                    company_name = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]').text
                    location = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                    job_title = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
                    job_description = driver.find_element_by_xpath('//div[@class="jobDescriptionContent desc"]').text
                    collected_successfully = True
                except:
                    sleep(randint(10,20))
                    collected_successfully = True
            try:
                #salary_estimate = driver.find_element_by_xpath('//*[@id="MainCol"]/div[1]/ul/li[*]/div[2]/div[3]/div[1]/span').text
                salary_estimate = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span').text
            except NoSuchElementException:
                # You need to set a "not found value. It's important."
                salary_estimate = -1 
            
            try:
                rating = driver.find_element_by_xpath('//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/span').text
            except NoSuchElementException:
                # You need to set a "not found value. It's important."
                rating = -1 

            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Going to the Company tab...
            sleep(randint(10,20))

            """""
             try:
                driver.find_element_by_xpath('//div[@data-item="tab" and @data-tab-type="overview"]').click()
                sleep(randint(5,15))

                try:
                    size = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
                except NoSuchElementException:
                    size = -1

                try:
                    founded = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[2]/span[2]').text
                except NoSuchElementException:
                    founded = -1

                try:
                    type_of_ownership = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span[2]').text
                except NoSuchElementException:
                    type_of_ownership = -1

                try:
                    industry = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[2]').text
                except NoSuchElementException:
                    industry = -1

                try:
                    sector = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[2]').text
                except NoSuchElementException:
                    sector = -1

                try:
                    revenue = driver.find_element_by_xpath('//*[@id="EmpBasicInfo"]/div[1]/div/div[6]/span[2]').text
                except NoSuchElementException:
                    revenue = -1
            # Rarely, some job postings do not have the "Company" tab.
            except NoSuchElementException:  
                
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1
                             
            if verbose:
                
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
"""
            jobs.append({
            "Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            #"Size" : size,
            #"Founded" : founded,
            #"Type of ownership" : type_of_ownership,
            #"Industry" : industry,
            #"Sector" : sector,
            #"Revenue" : revenue
            })

        # Clicking on the "next page" button
        try:
            driver.find_element_by_xpath('//*[@id="FooterPageNav"]/div/ul/li[7]/a/span').click()
            sleep(randint(10,20))
            driver.refresh()
            sleep(randint(7,25))
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break
            
    #This line converts the dictionary object into a pandas DataFrame.
    return pd.DataFrame(jobs) 


data = get_jobs("Data science", 1000, False)
print(data.head())
data.to_csv('DataScience_Jobs_Glassdoor_Final.csv')


#data = pd.DataFrame(jobs)
#data.head()
#df = pd.read_csv('data.csv')
#df.head()