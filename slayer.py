from splinter import Browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service(ChromeDriverManager().install())
browser = Browser('chrome', service=service)
browser.visit('https://monkeytype.com')


#cookie agreement
cookie_button = browser.find_by_css('.acceptAll')
if cookie_button:
    cookie_button.first.click()
#Click to start
browser.find_by_tag('body').first.click()



actions = ActionChains(browser.driver)

while True:
    # Check if result page is visible (not just present)
    result_element = browser.find_by_id('result')
    if result_element and result_element.first.visible:
        print("Result page detected - stopping!")
        break
    
    active_word = browser.find_by_css('#words .word.active')
    word_text = active_word.first.text
    actions.send_keys(word_text + ' ').perform()
    time.sleep(0.05) #affects how fast the bot will type, anything below 0.5 will get an undetectable speed


print(f"Finished typing!")
input("Press Enter to exit...")


browser.quit()

