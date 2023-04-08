from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from testCases import  web_register_email_already_exists  as case1
from testCases import  web_register_empty_input as case2
from testCases import  web_register_password_input as case3
from testCases import  test_web_registor as case4
# import testCases.web_register_email_already_exists

_test_web_register_email_already_exists = TestLoader().loadTestsFromTestCase(testCaseClass=case1.TestWebRegistor)
_test_web_register_empty_input = TestLoader().loadTestsFromTestCase(testCaseClass=case2.TestWebRegistor)
_test_web_register_password_input = TestLoader().loadTestsFromTestCase(testCaseClass=case3.TestWebRegistor)
_test_web_registor = TestLoader().loadTestsFromTestCase(testCaseClass=case4.TestWebRegistor)

suite = TestSuite([_test_web_registor,_test_web_register_email_already_exists, _test_web_register_empty_input,_test_web_register_password_input])
# suite = TestSuite([_test_web_registor])

# runner = HTMLTestRunner(combine_reports=True,output='report_dir',report_title="Test web registor thaimooc")
runner = HTMLTestRunner(report_title="Test suite",output='report_suite',combine_reports=True,report_name="Test suite web registor thaimooc", add_timestamp=False)
runner.run(suite)