class Book :
	def __init__(self,Name) :
		self.name = Name 
		self.orders = []
	def insert_buy(self,quantity,price) :
		buy_order = Order(self.name,len(self.orders)+1,
						  "BUY",quantity,price,False)
		print("--------------------")
		print("----- Insert Buy "+str(quantity)+"@"+str(price) + " id=" + str(len(self.orders)) +" on "+self.name)
		self.orders.append(buy_order)
		for order in self.orders :
			print(order)

		
	def insert_sell(self,quantity,price) :
		sell_order = Order(self.name,len(self.orders)+1,
						  "SELL",quantity,price,False)
		print("--------------------")
		print("----- Insert SELL "+str(quantity)+"@"+str(price) + " id=" + str(len(self.orders)) +" on "+self.name)
		self.orders.append(sell_order)
		print(self.name)
		for order in self.orders :
			print(order)

class Order:
	def __init__(self,book_name,id,type,quantity,price,is_executed=False) :
		self.id = id
		self.type = type
		self.quantity = quantity 
		self.unit_price = price
		self.is_executed=is_executed
		self.book_name = book_name
		
	def __repr__(self) : 
		if not self.is_executed : 
			return self.type + " " + str(self.quantity)+"@"+str(self.unit_price) + " id="+str(self.id)
		return "Execute " + str(quantity) + " at " + self.book_name
