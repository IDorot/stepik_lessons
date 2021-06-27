import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default=None, help="Choose your language: ru, en-GB, es, fr"
    )

@pytest.fixture(scope="function")
def browser(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    print(f"\nstart browser for test in {language} ..")
    yield browser
    print("\nquit browser...")
    browser.save_screenshot("1.png")
    browser.quit()




@pytest.fixture(scope="session")
def language(request):
    return  request.config.getoption("language")
