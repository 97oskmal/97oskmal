from customer_controller import *
from product_controller import *
from order_controller import *

test = CustomerController()
test.add_customer("James","Blunt","5 Hollywood Street","Los Angeles","AB2 3CE","0322 010101")
test.amend_customer("17",first_name="Max")
print(test.customer_headings())

test = OrderController()
print(test.new_empty_order("1"))
