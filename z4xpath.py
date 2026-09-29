from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(
        By.XPATH,
        "//label[contains(text(), 'First name')]/following-sibling::input"
    )
    name.send_keys("Ivan")

    last_name = browser.find_element(
        By.XPATH,
        "//label[contains(text(), 'Last name')]/following-sibling::input"
    )
    last_name.send_keys("Petrov")

    email = browser.find_element(
        By.XPATH,
        "//label[contains(text(), 'Email')]/following-sibling::input"
    )
    email.send_keys("ivan@example.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()