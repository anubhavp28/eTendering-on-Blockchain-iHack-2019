from stellar_base.builder import Builder

def pay(message, amount, secret, address):

	sender_secret = secret
	receiver_address = address

	builder = Builder(secret=sender_secret, horizon_uri=None, network='TESTNET')
	builder.add_text_memo(message).append_payment_op(destination=receiver_address, amount=amount, asset_code='XLM')
	builder.sign()
	response = builder.submit()
