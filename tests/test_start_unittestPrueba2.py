import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Prueba2_SoloId(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("http://www.clouditeducation.com/pruebas")

    def tearDown(self):
        self.driver.quit()

    def test_id(self):
        elemento = self.driver.find_element(By.ID, "noImportante")
        self.assertIsNotNone(elemento)

if __name__ == "__main__":
    unittest.main()
