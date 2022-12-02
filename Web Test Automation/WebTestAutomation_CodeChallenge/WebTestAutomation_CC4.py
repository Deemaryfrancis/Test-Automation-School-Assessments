# Navigate to https://www.bbc.com/ and
# print  out  the top 10 latest news from the home page

from selenium import webdriver
from selenium.webdriver.firefox.service import service, Service
from webdriver_manager.firefox import GeckoDriverManager

def main():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.get("https://www.bbc.com/")
    from time import sleep
    sleep(1000)
    driver.close()


main()