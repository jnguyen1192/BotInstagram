# This is a sample Python script.
@source https://instapy.org/
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
import random


def get_rand_number(min=5, max=10):
    return random.randint(min, max)

mail="johdu13@hotmail.fr"
mdp="...31ynnHojoj"
browser = webdriver.Chrome(ChromeDriverManager().install())

browser.implicitly_wait(get_rand_number())
browser.get('https://www.instagram.com/')
browser.implicitly_wait(get_rand_number())

bot = browser.find_element_by_xpath("//button[text()='Accepter']")
bot.click()
browser.implicitly_wait(get_rand_number())

# button connect
bot = browser.find_element_by_xpath("//span[text()='Se connecter avec Facebook']")
bot.click()
browser.implicitly_wait(get_rand_number())
# button connect
bot = browser.find_element_by_xpath("//button[@title='Tout accepter']")
bot.click()
browser.implicitly_wait(get_rand_number())
#input mail
bot = browser.find_element_by_xpath('//input[@id="email"]')
bot.send_keys(mail)
browser.implicitly_wait(get_rand_number())
#input pass
bot = browser.find_element_by_xpath("//input[@name='pass']")
bot.send_keys(mdp[::-1])
browser.implicitly_wait(get_rand_number())
# button connect
bot = browser.find_element_by_xpath("//button[@name='login']")
bot.click()
print("sleep before insta plus tard")
sleep(20)
# button activer
bot = browser.find_element_by_xpath("//button[text()='Plus tard']")
bot.click()
sleep(5)
# button activer
bot = browser.find_element_by_xpath("//buttont[text()='Activer']")
bot.click()
browser.implicitly_wait(get_rand_number())
sleep(40000)



browser.close()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
