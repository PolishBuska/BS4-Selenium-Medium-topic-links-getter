import time

from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Topics:
    def __init__(self, driver: Chrome):
        self._driver = driver
        self._driver.implicitly_wait(1)
        self._driver.maximize_window()
        self._windows = self._driver.window_handles
        self._wait = WebDriverWait(self._driver, 10)

    def main_page(self, link):
        self._driver.get(link)

    def sign_in(self, email, password):
        sign_in_btn = self._driver.find_element(By.XPATH, "//a[contains(text(), 'Sign in')]")
        sign_in_btn.click()
        google_btn = self._wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a/div[contains(text(), 'Sign in with Google')]")
        ))
        google_btn.click()
        google_email_form = self._wait.until(EC.element_to_be_clickable(
            (By.ID, "identifierId")
        ))
        google_email_form.send_keys(email)
        email_next_btn = self._wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="identifierNext"]/div/button')
        ))
        email_next_btn.click()

        google_password_form = self._wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
        ))
        google_password_form.send_keys(password)
        password_next_btn = self._wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="passwordNext"]/div/button')
        ))
        password_next_btn.click()

    def get_topics(self, topic: str):
        form = self._driver.find_element(By.CSS_SELECTOR, value='input[data-testid="headerSearchInput"]')
        form.send_keys(topic)
        time.sleep(0.5)
        form.send_keys(Keys.ENTER)
        self._wait.until(EC.presence_of_element_located((By.TAG_NAME, 'a')))

    def get_current_article(self):
        self._wait.until(EC.presence_of_all_elements_located(
            (By.TAG_NAME, 'article')
        ))
        articles = self._driver.find_elements(By.TAG_NAME, 'article')

        # Initialize a list to store the hrefs
        article_hrefs = []

        # Iterate over each article to find 'a' tags and extract the hrefs
        for article in articles:
            a_tags = article.find_elements(By.TAG_NAME, 'a')
            for a_tag in a_tags:
                href = a_tag.get_attribute('href')
                if href:  # Ensure href is not None
                    article_hrefs.append(href)

        return article_hrefs

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._driver.quit()
