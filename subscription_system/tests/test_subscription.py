import unittest

from customer import Customer
from plan import Plan
from website import Website
from subscription import Subscription

import datetime

from dateutil.relativedelta import relativedelta


class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.single_plan = Plan('Single', 49, 1)
        self.plus_plan = Plan('Plus', 99, 3)
        self.renewal_date = datetime.datetime.today().date()
        self.subscription_1 = Subscription(self.single_plan, self.renewal_date)

    def test_is_subscription_active(self):
        self.assertTrue(self.subscription_1.is_active())
    
    def test_is_subscription_not_active(self):
        self.renewal_date = datetime.datetime.today().date() + relativedelta(years=-1)
        self.subscription_1 = Subscription(self.single_plan, self.renewal_date)
        self.assertFalse(self.subscription_1.is_active())

    def test_renew_subscription_for_one_year(self):
        self.subscription_1.renew(self.renewal_date)
        self.assertGreater(self.subscription_1.renewal_date.year, self.renewal_date.year)
    
    def test_plan_change_for_subscription(self):
        old_price_before_plan_change = self.subscription_1.plan.price
        self.subscription_1.change_plan(self.plus_plan)
        new_price_after_plan_change = self.subscription_1.plan.price
        self.assertNotEqual(old_price_before_plan_change, new_price_after_plan_change)