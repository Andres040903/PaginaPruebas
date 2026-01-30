import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class ClickAndSendKeys(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("http://www.clouditeducation.com/pruebas")

    def tearDown(self):
        self.driver.quit()

    def test_click_and_type(self):
        self.driver.find_element(By.LINK_TEXT, "Pagina 2").click()
        nombre = self.driver.find_element(By.ID, "Segundo")
        nombre.send_keys("Karina")
        self.assertEqual(nombre.get_attribute("value"), "Karina")

if __name__ == "__main__":
    unittest.main()
