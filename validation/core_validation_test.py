from core_validation import CoreValidation
import unittest


class TestCoreValidation(unittest.TestCase):
    def test_isBlank(self):
        validate = CoreValidation()
        # when widget is blank and placeholder is Username
        widget = ""
        placeholder = "Username"
        result = validate.isBlank(widget, placeholder)
        self.assertTrue(result)

        # when widget is Leo and placeholder is blank
        widget = "Leo"
        placeholder = ""
        result = validate.isBlank(widget, placeholder)
        self.assertFalse(result)

        # when widget is blank and placeholder is blank
        widget = ""
        placeholder = ""
        result = validate.isBlank(widget, placeholder)
        self.assertTrue(result)

    def test_length(self):
        validate = CoreValidation()
        #when string length is less than requiredLength
        # while it should be greater
        string = ""
        requiredLength = 6
        validity = "greater"
        result = validate.length(string, requiredLength, validity)
        self.assertTrue(result)

        #when string length is greater than requiredLength
        # while it should be greater
        string = "abcdefghijklmnopqrstuvwxyz"
        requiredLength = 6
        validity = "greater"
        result = validate.length(string, requiredLength, validity)
        self.assertFalse(result)

        #when string length is greater than requiredLength
        # while it should be smaller
        string = "abcdefghijklmnopqrstuvwxyz"
        requiredLength = 6
        validity = "smaller"
        result = validate.length(string, requiredLength, validity)
        self.assertTrue(result)

        #when string length is greater than requiredLength
        # while it should be greater
        string = ""
        requiredLength = 6
        validity = "smaller"
        result = validate.length(string, requiredLength, validity)
        self.assertFalse(result)
