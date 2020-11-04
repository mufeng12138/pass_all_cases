import os
from selenium import webdriver
# import pytest
import time
import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

os.environ['http_proxy'] = 'http://127.0.0.1:1080'
os.environ['https_proxy'] = 'https://127.0.0.1:1080'

base_url = r"http://10.215.142.114/LightTower/login"
user_name = "userBase.userName"
user_passwd = "userBase.password"
name = "zhang_s"
passwd = "zhang_s@ecidi"
loc_submit = "submit_button"

home_id = "fw-header"
task_id = "MENU_MYPJ"

loc_pro_name = "projectInformation.projectName"
loc_search_proname_id = "pjt_search"

loc_case_id = "t1"
loc_case_no_id = "testcaseCode"

loc_btn_id = "testcase_btn"
loc_execute_class = "execute"

loc_popup_title_id = "popup_title"
loc_popup_ok_id = "popup_ok"

project_name = "测试数据"
version_name = "0722"
max_case = "C86"

save_path = r"E:\python_space\pass_all_cases\pic"

quiet = True
quiet = False
wait_timeout = 5

N = 100


class TestBase:
    def __init__(self):
        # self.project_name = input("请输入项目名称，以回车结束：")
        self.project_name = project_name
        self.loc_pro_name = loc_pro_name
        self.loc_search_proname_id = loc_search_proname_id
        self.loc_case_id = loc_case_id
        self.loc_case_no_id = loc_case_no_id
        self.max_case = max_case
        self.loc_btn_id = loc_btn_id
        self.loc_execute_class = loc_execute_class
        self.loc_popup_title_id = loc_popup_title_id
        self.loc_popup_ok_id = loc_popup_ok_id

        self.url = base_url
        self.quiet = quiet
        # self.timeout = timeout

        if self.quiet:
            option = webdriver.ChromeOptions()
            option.add_argument('headless')  # 静默模式
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = webdriver.Chrome()

        self.driver.get(self.url)
        self.driver.maximize_window()

        self.user_name = user_name
        self.user_passwd = user_passwd
        self.name = name
        self.passwd = passwd
        self.home_id = home_id
        self.task_id = task_id
        self.save_path = save_path

    def web_screen_shoot(self, reason="default"):
        picture_time = time.strftime("%Y-%m-%d_%H%M%S", time.localtime(time.time()))
        self.driver.get_screenshot_as_file(self.save_path + '\\' + picture_time + "_" + reason + '.png')
        print(picture_time+reason)

    def until_wait(self, timeout, mode, content):
        try:
            # self.driver.find_element(*(eval('By.' + mode), content))
            WebDriverWait(self.driver, 10). \
                until_not(lambda x: x.find_element(By.ID, 'loginFrm'))
            # until(self.driver.find_element(By.ID, content))
            # until(self.driver.find_element(By.ID, 'loginFrm'))
            # until(self.driver.find_element(*(eval('By.' + mode), content)))
        finally:
            print("end")
            self.driver.quit()

    # def until_wait(self, timeout, mode, content):
    #     try:
    #         # print('By.' + mode)
    #         wait_result = WebDriverWait(
    #             driver=self.driver,
    #             timeout=timeout*1000,
    #             poll_frequency=0.5,
    #             ignored_exceptions=None
    #             # ).until(self.driver.find_element('By.'+mode, content))
    #         ).until(self.driver.find_element(*(eval('By.' + mode), content)))
    #         # self.driver.find_element(By.ID)
    #     finally:
    #         print("end")
    #         self.driver.quit()

    def wait_time(self, t=wait_timeout):
        self.driver.implicitly_wait(t)

    def save_screen(self):
        self.driver.get_screenshot_as_file(self.save_path)

    def test_login(self):
        login_name = self.driver.find_element_by_name(self.user_name)
        login_passwd = self.driver.find_element_by_name(self.user_passwd)
        login_name.clear()
        login_passwd.clear()
        login_name.send_keys(self.name)
        login_passwd.send_keys(self.passwd)
        # self.web_screen_shoot()
        self.driver.find_element_by_id(loc_submit).click()
        # self.driver.get_screenshot_as_png()

        # self.until_wait(10, 'ID', self.home_id)
        WebDriverWait(self.driver, 10).until_not(lambda x: x.find_element(By.ID, 'loginFrm'))

        # self.until_wait(100, 'ID', 'loginFrm')
        # self.driver.find_element(By.ID, 'loginFrm')
        # print(a)
        # time.sleep(3)
        self.web_screen_shoot("确定进入系统")

        # self.driver.find_element_by_id(self.home_id)
        # return flag

        # login_submit = self.driver.find_element_by_id(loc_submit).click()
        # print("login_submit =", login_submit)

    # 定位到我的任务
    def test_loc_task(self):
        self.driver.find_element_by_id(self.task_id).click()
        self.web_screen_shoot("点击我的任务")

    # 在我的任务中定位项目
    def test_loc_project(self):
        find_pro_name = self.driver.find_element_by_name(self.loc_pro_name)
        find_pro_name.clear()
        # print("clear")
        find_pro_name.send_keys(self.project_name)
        # print("project_name")
        self.driver.find_element_by_id(self.loc_search_proname_id).click()
        # self.wait_time()
        time.sleep(2)
        # wait_sleep(2)
        # print("click")
        # self.driver.find_element_by_xpath("//*[@id="1"]/td[2]")
        self.driver.find_element_by_xpath('//*[@id="1"]/td[2]/a/font').click()
        # self.wait_time()
        # wait_sleep(2)
        time.sleep(2)

    # 在我的用例中找到并执行用例
    def test_loc_case(self):
        self.driver.find_element_by_id(self.loc_case_id).click()
        # wait_sleep(3)
        self.web_screen_shoot("点击我的用例")
        # 输入目标用例
        input_case_no = self.driver.find_element_by_id(self.loc_case_no_id)
        input_case_no.send_keys(self.max_case)
        self.web_screen_shoot("输入最大用例并点回车")
        input_case_no.send_keys(Keys.ENTER)
        self.driver.find_element_by_id(self.loc_btn_id).click()
        self.web_screen_shoot("点击查询")
        # wait_sleep(3)
        # 第一条可执行用例
        # self.driver.find_element_by_class_name(self.loc_execute_class).click()
        # 第一条用例
        self.driver.find_element_by_xpath('//*[@id="1"]/td[17]/a[2]').click()
        # wait_sleep(3)
        self.web_screen_shoot("点击第一条用例执行")

    # 执行用例
    def test_execute(self):
        i = 0
        while i < N:
            try:
                self.driver.find_element_by_id("pass").click()
            except:
                print("done " + str(i))
                return
            self.web_screen_shoot(2)
            i += 1
            try:
                self.driver.find_element_by_id(self.loc_popup_ok_id).click()
            except NoSuchElementException:
                continue
