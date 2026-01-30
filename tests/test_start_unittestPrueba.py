import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("http://www.clouditeducation.com/pruebas")

    def tearDown(self):
        self.driver.quit()

    def test_id(self):
        elemento = self.driver.find_element(By.ID, "noImportante")
        self.assertIsNotNone(elemento)

    def test_name(self):
        elemento2 = self.driver.find_element(By.NAME, "ultimo")
        self.assertIsNotNone(elemento2)

if __name__ == "__main__":
    unittest.main()
