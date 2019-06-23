# -*- coding: utf-8 -*-
class BasePage(object):
    """
    Klasa bazowa, z której będą korzystały wszystkie podstrony (pages)
    """
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        """
        Tutaj będziemy sprawdzać poprawnośc wyświetlania strony
        np. czy wszystkie przyciski są widoczne itd.
        """
        return
