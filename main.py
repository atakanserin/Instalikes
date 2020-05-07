from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class InstaLiker:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.like_button_set  = set()
        self.driver = webdriver.Chrome()

    def open_instagram(self):
        self.driver.get("https://instagram.com")
        sleep(2)

    def enter_login_credentials(self):
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.username)
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.password)
        sleep(2)

    def press_login(self):
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        sleep(5)

    def shut_down_notification_pop_up(self):
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        sleep(2)

    def like(self):
        while(True):
            buttons = self.driver.find_elements_by_xpath(" //button[normalize-space(@class)='wpO6b']/*[name()='svg']")
            sleep(3)
            for button in buttons:
                if button.get_attribute('aria-label') == "Like" and button not in self.like_button_set:
                    sleep(3)
                    new_like_button = button
                    actions = ActionChains(self.driver)
                    actions.move_to_element(new_like_button).perform()
                    sleep(3)
                    new_like_button.click()
                    self.like_button_set.add(new_like_button)

    def run(self):
        self.open_instagram()
        self.enter_login_credentials()
        self.press_login()
        self.shut_down_notification_pop_up()
        self.like()

instaliker = InstaLiker("user name here", "password here")
instaliker.run()
