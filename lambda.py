import json
import pizzapi
from pizzapi import Customer, Address, Order, PaymentObject

def lambda_handler(event, context):

	order_pizza()

	return {
		"statusCode": 200,
		"body": json.dumps('Success')
	}

def orderPizza():
	print "starting to order the pizza"
	file = open("info.json").read()
	values = json.loads(file)

	customer = Customer(values["first_name"], values["last_name"], values["email"], values["phone_number"], values["address"])
	address = Address(*customer.address.split(','))
	store = address.closest_store()

	print "ordering from store" + str(store.get_details())

	order = Order(store, customer, address)
	order.add_item(values["pizza_code"])

	card = PaymentObject(values["cc_number"], values["cc_expiration"], values["cc_security"], values["cc_zip"])
	order.pay_with()
	print "congrats! order was succesful"

