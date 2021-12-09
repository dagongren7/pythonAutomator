from pythonAutomator.util.common_util import CommonUtil
from pythonAutomator.util.operation_header import OperationHeader
from pythonAutomator.util.operation_json import OperetionJson
from pythonAutomator.base.runmethod import RunMethod
from pythonAutomator.data.get_data import GetData

class RunTest1():
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()

    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        # 10  0,1,2,3
        #用例个数
        rows_count = self.data.get_case_lines()
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                print(i,',',request_data)
                # header = self.data.is_header(i)
                res = self.run_method.run_main(method, url, request_data)

if __name__ == '__main__':
    run = RunTest1()
    run.go_on_run()