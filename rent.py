import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    wait = WebDriverWait(browser, 12)
    wait.until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    book_button = browser.find_element(By.CSS_SELECTOR, "#book")
    book_button.click()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)

    answer_field = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_field.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit_button.click()

    time.sleep(10)
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

finally:
    time.sleep(10)
    browser.quit()