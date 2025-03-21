from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

URL = "https://www.moneycontrol.com/markets/global-indices/"

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.177 Safari/537.36"
    )
    chrome_options.binary_location = "/usr/bin/google-chrome"

    service = Service("/usr/bin/chromedriver")
    return webdriver.Chrome(service=service, options=chrome_options)

@app.route("/getGiftNifty", methods=["GET"])
def get_gift_nifty():
    driver = get_driver()
    try:
        driver.get(URL)
        wait = WebDriverWait(driver, 10)
        row_xpath = "//tr[td//a[@title='GIFT NIFTY']]"
        row_element = wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))

        value_xpath = f"{row_xpath}/td[3]"
        value_element = driver.find_element(By.XPATH, value_xpath)
        market_value = value_element.text.strip()

        return jsonify({
            "status": "success",
            "market": "GIFT NIFTY",
            "value": market_value
        })

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500
    finally:
        driver.quit()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
