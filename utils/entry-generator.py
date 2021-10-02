from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

channel_url = '[URL]'
channel_description = '[DESC]'
channel_name = '[NAME]'
channel_language = '[LG]'
channel_category = '[category]'

url = 'https://www.youtube.com/watch?v=BSCR45veD1M'

# what if the url provided is already a channel one?
if ('channel' in url) or ('/c/' in url):
    channel_url = url
    print(channel_url)
else:
    try:
        # get channel url and name

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.headless = True  # also works
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="top-row"]/ytd-video-owner-renderer/a').click()
        channel_name = driver.find_element_by_xpath('//*[@id="text"]/a').get_attribute('innerHTML')
        WebDriverWait(driver, 20).until(EC.url_contains('channel'))
        channel_url = driver.current_url

        # get channel description
        if '/about' not in channel_url:
            driver.get(channel_url + '/about')
        WebDriverWait(driver, 20).until(EC.url_contains('/about'))
        channel_description = driver.find_element_by_id('description-container').text

    finally:
        driver.quit()

print(
    channel_language +
    ' - ' + channel_category +
    ' - ' + channel_name +
    ' - ' + channel_description +
    ' - ' + channel_url
)
