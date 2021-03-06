#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import unittest
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# the emulator is sometimes slow
SLEEPY_TIME = 2

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def get_desired_capabilities(app):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'HUAWEI GR3 2017',
        'app': PATH('../../apps/' + app),
        'newCommandTimeout': 240,
        'no-reset': True,
        'full-reset': False
    }
    return desired_caps


class PathaoTests(unittest.TestCase):
    def setUp(self):
        desired_caps = get_desired_capabilities('app-stage-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_tap(self):
        self.driver.implicitly_wait(20)
        EditText = self.driver.find_elements_by_class_name("android.widget.EditText")
        Button = self.driver.find_element_by_class_name("android.widget.Button")
        EditText[0].click()
        EditText[0].send_keys("01737788992")
        EditText[1].click()
        self.driver.implicitly_wait(5)
        EditText[1].send_keys("asdfgh")
        Button.click()
        self.driver.implicitly_wait(200)
        EditText[0].click()
        EditText[0].send_keys("01737788992")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PathaoTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
