import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import HtmlTestRunner

class TestWebRegistor(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()        
    def test_web_register_email_already_exists(self):
        driver = self.driver
        driver.get("https://idp.thaimooc.org/")
        driver.find_element(By.LINK_TEXT, "สมัครสมาชิก").click()
        driver.find_element(By.ID, "password").send_keys("123456789")
        driver.find_element(By.ID, "password-confirm").send_keys("12345789")
        driver.find_element(By.ID, "username").send_keys("kennnnnn")
        driver.find_element(By.ID, "email").send_keys("sekkri1234@gmail.com")
        driver.find_element(By.XPATH, "//input[@value='สมัครสมาชิก']").click()
        self.assertIn("อีเมลนี้มีอยู่ในระบบแล้ว",driver.page_source)
        driver.close()
        
def tearDown(self):
    print("DEBUG call tearDown")
    self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True,output='report_dir',report_title="Test web registor thaimooc"))
    