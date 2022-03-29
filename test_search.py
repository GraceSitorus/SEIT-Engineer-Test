from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import time
@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    driver.get('https://skillacademy.com/')
    yield driver
    driver.quit()
def test_googling(driver):
    driver.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/div/div/div[2]/div/div[1]/div/input').send_keys('Software' + Keys.ENTER)
    time.sleep(5)
    
# def test_googling_dua(driver):
#     driver.find_element_by_name('q').send_keys('Reza Rahadian' + Keys.ENTER)
#     assert 'Reza Rahadian' in driver.find_element_by_css_selector('h3').text
#     assert 'Reza Rahadian' in driver.title

    # https://fachrul.id/memulai-automation-test-selenium-python-bagian-1/

    