import pickle


def save_cookies(driver, filename):
    with open(filename, 'wb') as f:
        pickle.dump(driver.get_cookies(), f)


def load_cookies(driver, filename):
    with open(filename, 'rb') as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)


def save_fingerprint(driver, filename):
    fingerprint = {
        'user-agent': driver.execute_script("return navigator.userAgent;"),
        'platform': driver.execute_script("return navigator.platform;"),
        'vendor': driver.execute_script("return navigator.vendor;"),
    }

    with open(filename, 'wb') as f:
        pickle.dump(fingerprint, f)


def load_fingerprint(driver, filename):
    with open(filename, 'rb') as f:
        fingerprint = pickle.load(f)
        driver.execute_cdp_cmd('Network.setUserAgentOverride', {'userAgent': fingerprint['user-agent']})