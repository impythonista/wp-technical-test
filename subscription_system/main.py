import datetime

from dateutil.relativedelta import relativedelta

from customer import Customer
from plan import Plan
from website import Website


def main():
    # Initialize different plans
    single_plan = Plan('Single', 49, 1)
    plus_plan = Plan('Plus', 99, 3)
    infinite_plan = Plan('Infinite', 249, -1)

    # Initialize multiple websites
    website_1 = Website('https://website_1.com')
    website_2 = Website('https://website_2.com')
    website_3 = Website('https://website_3.com')
    website_4 = Website('https://website_4.com')

    # Initialize multiple customers
    customer_1 = Customer('customer_1', '123456789', 'cust_1@yopmail.com')
    customer_2 = Customer('customer_2', '123456789', 'cust_2@yopmail.com')
    customer_3 = Customer('customer_3', '123456789', 'cust_3@yopmail.com')

    # customer_1 subscribed for single_plan
    customer_1.add_subscription(single_plan)
    print("{} has subscribed for {} plan".format(customer_1, customer_1.subscription.plan))
    
    # customer_1 added one website
    customer_1.add_website(website_1)
    print("{} has added website {} as per the {} plan".format(customer_1, \
            customer_1.websites, customer_1.subscription.plan))

    # customer_1 can not add more website in single_plan
    customer_1.add_website(website_2)
    print("{} can't add website {} as per the {} plan".format(customer_1, \
            website_2, customer_1.subscription.plan))

    # customer_1 can change plan from single_plan to plus_plan
    customer_1.change_plan(plus_plan)
    print("{} has changed his current plan {} to {} plan".format(customer_1, \
            single_plan, customer_1.subscription.plan))
    
    # customer_2 subscribe for infinite_plan
    customer_2.add_subscription(infinite_plan)
    
    # customer_2 can add multiple websites
    customer_2.add_website(website_1)
    customer_2.add_website(website_2)
    customer_2.add_website(website_3)
    customer_2.add_website(website_4)

    print("{} has added four websites {} under infinite plan".format(customer_2, \
            customer_2.websites))


if __name__ == "__main__":
    main()
