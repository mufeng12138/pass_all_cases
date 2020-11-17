import os
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# os.environ['http_proxy'] = 'http://127.0.0.1:1080'
# os.environ['https_proxy'] = 'https://127.0.0.1:1080'

# 数据层
max_case_init = 106
base_url_init = 4

# project_name = "银行存款余额调节表"
project_name = "测试数据"
version_name = "0722"
# version_name = "version0520case"
name = "zhang_s"
passwd = "zhang_s@ecidi"

max_case = "C" + str(max_case_init)
base_url = r"http://10.215.142.11" + str(base_url_init) + "/LightTower/login"
# save_path = r"E:\python_space\pass_all_po\pic"
save_path = os.getcwd() + r"\pic"

quiet = True
# quiet = False
wait_timeout = 5
# screenshot = True
# screenshot = False

limit = 100


# 对象库层
class BasePage:
    def __init__(self):
        # src = open("test_yaml/src.yaml", mode="r", encoding="utf-8")
        # data = yaml.load(src)
        # self.project_name = input("请输入项目名称，以回车结束：")
        self.project_name = project_name
        self.version_name = version_name
        self.max_case = max_case
        self.save_path = save_path
        self.name = name
        self.passwd = passwd

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
        self.driver.set_window_size(1920, 1080)
        # self.driver.set_window_size(1366, 768)

        self.name_loc_pro = "projectInformation.projectName"
        self.id_loc_search_proname = "pjt_search"
        self.id_loc_case = "t1"
        self.id_loc_case_no = "testcaseCode"
        self.id_loc_btn = "testcase_btn"
        self.class_loc_execute = "execute"
        self.id_loc_popup_title = "popup_title"
        self.id_loc_popup_ok = "popup_ok"
        self.id_version_name = "version_name"
        self.name_user_name = "userBase.userName"
        self.name_user_passwd = "userBase.password"
        self.id_home = "fw-header"
        self.id_task = "MENU_MYPJ"
        self.id_loc_submit = "submit_button"

    def web_screen_shoot(self, reason="default"):
        # self.driver.maximize_window()
        picture_time = time.strftime("%Y-%m-%d_%H%M%S", time.localtime(time.time()))
        self.driver.get_screenshot_as_file(self.save_path + '\\' + picture_time + "_" + reason + '.png')
        print(picture_time + "_" + reason)

    def until_wait(self, timeout, mode, content):
        try:
            # self.driver.find_element(*(eval('By.' + mode), content))
            WebDriverWait(driver=self.driver, timeout=timeout, poll_frequency=0.5, ignored_exceptions=None). \
                until(lambda x: x.find_element(*(eval('By.' + mode), content)), message="1532")
            # until_not(lambda x: x.find_element(By.ID, 'loginFrm'))
            # until(self.driver.find_element(By.ID, content))
            # until(self.driver.find_element(By.ID, 'loginFrm'))

        except (NoSuchElementException, TimeoutException):
            print("end")
            return

    # def save_screen(self):
    #     self.driver.get_screenshot_as_file(self.save_path)

    def test_login(self):
        login_name = self.driver.find_element_by_name(self.name_user_name)
        login_passwd = self.driver.find_element_by_name(self.name_user_passwd)
        login_name.clear()
        login_passwd.clear()
        login_name.send_keys(self.name)
        login_passwd.send_keys(self.passwd)
        self.driver.find_element_by_id(self.id_loc_submit).click()

        self.until_wait(wait_timeout, 'ID', self.id_task)
        # self.web_screen_shoot("确定进入系统")

    # 定位到我的任务
    def test_loc_task(self):
        loc = self.driver.find_element_by_id(self.id_task)
        webdriver.ActionChains(self.driver).move_to_element(loc).click(loc).perform()
        self.until_wait(wait_timeout, 'NAME', self.name_loc_pro)
        # time.sleep(2)
        # self.web_screen_shoot("点击我的任务")

    # 在我的任务中定位项目
    def test_loc_project(self):
        find_pro_name = self.driver.find_element_by_name(self.name_loc_pro)
        find_pro_name.clear()
        find_pro_name.send_keys(self.project_name)
        find_pro_name.send_keys(Keys.ENTER)
        self.driver.find_element_by_id(self.id_loc_search_proname).click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="1"]/td[2]/a/font').click()
        self.until_wait(wait_timeout, 'ID', self.id_loc_case)
        # self.web_screen_shoot("进入项目详情")

    # 在我的用例中找到并执行用例
    def test_loc_case(self):
        self.driver.find_element_by_id(self.id_loc_case).click()
        # wait_sleep(3)
        # self.web_screen_shoot("点击我的用例")
        self.until_wait(wait_timeout, 'ID', self.id_version_name)

        # 确定版本
        select_version = Select(self.driver.find_element_by_id(self.id_version_name))
        select_version.select_by_visible_text(self.version_name)
        self.until_wait(wait_timeout, 'ID', self.id_loc_case_no)
        # self.web_screen_shoot("选择版本" + self.version_name)

        # 输入目标用例
        # input_case_no = self.driver.find_element_by_id(self.id_loc_case_no)
        # input_case_no.send_keys(self.max_case)
        # time.sleep(2)
        self.driver.find_element_by_id(self.id_loc_case_no).send_keys(self.max_case)
        self.driver.find_element_by_id(self.id_loc_case_no).send_keys(Keys.ENTER)
        time.sleep(2)
        self.web_screen_shoot("输入最大用例并点回车")

        # self.driver.find_element_by_id(self.id_loc_btn).click()
        time.sleep(2)
        self.web_screen_shoot("点击查询")

        if self.driver.find_element_by_xpath('//*[@id="1"]/td[5]').text != self.max_case:
            # print(self.driver.find_element_by_xpath('//*[@id="1"]/td[5]').text)
            # print(self.max_case)
            print("case not found：" + \
                  self.driver.find_element_by_xpath('//*[@id="1"]/td[5]').text + " != " + self.max_case)
            return

        try:
            # 点击执行
            self.driver.find_element_by_xpath('//*[@id="1"]/td[17]/a[2]').click()
        except NoSuchElementException:
            print("NoSuchElementException")
            return
        # wait_sleep(3)
        self.web_screen_shoot("点击第一条用例执行")

    # 执行用例
    def test_execute(self):
        i = 0
        while i < limit:
            try:
                self.until_wait(wait_timeout, 'ID', "pass")
                self.driver.find_element_by_id("pass").click()

            except NoSuchElementException:
                print("共计" + str(i - 1) + "条通过")
                return
            self.web_screen_shoot(str(i + 1))
            i += 1
            try:
                self.driver.find_element_by_id(self.id_loc_popup_ok).click()
            except NoSuchElementException:
                continue
