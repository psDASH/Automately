def open_page(driver, url):
    driver.get(url)

def verify_title(driver, expected_title):
    assert driver.title == expected_title
