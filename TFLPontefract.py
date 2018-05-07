from selenium import webdriver
import pandas as pd 
import csv
from time import sleep
from datetime import datetime

df = pd.read_csv("/yourCSVpath.csv")
# print(df)
df1=df[['Date', 'Start Time', 'End Time']].dropna(axis=0)
# print(df1)
date = df1['Date'].tolist()
start = df1['Start Time'].tolist()
end = df1['End Time'].tolist()

browser=webdriver.Chrome()
browser.get("https://pontefract.io/login")
try:
    form = browser.find_element_by_tag_name("form")
    username = form.find_elements_by_tag_name("input")[0]
    password = form.find_elements_by_tag_name("input")[1]
    username.send_keys("yourusername")
    password.send_keys("yourpassword")
    submit = form.find_elements_by_tag_name("input")[-1]
    submit.click()
    for d, s, e in zip(date, start, end):
        browser.get("https://pontefract.io/")
        form = browser.find_elements_by_tag_name("form")[1]
        start_day_input = form.find_elements_by_tag_name("input")[0]
        start_time_input = form.find_elements_by_tag_name("input")[1]
        end_day_input = form.find_elements_by_tag_name("input")[2]
        end_time_input = form.find_elements_by_tag_name("input")[3]
#         breaks_input = form.find_elements_by_tag_name("input")[4]
        project_input = form.find_elements_by_tag_name("input")[5]
        project_input.send_keys("Underground Travel")
        start_time_input.send_keys(s)
        end_time_input.send_keys(e)
        browser.execute_script("arguments[0].value = '{}';".format(
        datetime.strptime(d, "%d-%b-%y").strftime("%Y-%m-%d")), start_day_input)
        browser.execute_script("arguments[0].value = '{}';".format(
        datetime.strptime(d, "%d-%b-%y").strftime("%Y-%m-%d")), end_day_input)
        sleep(0.5)
        submit = form.find_elements_by_tag_name("input")[-1]
        submit.click()
finally:
    browser.close()