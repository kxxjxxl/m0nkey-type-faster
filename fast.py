from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

def get_word(browser):
    """
  gets the currently active word from the MonkeyType website.
    """
    try:
        words = browser.find_element_by_id("words")
        words = words.find_elements(by=By.TAG_NAME, value="div")
        for word in words:
            if "active" in word.get_attribute("class"):
                return word.text
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def type_word(word, keyboard, delay):
    """
    types a word using a simulated keyboard.
    """
    keyboard.type(word)  # type the word
    time.sleep(delay)  # wait for a delay
    keyboard.press(Key.space)  # press the space key
    keyboard.release(Key.space)  # release the space key
    time.sleep(delay)  # wait for a delay

def monkey_type_bot(chrome_driver_path, delay=0.00075, max_words=1000):
    """
    runs the MonkeyType bot.
    """
    keyboard = Controller()
    browser = webdriver.Chrome(chrome_driver_path)
    url = 'https://monkeytype.com'
    browser.get(url)

    # Click the cookie popup button
    button = browser.find_element_by_xpath('//*[@id="cookiePopup"]/div[2]/div[2]/div[1]').click()

    # Wait for the website to load
    time.sleep(10)

    # Counter for the number of words typed
    word_count = 0

    while word_count < max_words:
        word = get_word(browser)
        if word:
            type_word(word, keyboard, delay)
            word_count += 1

        # Wait for a delay
        time.sleep(delay)

    # Close the browser after typing the maximum number of words
    browser.close()

if __name__ == "__main__":
    # Replace with the path to your Chrome driver
    chrome_driver_path = "PATH_TO_YOUR_CHROME_DRIVER"
    monkey_type_bot(chrome_driver_path)
