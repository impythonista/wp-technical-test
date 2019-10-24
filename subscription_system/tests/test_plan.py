import unittest

from plan import Plan


class TestPlan(unittest.TestCase):

    def setUp(self):
        self.plus_plan = Plan('Plus', 99, 3)
        
    def test_new_website_allowed(self):
        self.assertTrue(self.plus_plan.new_website_allowed(2))

    def test_new_website_not_allowed(self):
        self.assertFalse(self.plus_plan.new_website_allowed(4))
