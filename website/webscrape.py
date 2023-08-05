from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select #for dropdowns
from bs4 import BeautifulSoup
import time

user_platform = "PlayStation 5"
genre = "Action"
driver = webdriver.Chrome()
URL = "https://howlongtobeat.com/"
driver.get(URL) #opens webpage

search_button = driver.find_element(By.CSS_SELECTOR, ".MainNavigation_search_box__UUnYc.back_form")
search_button.click()

#wait for the search options button to appear then click it
search_options = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.CSS_SELECTOR, ".SearchOptions_search_options_button__Qbgn_.back_form.shadow_box")))
search_options.click()

min_hours = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.CSS_SELECTOR, ".SearchOptions_search_range_l__dk60A.back_form")))
min_hours.send_keys("4")

max_hours = driver.find_element(By.CSS_SELECTOR, ".SearchOptions_search_range_r__L_VRK.back_form")
max_hours.send_keys("15")

#wait until the platform drop down is clickable then click it. Note the need for . in the class name when searching by css selector
platform_selector = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".form_select.back_form")))
platform_selector.click()

#select the dropdown menu and pick the corresponding platform
platform_dropdown = Select(driver.find_element(By.CSS_SELECTOR, ".form_select.back_form"))
platform_dropdown.select_by_visible_text(user_platform)

genre_selector = Select(driver.find_element(By.NAME, "search_genre"))
genre_selector.select_by_visible_text(genre)

time.sleep(5)

html_content = driver.page_source
soup = BeautifulSoup(html_content, "html.parser")

game_titles = soup.find_all(lambda tag: tag.name == "a" and tag.get("class") == ["text_white"])

# print("TITLE")
# print(game_titles.text.strip())
    
for idx, title in enumerate(game_titles, 1):
    print(f"{idx}. {title.text.strip()}")

#exclusions = ["Main Story", "Main + Extra", "Completionist"]

# for title in game_titles:

#     if title in exclusions:
#         game_titles.remove(title)
# game_info_dict = {}

# for title in game_titles:
#     game_info_dict[title.text.strip()] = ""

# print("TITLE: ")
# print(title_elements[0])
# print(title_elements[1])

# game = game_titles[1]
# game.click()
# game_desc = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".GameSummary_profile_info__HZFQu.GameSummary_large__TIGhL")))
# desc = game_desc.text.strip()
# game_info_dict[game_title] = desc
# print(desc)
    
# search_options = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.CSS_SELECTOR, ".MainNavigation_search_box__UUnYc.back_form")))
# search_options.click()
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".SearchOptions_search_tab__iDtf_.back_blue.center.shadow_box")))


    
# for idx, (title, game_descriptions) in enumerate(game_info_dict.items(), 1):
#     print(f"{idx}. {title}:")
#     print(game_descriptions)
#     print("-" * 80)

# num = 0
# exclusions = ["Main Story", "Main + Extra", "Completionist"]
# for t, title in enumerate(game_titles_list, 1):
#     if title not in exclusions:
#         num += 1
#         print(f"{num}. {title}")


time.sleep(20)
driver.quit() #closes browser
