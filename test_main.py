# max_case = "C96"
import os
from BasePage import *


# 数据层
max_case = "C97"

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

# save_path = r"E:\python_space\pass_all_po\pic"
save_path = os.getcwd()+r"\pic"

quiet = True
# quiet = False
wait_timeout = 5

N = 100


# 逻辑层
def test_run():
    mf = BasePage()
    mf.test_login()
    mf.test_loc_task()
    mf.test_loc_project()
    mf.test_loc_case()
    mf.test_execute()


if __name__ == '__main__':
    # 业务层
    test_run()
    # src = open("test_yaml/src.yml", mode="r", encoding="utf-8")
    # data = yaml.load(src, Loader=yaml.FullLoader)
    # print(data[0])

    # with open('test_yaml/src.yaml', mode="r", encoding='utf-8') as f:
    #     print(yaml.load(f.read(), Loader=yaml.Loader))