import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

load_dotenv()
time.sleep(5)


class Bot:

    url = os.environ.get("URL")
    sign_in_url = os.environ.get("SIGNINURL")
    driver = webdriver.Remote(
        "http://selenium:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME
    )

    def check_sign_in(self):
        welcome_message = Bot.driver.find_element_by_id(
            "nav-link-accountList-nav-line-1"
        )
        if "Sign in" not in welcome_message.get_attribute("innerHTML"):
            return True
        else:
            return False

    def sign_in(self):
        Bot.driver.get(Bot.sign_in_url)
        email_input = Bot.driver.find_element_by_id("ap_email")
        email_input.click()
        email_input.send_keys(os.environ.get("EMAIL"))
        continue_button = Bot.driver.find_element_by_id("continue")
        continue_button.click()
        password_input = Bot.driver.find_element_by_id("ap_password")
        password_input.send_keys(os.environ.get("PASSWORD"))
        sign_in_button = Bot.driver.find_element_by_id("signInSubmit")
        sign_in_button.click()
        try:
            self.check_sign_in()
        except:
            return False

    def buy_ps5(self):
        Bot.driver.get(Bot.url)
        while True:
            if self.check_sign_in():
                try:
                    buy_now_button = Bot.driver.find_element_by_id("buy-now-button")
                except:
                    Bot.driver.get(Bot.url)
                    continue
                if buy_now_button:
                    buy_now_button.click()
                    time.sleep(2)
                    Bot.driver.switch_to.frame("turbo-checkout-iframe")
                    place_order_button = Bot.driver.find_element_by_id(
                        "turbo-checkout-place-order-button"
                    )
                    if place_order_button:
                        place_order_button.click()
                        time.sleep(5)
                        try:
                            if (
                                "Order placed, thanks."
                                == Bot.driver.find_element_by_class_name(
                                    "a-alert-heading"
                                ).get_attribute("innerHTML")
                            ):
                                Bot.driver.save_screenshot("success.png")
                                Bot.driver.quit()
                                break
                            else:
                                Bot.driver.get(Bot.url)
                                continue
                        except:
                            Bot.driver.get(Bot.url)
                            continue
            else:
                self.sign_in()


if __name__ == "__main__":
    bot_instance = Bot()
    bot_instance.buy_ps5()
