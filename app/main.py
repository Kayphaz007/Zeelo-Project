from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utils.mouseActions import click
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from utils.utilsFunctions import enterPasswordTwice

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# TODO create a list or key of days and time
day_keys = {
    "Monday": "Mon",
    "Tuesday": "Tue",
    "Wednesday": "Wed",
    "Thursday": "Thu",
    "Friday": "Fri",
}

time_inbound_list = {
    0: "06:05"
}
username = "kayphaz007@gmail.com"
password = "Pa55w0rd!"
# day = "Thu"
day = day_keys["Friday"]
inbound = "06:05"
# inbound = "08:35"
outbound = "14:45"
# outbound = "16:15"

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



# used a for loop to loop through each date div element, and select the element with date of Thursday, and not the first element
# check if I can select element base on index using Xpath
def selectDate():  # click a date
    try:
        # TODO apply wait.until to all elements found
        # elem_continue = wait.until(
        #     EC.element_to_be_clickable((By.CLASS_NAME, "iMeCJE"))
        # )
        # elem_continue = wait.until(
        #     EC.element_to_be_clickable(
        #         (By.CSS_SELECTOR, "div.inuFBJ")
        #     )
        # )
        def filter_function(element):
            return (
                day
                in element.find_elements(By.CSS_SELECTOR, ".iMeCJE")[0].text
            )

        elem_continue = driver.find_elements(By.CSS_SELECTOR, ".inuFBJ")

        filtered_elem = list(filter(filter_function, elem_continue))
        if len(filtered_elem) > 1:
            elem_continue = filtered_elem[1]
        else:
            elem_continue = filtered_elem[0]

        elem_continue = elem_continue.find_elements(
            By.CSS_SELECTOR, ".iMeCJE"
        )[1]
        click(driver, elem_continue)

    except Exception as error:
        print(f"Error: {error}")


# click outbound select times
def click_outbound_select_times():
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
        selectElem.select_by_visible_text(inbound)

    except Exception as error:
        print(f"Error: {error}")


# click inbound select times


def click_inbound_select_times():
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
        selectElem.select_by_visible_text(outbound)

    except Exception as error:
        print(f"Error: {error}")


# click confirm booking
def click_first_confirm_booking():
    status = False
    try:
        elem_continue = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[@data-testid='manage_travel_plans_modal__submit_btn']",
                )
            )
        )
        status = elem_continue.is_enabled()
        if status:
            click(driver, elem_continue)

        return status

    except Exception as error:
        return status
        print(f"Error: {error}")


def click_close_button():
    try:
        # find close button
        close_button_element = driver.find_element(
            By.CSS_SELECTOR,
            "[data-testid='manage_travel_plans_modal__close_btn'] > i:first-of-type",
        )
        click(driver, close_button_element)
    except Exception as error:
        print(error)


# response will be sent.... "sorry, there are not enough seats available"

# repeat the above until successfull
# if successfull i.e if it has title Repeat booking (class name: jSyiu)
header_element = None
while header_element is None:

    selectDate()
    click_outbound_select_times()
    click_inbound_select_times()
    click_first_confirm_booking()
    print("I clicked first confirm bookings")
    try:
        header_element = driver.find_element(By.CSS_SELECTOR, ".jSyiu")
        if "Repeat" in header_element.text:
            break
    except Exception:
        header_element = None
        # print(error)

    click_close_button()
    print("I clicked the close button")


if "Repeat" in header_element.text:
    # select all elements with class hpNTpP, that is to select all checkbox
    check_box_elements = driver.find_elements(By.CSS_SELECTOR, ".hpNTpP")

    def filter_checkbox_function(element):
        try:
            return (
                "check_box_outline_blank"
                in element.find_element(By.CSS_SELECTOR, ".bxDTMN").text
            )
        except Exception:
            return False

    filtered_elements = list(
        filter(filter_checkbox_function, check_box_elements)
    )

    # for loop to tick all the checkbox
    if filtered_elements:
        for element in filtered_elements:
            clickable_element = element.find_element(
                By.CSS_SELECTOR, ".bxDTMN"
            )
            click(driver, clickable_element)
    else:
        # click skip
        skip_element = driver.find_element(By.CSS_SELECTOR, ".ffdbtA")
        click(driver, skip_element)
    # then click confirm bookings
    confirm_bookings_element = driver.find_element(
        By.XPATH,
        "//button[@data-testid='manage_travel_plans_modal__replicate__replicate_booking__submit_btn']",
    )

    click(driver, confirm_bookings_element)
    # if not successful
    # click the close button
    # restart booking again


# then filter elements with checkbox

# click all check box

# then select confirm bookings

# repeat booking page opens


# elem.clear()
driver.close()

# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
