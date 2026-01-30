import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElementsLista(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("http://www.clouditeducation.com/pruebas")

    def tearDown(self):
        self.driver.quit()

    def test_celdas_y_conteo(self):
        celdas = self.driver.find_elements(By.TAG_NAME, "td")
        self.assertGreater(len(celdas), 0)

        textos = [c.text.strip() for c in celdas if c.text.strip()]
        print("Textos:", textos)
        print("Total celdas con texto:", len(textos))

if __name__ == "__main__":
    unittest.main()
