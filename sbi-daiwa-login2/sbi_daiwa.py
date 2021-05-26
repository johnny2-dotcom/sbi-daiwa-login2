from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import eel

@ eel.expose
def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = 'https://www.sbisec.co.jp/ETGate'
    driver.get(url)
    sleep(3)

    link_url_toushin = driver.find_element_by_css_selector('#navi01P > ul > li:nth-child(5) > a').get_attribute('href')

    link_url_fx = driver.find_element_by_css_selector('#navi01P > ul > li:nth-child(7) > a').get_attribute('href')

    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[1])

    driver.get(link_url_toushin)

    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[2])

    driver.get(link_url_fx)

    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[3])

    URL = 'https://www.daiwa.jp/'
    driver.get(URL)
    sleep(3)

    link_url_toushin2 = driver.find_element_by_xpath('//a[text()="投資信託"]').get_attribute('href')

    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[4])

    driver.get(link_url_toushin2)

    driver.switch_to.window(driver.window_handles[0])


eel.init("html")
eel.start("index.html")

