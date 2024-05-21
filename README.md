Selenium Test Script for ATG.Party
This repository contains a Python script using Selenium for automated testing of the ATG.Party website. The script performs a sequence of actions: logging in, navigating to the article page, and posting an article. It includes checks for HTTP response codes and page load times, making it useful for both functional and performance testing.

Features
Automated Login: Logs into the ATG.Party website using provided credentials.
Article Posting: Automates the process of posting an article with a title, description, and cover image.
Performance Metrics: Logs HTTP response codes and page load times for performance monitoring.
WebDriverWait: Ensures synchronization by waiting for specific conditions to be met before proceeding with actions.
Requirements
Python 3.x
Selenium
ChromeDriver
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/atg-party-selenium-test.git
cd atg-party-selenium-test
Install the Required Packages:

bash
Copy code
pip install selenium
Download and Install ChromeDriver:

ChromeDriver download
Ensure ChromeDriver is in your PATH or specify the path in the script.
Usage
Update Credentials:

Replace the placeholder email and password in the script with your own credentials.
python
Copy code
email.send_keys("your_email@example.com")
password.send_keys("your_password")
Update Cover Image Path:

Provide the correct path to your cover image.
python
Copy code
cover_image_input.send_keys("path/to/your/image.jpg")
Run the Script:

bash
Copy code
python test_login_and_post_article.py
Script Details
The script performs the following steps:

Initialize WebDriver:

Launches the Chrome browser and maximizes the window.
Open the ATG.Party Website:

Navigates to the homepage and logs the HTTP response code and page load time.
Log In:

Clicks on the login button and enters the email and password to log in.
Navigate to the Article Page:

Directs the browser to the article posting page.
Post an Article:

Fills in the article title, description, and uploads a cover image.
Submits the article and logs the URL of the newly posted article.
Close the Browser:

Quits the WebDriver session.
Contributing
Contributions are welcome! Please create an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or feedback, please contact your_name.

Feel free to customize the content according to your specific requirements or preferences. This template provides a comprehensive overview and usage guide for your Selenium test script repository.
