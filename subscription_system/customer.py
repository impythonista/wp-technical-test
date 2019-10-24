from dateutil.relativedelta import relativedelta
import datetime

from subscription import Subscription

class Customer:

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
        self.subscription = None
        self.websites = list()
    
    def __str__(self):
        return "{}".format(self.name)
    
    def add_website(self, website):
        if self.__can_add_website():
            self.websites.append(website)
    
    def add_subscription(self, plan, renew_date=datetime.datetime.today().date()):
        self.subscription = Subscription(plan, renew_date)
    
    def change_plan(self, plan):
        self.subscription.change_plan(plan)

    def has_active_subscription(self):
        return self.subscription.is_active()
    
    @property
    def current_plan(self):
        return self.subscription.plan
    
    def __can_add_website(self):
        return self.has_active_subscription() and self.current_plan.new_website_allowed(len(self.websites))
