# max_case = "C96"

from BasePage import *


# 逻辑层

def test_run():
    mf = BasePage()
    # 登录
    mf.test_login()
    # 找到我的任务
    mf.test_loc_task()
    # 找到项目
    mf.test_loc_project()
    # 找到用例
    mf.test_loc_case()
    # 执行用例
    # mf.test_execute()


if __name__ == '__main__':
    # 业务层
    test_run()
    # src = open("test_yaml/src.yml", mode="r", encoding="utf-8")
    # data = yaml.load(src, Loader=yaml.FullLoader)
    # print(data[0])

    # with open('test_yaml/src.yaml', mode="r", encoding='utf-8') as f:
    #     print(yaml.load(f.read(), Loader=yaml.Loader))
