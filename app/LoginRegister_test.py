from LoginRegister import LoginRegister
import hashlib
import json
import unittest


class LoginRegisterTest(unittest.TestCase):
    def test_login(self):
        test = LoginRegister()
        # test using valid credentials
        password = "Mausam1"
        encoded_pass = hashlib.md5(password.encode())
        encrypted_pass = encoded_pass.hexdigest()
        credentials = {
            "username": "leo",
            "password": encrypted_pass
        }
        result = test.login(credentials)
        result = json.dumps(result)
        result = json.loads(result)
        expected = [[2, 'leo', '4b17751b60942d13404229d384d66347', 'mausam', 'dahal']]
        self.assertListEqual(expected, result)

        # test using invalid credentials
        password = "Mausam"
        encoded_pass = hashlib.md5(password.encode())
        encrypted_pass = encoded_pass.hexdigest()
        credentials = {
            "username": "leo",
            "password": encrypted_pass
        }
        result = test.login(credentials)
        result = json.dumps(result)
        result = json.loads(result)
        expected = "False"
        self.assertEqual(expected, result)

    def test_register(self):
        test = LoginRegister()

        # test using already registered username
        password = "test"
        encoded_pass = hashlib.md5(password.encode())
        encrypted_pass = encoded_pass.hexdigest()
        credentials = {
            "username": "leo",
            "password": encrypted_pass,
            "fname": "Mausam",
            "lname": "Dahal"
        }
        result = test.register(credentials)
        expected = "False"
        self.assertEqual(result, expected)

        # test using already registered username
        password = "test"
        encoded_pass = hashlib.md5(password.encode())
        encrypted_pass = encoded_pass.hexdigest()
        credentials = {
            "username": "test",
            "password": encrypted_pass,
            "fname": "Test First Name",
            "lname": "Test Last Name"
        }
        result = test.register(credentials)
        expected = "True"
        self.assertEqual(result, expected)
