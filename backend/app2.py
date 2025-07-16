import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

class Xpath_Util:
    def __init__(self):
        self.guessable_elements = ['input', 'button', 'select', 'textarea', 'a', 'label', 'img', 'div']
        self.known_attribute_list = ['id', 'name', 'placeholder', 'value', 'title', 'type', 'class', 'aria-label', 'data-testid']
        self.variable_names = []
        self.button_text_lists = []
        self.language_counter = 1
        self.xpath_collection = []

    def generate_xpath(self, driver):
        elements = driver.find_elements(By.XPATH, '//*')
        for element in elements:
            try:
                #tag = element.tag_name.lower()
                tag = element.tag_name
                if tag not in self.guessable_elements:
                    continue

                attr_found = False
                for attr in self.known_attribute_list:
                    attr_value = element.get_attribute(attr)
                    if attr_value and not self._is_auto_generated(attr_value):
                        xpath = f"//{tag}[@{attr}='{attr_value}']"
                        if self._is_xpath_unique(driver, xpath):
                            variable_name = self._generate_variable_name(tag, attr_value)
                            self.xpath_collection.append({
                                'tag': tag,
                                'attribute': attr,
                                'value': attr_value,
                                'xpath': xpath,
                                'variable_name': variable_name
                            })
                            attr_found = True
                            break

                if not attr_found and tag == 'button':
                    text = element.text.strip()
                    if text:
                        xpath = f"//button[text()='{text}']"
                        if self._is_xpath_unique(driver, xpath):
                            var_name = self._generate_variable_name(tag, text)
                            self.xpath_collection.append({
                                'tag': tag,
                                'attribute': 'text',
                                'value': text,
                                'xpath': xpath,
                                'variable_name': var_name
                            })

            except Exception as e:
                print(f"Error processing element: {e}")

    def _is_xpath_unique(self, driver, xpath):
        try:
            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, xpath)))
            return len(driver.find_elements(By.XPATH, xpath)) == 1
        except:
            return False

    def _is_auto_generated(self, value):
        return bool(re.search(r'\b\w{5,}\d+\w*\b', value))

    def _generate_variable_name(self, tag, value):
        #value = value.lower()
        value = re.sub(r'[\s\-\/\[\],.&]+', '_', value)
        value = re.sub(r'__+', '_', value).strip('_')
        return value

@app.route('/extract-xpaths', methods=['POST', 'GET'])
def extract_xpaths():
    if request.method == 'GET':
        url = request.args.get('normalizedUrl') or request.args.get('url')
        if not url:
            return jsonify({'error': 'URL is required'}), 400
    else:
        url = None

    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        if url:
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        else:
            html_content = request.get_json().get('html')
            if not html_content:
                return jsonify({'error': 'HTML content is required in POST request.'}), 400
            driver.get("data:text/html;charset=utf-8," + html_content)

        xpath_util = Xpath_Util()
        xpath_util.generate_xpath(driver)

        driver.quit()
        return jsonify({'xpaths': xpath_util.xpath_collection})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)