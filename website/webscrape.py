from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select #for dropdowns
from bs4 import BeautifulSoup
import time

#setting the values of user_platform and genre for the sake of testing.
#values based on user input in actual application
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

#setting the genre
genre_selector = Select(driver.find_element(By.NAME, "search_genre"))
genre_selector.select_by_visible_text(genre)

time.sleep(5)

#using beautiful soup to gather game titles
html_content = driver.page_source
soup = BeautifulSoup(html_content, "html.parser")

game_titles = soup.find_all(lambda tag: tag.name == "a" and tag.get("class") == ["text_white"])

game_info_dict = {}


#creating a dictionary with game titles as keys and their description as the values
for title in game_titles:
    game_name = title.text.strip()
    game = driver.find_element(By.PARTIAL_LINK_TEXT, game_name)
    game.click() #click the game in order to access the description
    
    game_desc = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".GameSummary_profile_info__HZFQu.GameSummary_large__TIGhL")))
    desc = game_desc.text.strip()
    game_info_dict[game_name] = desc
    
    #return to the search menu/page for next iteration
    search_options = WebDriverWait(driver, 10).until( EC.element_to_be_clickable((By.CSS_SELECTOR, ".MainNavigation_search_box__UUnYc.back_form")))
    search_options.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".SearchOptions_search_tab__iDtf_.back_blue.center.shadow_box")))
    
print(game_info_dict.items())


time.sleep(20)
driver.quit() #closes browser