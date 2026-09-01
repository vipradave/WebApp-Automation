# Web Application Test Automation Suite

## 1. Project Overview
This project is an end-to-end (E2E) automated testing framework built for the [SauceDemo](https://www.saucedemo.com/) web application. It follows industry best practices to ensure stability, maintainability, and readability.

## 2. Features
- **Page Object Model (POM)**: Ensures test logic is separated from UI selectors.
- **Cross-Browser Testing**: Fully supports Chromium, Firefox, and WebKit.
- **Failure Artifacts**: Automatically captures screenshots and traces on test failure.
- **HTML Reporting**: Generates a rich, interactive HTML test report.
- **Test Data Management**: Separates static test data from test execution logic.
- **CI/CD Integration**: Automatically executes the regression suite using GitHub Actions on pushes and pull requests.

## 3. Tech Stack
- **Language**: Python 3.11+
- **Test Runner**: Pytest
- **Browser Automation**: Playwright (`pytest-playwright`)
- **Reporting**: `pytest-html`
- **CI/CD**: GitHub Actions

## 4. Project Structure
```
web-application-test-automation/
├── .github/
│   └── workflows/
│       └── tests.yml            # CI/CD configuration
├── pages/
│   ├── login_page.py            # POM for Login Page
│   ├── products_page.py         # POM for Products Page
│   ├── cart_page.py             # POM for Cart Page
│   └── checkout_page.py         # POM for Checkout Page
├── tests/
│   ├── test_basic.py            # Basic smoke tests
│   ├── test_login.py            # Login scenarios
│   ├── test_products_and_cart.py# Cart interactions
│   └── test_checkout.py         # End-to-end checkout flow
├── test_data/
│   └── test_data.py             # Reusable test variables
├── reports/                     # HTML reports and traces (ignored in Git)
├── screenshots/                 # Failure screenshots (ignored in Git)
├── .gitignore
├── pytest.ini                   # Pytest configuration
├── requirements.txt             # Python dependencies
└── README.md
```

## 5. Installation
1. Clone the repository.
2. Ensure you have Python installed.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install Playwright browsers:
   ```bash
   playwright install
   ```

## 6. Running Tests
To run the entire test suite using the default browser (Chromium):
```bash
pytest
```

## 7. Cross-Browser Testing
Run tests against specific browsers independently:
```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

To run against all three sequentially:
```bash
pytest --browser chromium --browser firefox --browser webkit
```

## 8. Test Reporting
Test executions automatically generate a comprehensive HTML report along with any failure screenshots and Playwright traces. 

After running the tests, open the generated report located at:
`reports/test_report.html`

## 9. CI/CD
This repository leverages GitHub Actions to enforce quality on every code change. When code is pushed or a pull request is created, the CI pipeline checks out the code, installs dependencies, and automatically executes the regression suite concurrently across **Chromium**, **Firefox**, and **WebKit**. 

If any test fails, the GitHub Actions workflow preserves debugging artifacts (the HTML report, screenshots, and Playwright traces) for download.

## 10. Test Scenarios
Current automated tests cover:
- Successful and invalid logins (including locked-out users and empty fields).
- Adding single and multiple products to the cart.
- Persistent cart state during navigation.
- Complete end-to-end checkout processing.
- Checkout form validation (missing required information).
