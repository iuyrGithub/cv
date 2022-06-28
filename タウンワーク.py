from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

MY_EMAIL = "Your Email Address"
MY_PASSWORD = "Your Password"

chrome_driver_path = "/Users/ryui/Documents/Python/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://townwork.net/tokyo/")

# Debugging Element is not clickable at point
# https://stackoverflow.com/questions/11908249/debugging-element-is-not-clickable-at-point-error

# ログイン
login = driver.find_element(by=By.LINK_TEXT, value="ログイン")
login.click()

email_login = driver.find_element(by=By.CSS_SELECTOR, value=".memberLogin_id input")
email_login.send_keys(MY_EMAIL)

password_login = driver.find_element(by=By.CSS_SELECTOR, value=".memberLogin_pw input")
password_login.send_keys(MY_PASSWORD)

submit_login = driver.find_element(by=By.ID, value="sbmbtn")
submit_login.click()

# 50回条件に適合する企業へ応募
# 官公庁案件、アルバイト、週2~3回勤務
for _ in range(50):
    time.sleep(3)
    # 詳細検索
    # # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-floatingButtonPrev"]/dl[7]/dd/ul/li[1]/label'))).click()
    # driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='part-time-job01']"))))
    check_part_time_job = driver.find_element(By.XPATH, '//*[@id="js-floatingButtonPrev"]/dl[7]/dd/ul/li[1]/label')
    # check_part_time_job.click()
    actions = ActionChains(driver)
    actions.move_to_element(check_part_time_job).perform()

    # What is WebdriverWait and How it works.
    # https://discuss.dizzycoding.com/elementclickinterceptedexception-message-element-click-intercepted-element-is-not-clickable-error-clicking-a-radio-button-using-selenium-and-python/
    time.sleep(1)
    job_field_select = driver.find_element(by=By.XPATH, value='//*[@id="js-floatingButtonPrev"]/dl[3]/dd/select')
    job_field_select.click()

    time.sleep(1)
    select_desk_work = driver.find_element(by=By.XPATH, value='//*[@id="js-floatingButtonPrev"]/dl[3]/dd/select/option[7]')
    select_desk_work.click()

    time.sleep(1)
    select_what_desk_work = driver.find_element(by=By.XPATH, value='//*[@id="js-floatingButtonPrev"]/dl[3]/dd/div/select[7]')
    select_what_desk_work.click()

    time.sleep(1)
    select_call_center = driver.find_element(by=By.XPATH, value='//*[@id="js-floatingButtonPrev"]/dl[3]/dd/div/select[7]/option[8]')
    select_call_center.click()

    time.sleep(1)
    click_under_selected_circumstances = driver.find_element(by=By.XPATH, value='//*[@id="js-floatingButtonArea"]/div/ul[1]/li[1]/div/input')
    click_under_selected_circumstances.click()

    # 応募企業表示画面
    search_by_word = driver.find_element(by=By.ID, value="textfield000")
    search_by_word.send_keys("官公庁")

    click_word_selection = driver.find_element(by=By.XPATH, value='//*[@id="fwForm"]/div[1]')
    click_word_selection.click()

    click_baito = driver.find_element(by=By.XPATH, value='//*[@id="01"]')
    click_baito.click()

    click_baito_selection = driver.find_element(by=By.XPATH, value='//*[@id="emcForm"]/div/input')
    click_baito_selection.click()

    specification = driver.find_element(by=By.XPATH, value='//*[@id="jsi-sch-panel-wrapper"]/dl[3]/dd/div[1]/a')
    specification.click()

    time.sleep(3)
    few_per_week = driver.find_element(by=By.XPATH, value='//*[@id="cndLmtForm"]/div[2]/div[1]/dl[1]/dd/div[2]/ul/li[5]/span/a')
    few_per_week.click()

    first_company = driver.find_element(by=By.XPATH, value='//*[@id="jsi-content-wrapper"]/div/div[2]/div[4]/div/div/div[2]/ul/li[2]/div/a/span')
    first_company.click()

    current_occupation = driver.find_element(by=By.ID, value="selectfield003")
    current_occupation.click()

    current_student = driver.find_element(by=By.XPATH, value='//*[@id="selectfield003"]/option[3]')
    current_student.click()

    defy_notification = driver.find_element(by=By.XPATH, value='//*[@id="jsi-form-wrapper"]/div/form/div[2]/div[1]/div/div/label')
    defy_notification.click()

    submit_to_company = driver.find_element(by=By.XPATH, value='//*[@id="jsi-form-wrapper"]/div/form/div[2]/div[2]/input')
    submit_to_company.click()

    time.sleep(3)
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass

    time.sleep(3)
    element = driver.find_element(by=By.XPATH, value='//*[@id="jsi-form-wrapper"]/div/form/div[2]/div[2]/input')
    driver.execute_script("arguments[0].click();", element)
    make_sure = driver.find_element(by=By.XPATH, value='//*[@id="jsi-custom-modal-wrapper"]/div/ul/li[2]/div/input')
    make_sure.click()

    back_to_tokyo = driver.find_element(by=By.XPATH, value='//*[@id="pageid-app-completion"]/div/header/div[2]/div/div[2]/nav/ul/li[1]/a/span')
    back_to_tokyo.click()






