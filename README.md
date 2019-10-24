# Code Review

[https://gist.github.com/jbma/3b7e26c595f2e4c05525b0d70f4b3605](https://gist.github.com/jbma/3b7e26c595f2e4c05525b0d70f4b3605)

This is an view to create a user directly through the API while being authenticated.

What do you think of that code? Are there any issues you see? Please describe your evaluation of this code. Would you write it differently? If so, please rewrite it to meet your standards and explain the reasoning behind any changes.




# Licencing System

We would like to see how you solve an OO design problem. Let's create a simple subscription system. 
The goal is to emulate buying a yearly plan and attach website(s) to it.

There are 3 business entities : 

1. **Customer** - has a name, a password an email address, a subscription and a subscription renewal date. 
2. **Plan** - has a name, a price, and a number of websites allowance. 
3. **Website** - has an URL, and a customer


A customer should be able to subscribe to plan, move from a plan to another and manage websites (add/update/remove) according to his plan.
Subscriptions have a 1-year time value.



## Notes : 
1. Having a DB is optional
2. We have 3 plans :
   * Single, 1 website, 49$
   * Plus, 3 websites $99
   * Infinite, unlimited websites $249


* Please add automated tests, using unittest
* Please use plain Python for this test : no framework . Of course any useful libraries can be used
* Since we are looking for OOP architecture/pattern, no front-end is needed.
* Code should be posted on Github/Gitlab/BitBucket