class Plan:
    def __init__(self, name, price, allowed_websites):
        self.name = name
        self.price = price
        self.allowed_websites = allowed_websites
    
    def __str__(self):
        return "{}".format(self.name)
    
    def new_website_allowed(self, website_count):
        if self.allowed_websites == -1:
            return True
        return self.allowed_websites > website_count
