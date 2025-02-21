from libraries.Common import open_page, verify_title

@when("I navigate to {url}")
def navigate_to_url(context, url):
    open_page(context.driver, url)

@then("the title should be {title}")
def check_title(context, title):
    verify_title(context.driver, title)
