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

The framework uses **Playwright** for browser automation and **pytest** for running and managing tests.

## Project Structure

playwright-framework/
- ├── tests/
- │   ├── login/
- │   │   ├── test_valid_login.py
- │   │   ├── test_invalid_login.py
- │   ├── dashboard/
- │   │   ├── test_dashboard_visibility.py
- │   │   ├── test_dashboard_navigation.py
- ├── pages/
- │   ├── __init__.py
- │   ├── base_page.py
- │   ├── login_page.py
- │   ├── dashboard_page.py
- ├── utils/
- │   ├── __init__.py
- │   ├── helpers.py
- │   ├── constants.py
- ├── conftest.py
- ├── pytest.ini
- ├── requirements.txt
- └── README.md


## Prerequisites

Before running the tests, ensure you have the following installed:
- **Python 3.8+** (or higher).
- **pip** (Python's package installer).

Additionally, you'll need to install the **Playwright** browser binaries.

## Installation

Follow these steps to set up the testing framework:

### 1. Clone the repository

```bash
git clone https://github.com/marcusqatech/orangehrm-automation-framework
cd playwright-framework
