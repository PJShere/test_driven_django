from .base import FunctionalTest
from selenium.webdriver.common.keys import Keys # noqa


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        self.fail('write me!') 
