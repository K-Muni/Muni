import unittest

from tests.signup import TestSignup
from tests.loginpage import TestLogin
from tests.Product import TestProductBrowsing
from tests.cart import TestCart
from tests.logout import TestLogout

unittest.TestLoader().loadTestsFromTestCase(TestSignup)
unittest.TestLoader().loadTestsFromTestCase(TestLogin)
unittest.TestLoader().loadTestsFromTestCase(TestProductBrowsing)
unittest.TestLoader().loadTestsFromTestCase(TestCart)
unittest.TestLoader().loadTestsFromTestCase(TestLogout)