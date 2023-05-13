# Data-Science-Salary-Predictions
 Data Science Salary Predictions ML app
 
 Link to the app: **[Web App](https://oussamahajoui-data-science-salary-predictions-app-srbjbb.streamlitapp.com/ "DS Salary Web App - Streamlit")**

## Goal & Context:
*  **TL,DR:** Build a web app to provide salary prediction for Data Science jobs within the US
*  **Full story:** This project aims to provide a salary prediction for data science jobs within the US using machine learning algorithms. The project involves web scraping job portals such as Glassdoor and Indeed for data science jobs data. The collected data is then cleaned, transformed, merged, and analyzed through exploratory data analysis to gain insights. The data is then used to train machine learning models that estimate salary data. The best performing model is exported as a pickle file and used in a web application created using Streamlit.


## Steps:
* Web scrapped Job portals (Glassdoor & Indeed) for Data science jobs data
* Load the data into our Jupyter notebook
* Clean, transform and merge the data
* Proceed to EDA on the data and collect insights
* Create machine learning models to estimate Salary data
* Run diagnostics on the ML model 
* Export the model as pickle file
* Leverage Streamlit to create the **[Web App](https://oussamahajoui-data-science-salary-predictions-app-srbjbb.streamlitapp.com/ "DS Salary Web App - Streamlit")**

Full steps in details within my **[Jupyther notebook](https://github.com/Oussamahajoui/Data-Science-Salary-Predictions/blob/main/Data%20Science%20Salary%20Predictor.ipynb "Data Science Salary Predictions Notebook")**

## End result:
I managed to build the following Web App :smile:	 :
[![image](https://user-images.githubusercontent.com/83676274/191068021-fb3d34c1-3d6f-438d-9b9e-2fe7b53044f7.png)](https://oussamahajoui-data-science-salary-predictions-app-srbjbb.streamlitapp.com/ "DS Salary Web App - Streamlit")

## Snippets of some of the main uncovered data points:
* **Different Data jobs collected within the sample:**
![image](https://user-images.githubusercontent.com/83676274/191071545-72a26e89-fb0e-4063-b84a-439711b05e70.png)

* **Minimum Salary data by function & data source:**
![image](https://user-images.githubusercontent.com/83676274/191069966-52b75106-efb3-4d19-baa4-aaf3ae1e4be7.png)

* **Pivot Table of the salary data per function & source:** *snippet only*
![image](https://user-images.githubusercontent.com/83676274/191070203-1be99cb0-f228-47d4-917c-dac71bab5cbe.png)

**Note:** *There is another pivot table within the notebook that has also further split of data by State/location*
* **Number of Jobs per locations in the US:**
![image](https://user-images.githubusercontent.com/83676274/191071048-7ba70acf-dffc-4374-bf37-fc17348bf013.png)

As usual most Tech jobs tends to be within California & New York. However, after the COVID-19 & the work-from-home wave, many employers are willing to offer Remote positions. Remote jobs ranked 2nd in total (*even ahead of NY*).

**Note:** *Many of the CA jobs, likely do offer remote options too. I focused on the primary location in this distribution.* 

## Improvements to be made:
* The ML model needs better tunning and to be able to provide better predictions
* Altough the total sample collect has about ~900 job postings data points, a much bigger sample could yield much more/better results
* Scrapping other job boards like levels.fyi, payscale, etc.
* *Maybe some better visuals within the web app?* 

Will be working on these improvements and updating everything *hopefully*

###### Made by Oussama Hajoui
