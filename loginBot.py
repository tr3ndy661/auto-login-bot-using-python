from selenium import webdriver
import os

def startBot(username, password, url):
    path = 'C:\Users\BOI\Downloads\chromedriver-win64\chromedriver-win64'
    driver = webdriver.Chrome(path)
    