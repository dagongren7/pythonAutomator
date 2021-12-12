from pythonAutomator.util.common_util import CommonUtil
from pythonAutomator.util.operation_header import OperationHeader
from pythonAutomator.util.operation_json import OperetionJson
from pythonAutomator.base.runmethod import RunMethod
from pythonAutomator.data.get_data import GetData
from pythonAutomator.data.dependent_data import DependdentData

class RunTest1():
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()

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
                expect_data = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                # header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    print('depend_case: ', depend_case)
                    self.depend_data = DependdentData(depend_case)
                    # 获取的依赖响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data
                    print(request_data)
                    #header头信息，是否要写入cookie
                if header == 'write':
                    res = self.run_method.run_main(method, url, request_data)
                    op_header = OperationHeader(res)
                    op_header.write_cookie()

                elif header == 'yes':
                    op_json = OperetionJson('../dataconfig/cookie.json')
                    cookie = op_json.get_data('apsid')
                    cookies = {
                        'apsid': cookie
                    }
                    res = self.run_method.run_main(method, url, request_data, cookies)
                else:
                    res = self.run_method.run_main(method, url, request_data)

                #判断预期是否包含在实际结果里面
                if self.com_util.is_contain(expect_data,res):
                       self.data.write_result(i,'success')
                       pass_count.append(i)
                else:
                       self.data.write_result(i,'fail')
                       fail_count.append(i)
        print('pass_count: ',pass_count)
        print('fail_count: ',fail_count)
if __name__ == '__main__':
    run = RunTest1()
    run.go_on_run()
