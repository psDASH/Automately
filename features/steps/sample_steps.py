from selenium import webdriver

driver = None

@given("I open the browser")
def open_browser(context):
    global driver
    driver = webdriver.Chrome()

@when('I navigate to "{url}"')
def navigate_to_url(context, url):
    driver.get(url)

@then('the page title should be "{title}"')
def check_page_title(context, title):
    assert driver.title == title
    driver.quit()
