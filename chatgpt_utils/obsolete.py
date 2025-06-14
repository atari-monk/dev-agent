from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def send_line(driver: webdriver.Chrome, prompt: str, input_area_id: str="prompt-textarea"):
    try:
        input_area = driver.find_element(By.ID, input_area_id)
        input_area.clear()
        input_area.send_keys(prompt)
        input_area.send_keys(Keys.RETURN)
        print("Prompt sent successfully")
        return True
    except Exception as e:
        print(f"Failed to send prompt: {str(e)}")
        return False

def send_multiline(driver: webdriver.Chrome, prompt: str, input_area_id: str="prompt-textarea"):
    try:
        input_area = driver.find_element(By.ID, input_area_id)
        input_area.clear()

        lines = prompt.split("\n")
        for i, line in enumerate(lines):
            input_area.send_keys(line)
            if i < len(lines) - 1:
                input_area.send_keys(Keys.SHIFT, Keys.ENTER)
                input_area.send_keys(Keys.NULL)

        input_area.send_keys(Keys.RETURN)
        print("Prompt sent successfully")
        return True
    except Exception as e:
        print(f"Failed to send prompt: {str(e)}")
        return False
