from selenium.webdriver.support.wait import WebDriverWait
from utils.mouseActions import click
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC


def enterPasswordTwice(driver, password):
    wait = WebDriverWait(driver, 10)
    # find password input
    elem = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@data-testid='login-password']")
        )
    )
    # elem = wait.untildriver.find_element(
    #     By.XPATH, "//input[@data-testid='login-password']"
    # )
    elem.send_keys(password)

    driver.implicitly_wait(3)

    # clsick continue
    elem_continue = driver.find_element(
        By.XPATH, "//button[@data-testid='login-confirm-button']"
    )

    click(driver, elem_continue)

    # find password input
    elem = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@data-testid='login-password']")
        )
    )
    # elem = wait.untildriver.find_element(
    #     By.XPATH, "//input[@data-testid='login-password']"
    # )
    elem.send_keys(password)

    driver.implicitly_wait(3)
    # click continue
    elem_continue = driver.find_element(
        By.XPATH, "//button[@data-testid='login-confirm-button']"
    )

    click(driver, elem_continue)
    
    # find password input
    elem = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@data-testid='login-password']")
        )
    )
    # elem = wait.untildriver.find_element(
    #     By.XPATH, "//input[@data-testid='login-password']"
    # )
    elem.send_keys(password)

    driver.implicitly_wait(3)
    # click continue
    elem_continue = driver.find_element(
        By.XPATH, "//button[@data-testid='login-confirm-button']"
    )

    click(driver, elem_continue)

