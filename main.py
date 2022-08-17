import selenium

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pynput.keyboard import Controller


while True:

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://play.typeracer.com/")

    try:
        agree_button = driver.find_element('xpath', '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]')
        agree_button.click()
    except NoSuchElementException:
        pass

    while True:
        try:
            enter_race = driver.find_element('xpath', '//*[@id="gwt-uid-1"]/a')
            enter_race.click()
            break
        except NoSuchElementException:
            pass

    while True:
        try:
            driver.find_element('xpath', '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input')
            break
        except NoSuchElementException:
            pass


    while True:
        disabled_attribute = driver.find_element('xpath', '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input').get_attribute("disabled")
        if disabled_attribute == None:
            break

    elements = []
    i = 1

    while True:
        try:
            elements.append(driver.find_element('xpath', f'//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[{i}]').get_attribute("innerHTML"))
            i += 1
        except:
            break
    keyboard = Controller()

    text_to_write = ''
    for el in elements:
        text_to_write += el

    TYPE_PAUSE = 0.03

    for character in text_to_write:
        keyboard.press(character)
        keyboard.release(character)
        sleep(TYPE_PAUSE)
    
    sleep(1)
    driver.close()