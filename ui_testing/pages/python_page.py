from ui_testing.pages.base_page import BasePage
from ui_testing.locators.python_locators import PythonLocators


class PythonMainPage(BasePage):
    """Class provides special methods for python.org pages"""

    def get_latest_python_version(self):
        """Provides getting string that contains python latest version"""
        return self.find_element(PythonLocators.LOCATOR_PYTHON_DOWNLOAD_LATEST_SECTION).text

    def get_mac_os_md5_sum(self):
        """Provides getting string with control md5 check sum for python mac os version"""
        return self.find_element(PythonLocators.LOCATOR_PYTHON_MAC_OS_MD5_SUM).text

    def click_download_latest(self):
        """Provides finding and clicking link to python latest version download page"""
        self.find_element(PythonLocators.LOCATOR_PYTHON_DOWNLOAD_LATEST_SECTION).click()

    def click_download_for_mac_link(self):
        """Provides finding and clicking button to download python .pkg file"""
        self.find_element(PythonLocators.LOCATOR_PYTHON_MAC_OS_DOWNLOAD_LINK).click()

    def click_docs_link(self):
        """Provides finding and clicking link to https://www.python.org/doc/ page"""
        self.find_element(PythonLocators.LOCATOR_PYTHON_DOCS_LINK).click()

    def search_doc(self, search_item):
        """Provides searching search_item string at the python doc page"""
        self.find_element(PythonLocators.LOCATOR_PYTHON_SEARCH_FIELD).send_keys(search_item)
        self.find_element(PythonLocators.LOCATOR_PYTHON_SUBMIT_BUTTON).click()

    def get_doc_for_metaclasses(self):
        """Provides getting https://www.python.org/dev/peps/pep-3115/ page after successful search request"""
        self.find_element(PythonLocators.LOCATOR_PYTHON_METACLASSES_3000).click()

    def get_post_history_content(self):
        """Provides getting post history content at the https://www.python.org/dev/peps/pep-3115/ page"""
        return self.find_element(PythonLocators.LOCATOR_PYTHON_POST_HISTORY_FIELD).text

    def click_at_slide_index(self, index):
        """Provides finding and clicking button with tab index on a main page"""
        python_locators = PythonLocators()
        index_tab_locator = python_locators.get_python_index_tab_locator(index)
        return self.find_element(index_tab_locator).click()

    def check_visibility_of_slide_content(self, index):
        """Provides finding and checking visibility of current index tab on a main page"""
        python_locators = PythonLocators()
        slide_locator = python_locators.get_python_slides_locator(index)
        return self.find_element(slide_locator).is_displayed()

    def get_slide_content(self, index):
        """Provides getting string with current index tab content on a main page"""
        python_locators = PythonLocators()
        content_locator = python_locators.get_python_slides_content_locator(index)
        return self.find_element(content_locator).text
