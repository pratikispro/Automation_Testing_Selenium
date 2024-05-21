# Selenium Test Script for ATG.Party

This repository contains a Python script using Selenium for automated testing of the ATG.Party website. The script performs a sequence of actions: logging in, navigating to the article page, and posting an article. It includes checks for HTTP response codes and page load times, making it useful for both functional and performance testing.

## Features

- **Automated Login**: Logs into the ATG.Party website using provided credentials.
- **Article Posting**: Automates the process of posting an article with a title, description, and cover image.
- **Performance Metrics**: Logs HTTP response codes and page load times for performance monitoring.
- **WebDriverWait**: Ensures synchronization by waiting for specific conditions to be met before proceeding with actions.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver
