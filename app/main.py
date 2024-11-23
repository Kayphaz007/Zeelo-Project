from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.mouseActions import click
from selenium.webdriver.support.ui import Select
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


# click Manage your passes

elem_continue = driver.find_element(
    By.XPATH, "//div[@data-testid='my_rides__travel_pass[0]']"
)

click(driver, elem_continue)

# TODO select specific date
# click a date

try:
    # TODO apply wait.until to all elements found
    elem_continue = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, "iMeCJE"))
    )
    # elem_continue = wait.until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH, "//button[@id='hs-eu-confirmation-button']")
    #     )
    # )

    click(driver, elem_continue)

except Exception as error:
    print(f"Error: {error}")

# click outbound select times
try:
    accept_alert = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@data-testid='manage_travel_plans_modal__outbound__select_times_btn']",
            )
        )
    )
    # accept_alert = driver.find_element(
    #     By.XPATH, "//button[@id='hs-eu-confirmation-button']"
    # )

    click(driver, accept_alert)

except Exception as error:
    print(f"Error: {error}")

# select time
try:
    elem_continue = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@data-testid='manage_travel_plans_modal__outbound__time']//div//select",
            )
        )
    )

    selectElem = Select(elem_continue)
    selectElem.select_by_visible_text("08:35")

except Exception as error:
    print(f"Error: {error}")


# click inbound select times

try:
    accept_alert = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@data-testid='manage_travel_plans_modal__inbound__select_times_btn']",
            )
        )
    )
    # accept_alert = driver.find_element(
    #     By.XPATH, "//button[@id='hs-eu-confirmation-button']"
    # )

    click(driver, accept_alert)

except Exception as error:
    print(f"Error: {error}")

# select time
try:
    elem_continue = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//div[@data-testid='manage_travel_plans_modal__inbound__time']//div//select",
            )
        )
    )

    selectElem = Select(elem_continue)
    selectElem.select_by_visible_text("16:15")

except Exception as error:
    print(f"Error: {error}")

# click confirm booking
try:
    elem_continue = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//button[@data-testid='manage_travel_plans_modal__submit_btn']",
            )
        )
    )

    click(driver, elem_continue)

except Exception as error:
    print(f"Error: {error}")

# response will be sent.... "sorry, there are not enough seats available"

# repeat the above until successfull

# if successfull

# TODO Select all necessary days
# repeat booking page opens


# elem.clear()
print("hold")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
