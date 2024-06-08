import inspect

import pytest
import logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

@pytest.mark.usefixtures("setup_and_teardown")
class BaseClass:

    def WaitElement(self,locator):
        WebDriverWait(self.driver,10).until((EC.presence_of_element_located(locator)))

    def ActionMove(self,locator1):
        return ActionChains(self.driver).move_to_element(locator1)

    def selectIndex(self,locator,index):
        return Select(locator).select_by_index(index)

    def selectByText(self,locator, text):
        return Select(locator).select_by_visible_text(text)


    def wait(self):
        return self.driver.implicitly_wait(5)

    def getLogger(self):
        # This line retrieves the name of the calling function.
        loggerName = inspect.stack()[1][3]

        # This line creates or retrieves a logger object using the name of the calling function.
        logger = logging.getLogger(loggerName)

        # Check if the logger has handlers already to avoid duplicate logs.
        if not logger.handlers:
            # Create a FileHandler object to write log records to a file.
            filehandler = logging.FileHandler("logfile.log")

            # Create a Formatter object with the specified format.
            formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

            # Set the formatter to the FileHandler.
            filehandler.setFormatter(formatter)

            # Add the FileHandler to the logger.
            logger.addHandler(filehandler)

            # Optionally, set the logging level. For example, to DEBUG.
            logger.setLevel(logging.ERROR)

        return logger


"""
    def getLogger(self):
        #This line retrieves the name of the calling function (the function that called the function containing this code). It uses the inspect module to inspect the call stack and retrieves the name of the function at index 1, which is the immediate caller, and then selects the third element of the tuple returned by inspect.stack(), which is the name of the function.
        loggerName = inspect.stack()[1][3]
        #This line creates a logger object using the name of the calling function obtained in the previous line. It uses the getLogger function from the logging module to get or create a logger with the specified name.
        logger = logging.getLogger(loggerName)
        #This line creates a FileHandler object named filehandler, which will be responsible for writing log records to a file named "logfile.log".
        filehandler = logging.FileHandler("logfile.log")
        #This line creates a Formatter object named formatter with a specified format. The format string "%(asctime)s : %(levelname)s : %(name)s : %(message)s" specifies the format for log records. It includes placeholders like %(asctime)s for the time of the log message, %(levelname)s for the log level, %(name)s for the logger name, and %(message)s for the log message itself.
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        #This line sets the formatter (formatter) created in the previous line to the FileHandler object (filehandler). This ensures that log records written by this handler will be formatted according to the specified format
        filehandler.setFormatter(formatter)
"""
