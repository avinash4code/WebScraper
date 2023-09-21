from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


def findValueToEnter(element):
    # scan the element
    # pass to ML algo to get right value to type in
    # This is a dummy impl
    if (element.get_attribute('name') == 'username'):
        return 'Admin'
    elif (element.get_attribute('name') == 'password'):
        return 'admin123'
    else:
        return ''

print(driver.title)

_inputs = driver.find_elements(By.XPATH, '//input')

for input in _inputs:
    print(input.get_attribute('name'))
    if (input.is_displayed() and input.is_enabled()):
        valueToEnter = findValueToEnter(input)
        input.send_keys(valueToEnter)


        
        
    
driver.close()


    
