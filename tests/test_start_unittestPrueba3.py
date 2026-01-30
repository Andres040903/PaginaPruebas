import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Prueba3_ClassLinkPartial(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("http://www.clouditeducation.com/pruebas")

    def tearDown(self):
        self.driver.quit()

    def test_class(self):
        elemento = self.driver.find_element(By.CLASS_NAME, "rojo")
        self.assertIsNotNone(elemento)

    def test_link_text(self):
        link = self.driver.find_element(By.LINK_TEXT, "Pagina 2")
        self.assertIsNotNone(link)

    def test_partial_link_text(self):
        link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Pagina")
        self.assertIsNotNone(link)

if __name__ == "__main__":
    unittest.main()
