import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from config import FORM_URL, FIELD_VALUE


def main():
    # chrome config
    selenium_options = webdriver.ChromeOptions()
    selenium_options.add_experimental_option('detach', True)
    selenium_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=selenium_options)
    selenium_driver.execute_cdp_cmd('Network.setCacheDisabled', {'cacheDisabled': True})

    # wait until form opens
    print('1. waiting form')
    while True:
        selenium_driver.get(FORM_URL)
        item_elements = selenium_driver.find_elements(By.CSS_SELECTOR, '*[role="listitem"]')

        if len(item_elements) > 0:
            break

        time.sleep(0.3)
        print(time.time())

    print('2. form opened')
    time.sleep(0.3)

    # fill known fields
    for item_element in item_elements:
        field = get_field(item_element)

        if field is not None:
            value = FIELD_VALUE.get(field)
            input_element = item_element.find_element(By.TAG_NAME, 'input')
            input_element.send_keys(value)
    print('3. filled fields')

    # scroll to top
    selenium_driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
    print('4. done')


def get_field(item_element):
    title_divs = item_element.find_elements(By.CSS_SELECTOR, '*[role="heading"]')
    for title_div in title_divs:
        title_spans = title_div.find_elements(By.TAG_NAME, 'span')
        for title_span in title_spans:
            title_text = title_span.get_attribute('innerHTML')
            for field in FIELD_VALUE.keys():
                if field in title_text:
                    return field
    return None


if __name__ == '__main__':
    main()
