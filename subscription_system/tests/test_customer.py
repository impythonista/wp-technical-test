import unittest

from customer import Customer
from plan import Plan
from website import Website
from subscription import Subscription

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.single_plan = Plan('Single', 49, 1)
        self.plus_plan = Plan('Plus', 99, 3)

        self.website_1 = Website('https://google.com')
        self.website_2 = Website('https://google.com')
        
        self.customer_1 = Customer('customer_1', '123456789', 'cust_1@yopmail.com')
    
    def test_customer_can_add_website(self):
        self.customer_1.add_subscription(self.single_plan)
        self.customer_1.add_website(self.website_1)
        self.assertEqual(len(self.customer_1.websites), 1)
    
    def test_customer_can_add_website_as_per_the_plan(self):
        self.customer_1.add_subscription(self.plus_plan)
        self.customer_1.add_website(self.website_1)
        self.customer_1.add_website(self.website_2)
        self.assertEqual(len(self.customer_1.websites), 2)
    
    def test_customer_can_not_add_website(self):
        self.customer_1.add_subscription(self.single_plan)
        self.customer_1.add_website(self.website_1)
        self.customer_1.add_website(self.website_1)
        self.assertNotEqual(len(self.customer_1.websites), 2)
    
    def test_customer_can_change_plan(self):
        self.customer_1.add_subscription(self.single_plan)
        old_plan = self.customer_1.subscription.plan
        self.customer_1.add_subscription(self.plus_plan)
        new_plan = self.customer_1.subscription.plan
        self.assertNotEqual(old_plan, new_plan)
    
    def test_customer_can_add_subscription(self):
        self.customer_1.add_subscription(self.single_plan)
        self.assertIsInstance(self.customer_1.subscription, Subscription)


