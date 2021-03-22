import time
from selenium.common.exceptions import NoSuchElementException


def send_easy_application(driver, phone, all_listings):
    for job in all_listings:
        print("called")
        job.click()
        time.sleep(2)
        # Try to locate the apply button, if can't locate then skip the job.

        try:
            apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
            apply_button.click()
            time.sleep(5)

            # If phone field is empty, then fill your phone number.
            phone_field = driver.find_element_by_class_name("fb-single-line-text__input")
            if phone_field.text == "":
                phone_field.send_keys(phone)

            submit_button = driver.find_element_by_css_selector("footer button")

            # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
            if submit_button.get_attribute("data-control-name") == "continue_unify":
                close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
                discard_button.click()
                print("Complex application, skipped.")
                continue
            else:
                submit_button.click()

            # Once application completed, close the pop-up window.
            time.sleep(2)
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

        # If already applied to job or job is no longer accepting applications, then skip.
        except NoSuchElementException:
            print("No application button, skipped.")
            continue

    time.sleep(5)
