# Playwright Test Automation Framework for OrangeHRM

This repository contains an automated test suite for the **OrangeHRM** system using **Playwright** and **pytest**. The framework is structured to test core functionalities such as login and dashboard operations, ensuring the system behaves as expected.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Overview

This test automation framework validates essential features of the **OrangeHRM** system:
- **Login**: Tests valid and invalid login attempts.
- **Dashboard**: Ensures key dashboard elements are visible and interactive, and checks navigation functionality.

The framework leverages Playwright for browser automation and pytest for running and managing tests. The tests are designed to be easily extensible and maintainable, with a clear separation of concerns using the Page Object Model (POM).

## Project Structure
The directory structure is designed to organize the tests, page objects, utilities, and configurations clearly.

playwright-framework/
├── tests/
│   ├── login/
│   │   ├── test_valid_login.py       # Test for valid login attempts
│   │   ├── test_invalid_login.py     # Test for invalid login attempts
│   ├── dashboard/
│   │   ├── test_dashboard_visibility.py  # Test for dashboard visibility
│   │   ├── test_dashboard_navigation.py  # Test for dashboard navigation
├── pages/
│   ├── __init__.py
│   ├── base_page.py                  # Base page object with common actions
│   ├── login_page.py                 # Login page object with login-specific actions
│   ├── dashboard_page.py             # Dashboard page object with dashboard-specific actions
├── utils/
│   ├── __init__.py
│   ├── helpers.py                    # Helper functions used across tests
│   ├── constants.py                  # Constants such as selectors and URLs
├── conftest.py                       # pytest configuration and fixtures
├── pytest.ini                        # pytest configuration file
├── requirements.txt                  # List of required Python dependencies
└── README.md                         # Project documentation



## Prerequisites

Before running the tests, ensure you have the following installed:
- **Python 3.8+** (or higher).
- **pip** (Python's package installer).

Additionally, you'll need to install the **Playwright** browser binaries.

## Installation

Follow these steps to set up the testing framework:

### 1. Clone the repository

```bash
git clone https://github.com/marcusqatech/orangehrm-automation-framework.git
cd playwright-framework
