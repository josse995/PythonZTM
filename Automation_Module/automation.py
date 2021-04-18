from selenium import webdriver

edgeBrowser = webdriver.Edge('./msedgedriver.exe')
edgeBrowser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in edgeBrowser.title

# page_source is the whole html of the page
assert 'Show Message' in edgeBrowser.page_source

user_message = edgeBrowser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')

show_message_button = edgeBrowser.find_element_by_class_name('btn-default')
show_message_button.click()

output_message = edgeBrowser.find_element_by_id('display')
assert 'I AM EXTRA COOOOL' in output_message.text

edgeBrowser.close()
edgeBrowser.close()
