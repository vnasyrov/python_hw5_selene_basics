from selene import browser

browser.config.timeout = 2
browser.config.window_width = 1920
browser.config.window_height = 1080
browser.config.base_url = 'https://demoqa.com/automation-practice-form'

def close_modal():
    try:
        browser.element('#closeLargeModal').with_(timeout=0.5).click()
    except:
        pass