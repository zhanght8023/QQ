# encoding:utf-8
# !/usr/bin/python
import unittest
import time
from selenium import webdriver
from appium import webdriver
from genericpath import exists

class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['version'] = '7.0'
        desired_caps['deviceName'] = 'SM-C5000'
        #desired_caps['deviceName'] = "WTK7N16A17006921"
        desired_caps['appPackage'] = 'com.tencent.mobileqq'
        desired_caps['appActivity'] = 'com.tencent.mobileqq.activity.SplashActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        # desired_caps['app'] = PATH('C:\Users\Administrator\Desktop\QQ_762.apk')  # ???????App????????¦Ë??
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def test_logInOk(self):
        time.sleep(5)
        self.driver.find_element_by_name(u'µÇ Â¼').click()
        name = self.driver.find_element_by_name(u'QQºÅ/ÊÖ»úºÅ/ÓÊÏä')
        name.click()
        time.sleep(2)
        name.send_keys('2657886865')


        psd = self.driver.find_element_by_accessibility_id("ÃÜÂë °²È«")
        psd.click()
        psd.send_keys("++hongtao8023")
        time.sleep(2)
  
        blogin = self.driver.find_element_by_name("µÇÂ¼")
        blogin.click()
        time.sleep(5)
        try:
            if self.driver.find_element_by_name("µÇÂ¼").is_displayed():
                exist = True
        except Exception, e:
            print e
            exist = False
        self.assertEqual(exist, False)
        print u"-----------µÇÂ½³É¹¦----------"
       
 
    def test_logInFailed(self):
        time.sleep(5)
        self.driver.find_element_by_name(u'µÇ Â¼').click()
        name = self.driver.find_element_by_name(u'QQºÅ/ÊÖ»úºÅ/ÓÊÏä')
        name.click()
        time.sleep(2)
        name.send_keys('2657886865')


        psd = self.driver.find_element_by_accessibility_id(u"ÃÜÂë °²È«")
        psd.click()
        psd.send_keys("++hongtao")
        time.sleep(2)
  
        blogin = self.driver.find_element_by_name(u"µÇÂ¼")
        blogin.click()
        time.sleep(10)
        self.driver.switch_to_alert()

        self.driver.find_element_by_name(u'È·¶¨').click()
        #self.driver.find_element_by_id("dialogRightBtn").click()
        time.sleep(5)
    
        try:
            if self.driver.find_element_by_name(u"µÇÂ¼").is_displayed():
                exist = True
        except Exception, e:
            print e
            exist = False
        self.assertEqual(exist,True)
        print u"------------µÇÂ¼Ê§°Ü-----------------"
        
         

   

    def tearDown(self):
        self.driver.quit()





