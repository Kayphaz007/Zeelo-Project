from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.mouseActions import click
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.utilsFunctions import enterPasswordTwice

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

username = "kayphaz007@gmail.com"
password = "S0mt0l0v3."

zeeloUrl = "http://app.zeelo.co/my-zeelo"


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
# driver = webdriver.Chrome(options=options)
driver.get(zeeloUrl)
# alert = driver.switch_to.alert
# TODO write if condition i.e if there is a popup to accept cookies
try:
    accept_alert = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@id='hs-eu-confirmation-button']")
        )
    )
    # accept_alert = driver.find_element(
    #     By.XPATH, "//button[@id='hs-eu-confirmation-button']"
    # )

    click(driver, accept_alert)

except Exception as error:
    print(f"Error: {error}")


elem = driver.find_element(
    By.XPATH, "//button[@data-testid='sign_up_with_email_btn']"
)
click(driver, elem)

# enter email address
elem = driver.find_element(By.XPATH, "//input[@id='login-email']")
elem.send_keys(username)
# click continue
elem_continue = driver.find_element(
    By.XPATH, "//button[@data-testid='login-confirm-button']"
)

click(driver, elem_continue)

driver.implicitly_wait(3)
# enter password twice
enterPasswordTwice(driver, password)
# elem.clear()
print("hold")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
