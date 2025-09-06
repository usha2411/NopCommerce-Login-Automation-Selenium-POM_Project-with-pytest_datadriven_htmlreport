This project automates the login functionality of the NopCommerce demo site using following tools and technologies:

Language: Python

Automation Library: Selenium WebDriver

Testing Framework: Pytest

Design Pattern: Page Object Model (POM)

Data Source: Excel (for Data Driven Testing using openpyxl)

Reports: HTML reports using pytest-html

Browser: Chrome (configurable)


NopCommerce_Login_Automation/
│── config/
│   └── config.ini                # Application URL & credentials
│── testData/
│   └── login_data.xlsx           # Test data for login (valid & invalid users)
│── pages/
│   └── base_page.py              # Common reusable methods
│   └── login_page.py             # Locators & actions for login page
│── tests/
│   └── test_login.py             # Test cases for login
│── reports/
│   └── allure-report/            # Test execution reports
│── utilities/
│   └── read_excel.py             # Utility for reading Excel test data
│── requirements.txt              # Required dependencies
│── pytest.ini                    # PyTest configurations
│── README.md                     # Project documentation
