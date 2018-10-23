from selenium import webdriver
import getpass
import config
from config import *
import sys
import fileinput


def add_config(u, p):
    for line in fileinput.input("config.py", inplace=1):
        username_c = "user = ''"
        password_c = "psswd = ''"
        if username_c in line:
            line = line.replace(username_c, "user = '" + u + "'")
            sys.stdout.write(line)
        if password_c in line:
            line = line.replace(password_c, "psswd = '" + p + "'")
            sys.stdout.write(line)


if config.user == '':

    user = input("Enter your username: ")

    psswd = getpass.getpass("Enter your password: ")

    add_config(user, psswd)
    #config.username = user
    #config.password = psswd

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--profile-directory=Default")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://ublearns.buffalo.edu/")

login_b = driver.find_element_by_xpath("//a[@class='login']")

login_b.click()

username = driver.find_element_by_id("login")

username.send_keys(user)

password = driver.find_element_by_id("password")

password.send_keys(psswd)

submit = driver.find_element_by_id("login-button")

submit.click()
