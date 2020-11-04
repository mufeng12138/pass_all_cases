from TestBase import TestBase
import yaml
# max_case = "C96"


def test_run():
    mf = TestBase()
    mf.test_login()
    mf.test_loc_task()
    mf.test_loc_project()
    mf.test_loc_case()
    mf.test_execute()


if __name__ == '__main__':
    # test_run()
    src = open("test_yaml/src.yml", mode="r", encoding="utf-8")
    data = yaml.load(src, Loader=yaml.FullLoader)
    print(data[0])

    # with open('test_yaml/src.yaml', mode="r", encoding='utf-8') as f:
    #     print(yaml.load(f.read(), Loader=yaml.Loader))