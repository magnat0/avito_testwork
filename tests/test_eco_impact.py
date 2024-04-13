import pytest
import pages

class TestEcoImpact:

    def test_1(self, page):
        func_name = self.test_1.__name__
        pages.ecoImpactPage.open_index_page(page, -1, func_name)

    def test_2(self, page):
        func_name = self.test_2.__name__
        pages.ecoImpactPage.open_index_page(page, 0, func_name)

    def test_3(self, page):
        func_name = self.test_3.__name__
        pages.ecoImpactPage.open_index_page(page, 1, func_name)

    def test_4(self, page):
        func_name = self.test_4.__name__
        pages.ecoImpactPage.open_index_page(page, 999, func_name)
    
    def test_5(self, page):
        func_name = self.test_5.__name__
        pages.ecoImpactPage.open_index_page(page, 1000, func_name)
    
    def test_6(self, page):
        func_name = self.test_6.__name__
        pages.ecoImpactPage.open_index_page(page, 1001, func_name)
    
    def test_7(self, page):
        func_name = self.test_7.__name__
        pages.ecoImpactPage.open_index_page(page, 999999, func_name)

    def test_8(self, page):
        func_name = self.test_8.__name__
        pages.ecoImpactPage.open_index_page(page, 1000000, func_name)
    
    def test_9(self, page):
        func_name = self.test_9.__name__
        pages.ecoImpactPage.open_index_page(page, 1000001, func_name)
    
    def test_10(self, page):
        func_name = self.test_10.__name__
        pages.ecoImpactPage.open_index_page(page, 999999999, func_name)
    
    def test_11(self, page):
        func_name = self.test_11.__name__
        pages.ecoImpactPage.open_index_page(page, 1000000000, func_name)
    
    def test_12(self, page):
        func_name = self.test_12.__name__
        pages.ecoImpactPage.open_index_page(page, 1000000001, func_name)
    
    def test_13(self, page):
        func_name = self.test_13.__name__
        pages.ecoImpactPage.open_index_page(page, 999999999999, func_name)
    
    def test_14(self, page):
        func_name = self.test_14.__name__
        pages.ecoImpactPage.open_index_page(page, 1000000000000, func_name)
    
    def test_15(self, page):
        func_name = self.test_15.__name__
        pages.ecoImpactPage.open_index_page(page, 1000000000001, func_name)

    def test_16(self, page):
        func_name = self.test_16.__name__
        pages.ecoImpactPage.open_index_page(page, 10.5, func_name)
    
    def test_17(self, page):
        func_name = self.test_17.__name__
        pages.ecoImpactPage.open_index_page(page, 10.49, func_name)
    
    def test_18(self, page):
        func_name = self.test_18.__name__
        pages.ecoImpactPage.open_index_page(page, 10.51, func_name)
    
    def test_19(self, page):
        func_name = self.test_19.__name__
        pages.ecoImpactPage.open_index_page(page, "100", func_name)
    
    def test_20(self, page):
        func_name = self.test_20.__name__
        pages.ecoImpactPage.open_index_page(page, "indicator", func_name)
    
    def test_21(self, page):
        func_name = self.test_21.__name__
        pages.ecoImpactPage.open_index_page(page, 1000000000000000, func_name)

