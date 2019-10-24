import datetime

from dateutil.relativedelta import relativedelta


class Subscription:
    def __init__(self, plan, renewal_date):
        self.plan = plan
        self.renewal_date = renewal_date
    
    def is_active(self):
        return self.renewal_date >= datetime.datetime.today().date()

    def renew(self, renewal_date):
        self.renewal_date = self.__calculate_renewal_date(renewal_date)
    
    def change_plan(self, plan):
        self.plan = plan
    
    def __calculate_renewal_date(self, renewal_date):
        return renewal_date + relativedelta(years=1)
