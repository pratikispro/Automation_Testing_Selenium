from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class LoginTest(unittest.TestCase):
    def test_login_and_post_article(self):
        #initializes chrome driver
        driver = webdriver.Chrome()
        driver.maximize_window()

        # Open the website
        url = "https://atg.party"
        driver.get(url)

        # Check HTTP response code
        response_code = driver.execute_script("return window.performance.getEntries()[0].response.status")
        print("HTTP response code:", response_code)

        # Log response time of page load
        load_time = driver.execute_script("return window.performance.timing.loadEventEnd - window.performance.timing.navigationStart")
        print("Page load time:", load_time, "ms")

        # Click on Login
        login_link = driver.find_element(By.XPATH, '//button[@class="atg-secondarybtn-tiny outer-header__loginbtn loginbtn_new"]')
        login_link.click()

        # Login with email and password
        email = driver.find_element(By.ID, "email_landing")
        password = driver.find_element(By.ID, "password_landing")
        Signin_button  = driver.find_element(By.XPATH, '//button[@class="landing-signin-btn"]')

        email.send_keys("wiz_saurabh@rediffmail.com")
        password.send_keys("Pass@123")
        Signin_button.click()

        # Wait for login process to complete
        WebDriverWait(driver, 10).until(EC.url_contains("atg.party/dashboard"))

        # Go to the article page
        article_url = "https://atg.party/article"
        driver.get(article_url)

        # Fill in title, description, and upload cover image
        title_input = driver.find_element(By.ID, "title")
        description_input = driver.find_element(By.ID, "description")
        cover_image_input = driver.find_element(By.ID, "add-cover-image")
        post_button = driver.find_element(By.XPATH,"//button[@class='atg-primarybtn-tiny header__post-btn']")

        title_input.send_keys("Test Article")
        description_input.send_keys("This is a test article.")
        cover_image_input.send_keys("img path")
        post_button.click()

        # Wait for article to be posted and get the URL of the new page
        new_page_url = driver.current_url
        print("URL of the new page after posting the article:", new_page_url)

        # Quit the driver
        driver.quit()

if __name__ == "__main__":
    unittest.main()
