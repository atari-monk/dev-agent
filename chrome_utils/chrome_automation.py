from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chatgpt_utils.chatgpt_config import ChatGPTConfig
from chrome_utils.chrome_profiles import get_chrome_profile
from utils.valid_url import is_valid_url


def open_chrome_with_profile(config: ChatGPTConfig) -> webdriver.Chrome | None:
    if not is_valid_url(config.page):
        raise ValueError(f"Invalid URL: '{config.page}'. Must include scheme (e.g., https://) and domain.")
    
    if not (profile := get_chrome_profile(config.config_path)):
        print("No active Chrome profile found")
        return None
    
    active_profile = profile["chromeProfilePath"]
    profile_directory = profile["profileDirectory"]
    custom_path = profile["customPath"]
    if custom_path:
        active_profile = custom_path
    print(f"Active Profile: {active_profile}, Profile Directory: {profile_directory}")

    options = Options()
    options.add_argument(rf"user-data-dir={active_profile}") # type: ignore
    options.add_argument(f"profile-directory={profile_directory}") # type: ignore
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) # type: ignore
    options.add_argument("--disable-blink-features=AutomationControlled") # type: ignore

    if config.detach:
        options.add_experimental_option("detach", True) # type: ignore

    driver = webdriver.Chrome(options=options)
    driver.get(config.page)
    print(f"Successfully opened: {config.page}")
    return driver