from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

options = Options()

prefs = {'exit_type': 'Normal'}
options.add_experimental_option("prefs", {'profile': prefs})
options.add_argument(f"user-data-dir={os.getcwd()}/chrome")
options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1")
options.add_argument("no-sandbox")
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--autoplay-policy=no-user-gesture-required")
options.add_experimental_option("excludeSwitches", ['enable-automation'])


driver = webdriver.Chrome(options=options)

def save_cookies_to_netscape_file(cookies, output_file):
    with open(output_file, 'w') as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# This is a generated file! Do not edit.\n\n")
        f.write("# domain  include_subdomains  path  secure  expiration_date  name  value\n")
        
        for cookie in cookies:
            # Determine the correct attribute name for expiry based on Selenium version or browser
            expiry = cookie.get('expiry') or cookie.get('expires') or 0
            
            f.write(f"{cookie['domain']}\t")
            f.write("TRUE\t")  # include_subdomains
            f.write(f"{cookie['path']}\t")
            f.write("TRUE\t" if cookie.get('secure') else "FALSE\t")
            f.write(f"{int(expiry)}\t")  # expiration_date
            f.write(f"{cookie['name']}\t{cookie['value']}\n")

    return f"Cookies have been saved to {output_file}"

cookies = driver.get_cookies()
output_file = f"{os.getcwd()}/cookies0.txt"
save_cookies_to_netscape_file(cookies, output_file)
print("Cookies saved to:",output_file)

driver.quit()
