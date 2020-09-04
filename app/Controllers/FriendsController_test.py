import unittest
from app.Controllers.FriendsController import FriendsController

class TestFriendsController(unittest.TestCase):
    def test_handle(self):
        test = FriendsController()
        # test using valid route for handle method
        request = {
            "route": "send_request",
            "userId": "2",
            "add": "1000",
        }
        result = test.handle(request)
        excepted = "False"
        self.assertEqual(result, excepted)

        # test using valid inroute for handle method
        request = {
            "route": "invalid_route",
            "userId": "2",
            "add": "1000",
        }
        result = test.handle(request)
        excepted = "False"
        self.assertEqual(result, excepted)

    def test_send_request(self):
        test = FriendsController()
        # test using invalid destination user id but valid origin user id
        request = {
            "route": "send_request",
            "userId": "2",
            "add": "1000",
        }
        result = test.handle(request)
        excepted = "False"
        self.assertEqual(result, excepted)

        # test using invalid destination user id and invalid origin user id
        request = {
            "route": "send_request",
            "userId": "200",
            "add": "1000",
        }
        result = test.handle(request)
        excepted = "False"
        self.assertEqual(result, excepted)

        # test using valid destination user id and valid origin user id
        request = {
            "route": "send_request",
            "userId": "2",
            "add": "8",
        }
        result = test.handle(request)
        excepted = "True"
        self.assertEqual(result, excepted)

    def test_accept_request(self):
        test = FriendsController()
        # test using invalid destination_user and invalid origin_user
        request = {
            "route": "accept_request",
            "userId": "2000",
            "add": "80000"
        }
        result = test.handle(request)
        excepted = "False"
        self.assertEqual(result, excepted)

        # test using valid destination_user and valid origin_user
        request = {
            "route": "accept_request",
            "userId": "2",
            "add": "8",
        }
        result = test.handle(request)
        excepted = "True"
        self.assertEqual(result, excepted)

        # test using valid invalid destination_user and valid origin_user
        request = {
            "route": "accept_request",
            "userId": "2",
            "add": "8000",
        }
        result = test.handle(request)
        excepted = "False"
        self.assertEqual(result, excepted)

        # test using valid valid destination_user and invalid origin_user
        request = {
            "route": "accept_request",
            "userId": "200000",
            "add": "8",
        }
        result = test.handle(request)
        excepted = "False"
        self.assertEqual(result, excepted)

    def test_get_friends(self):
        test = FriendsController()

        # test with valid user id to get all the friends
        request = {
            "route": "get_friends",
            "userId": "2",
        }
        result = test.get_friends(request)
        resulttype = type(result)
        # expected type is list
        expectedtype = type(['fad'])
        self.assertEqual(resulttype, expectedtype)

        # test with invalid user id to get all the friends
        request = {
            "route": "get_friends",
            "userId": "2000",
        }
        result = test.get_friends(request)
        expected = "False"
        self.assertEqual(result, expected)
