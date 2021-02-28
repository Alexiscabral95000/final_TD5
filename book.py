import pandas as pd 

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
		print(self)

		
	def insert_sell(self,quantity,price) :
		sell_order = Order(self.name,len(self.orders)+1,
						  "SELL",quantity,price,False)
		print("--------------------")
		print("----- Insert SELL "+str(quantity)+"@"+str(price) + " id=" + str(len(self.orders)) +" on "+self.name)
		self.orders.append(sell_order)
		print(self)
	
	def __repr__(self) : 
		df = pd.DataFrame(columns = ["id","type","quantity","unit price","is executed"])

		for order in self.orders : 
			new_row = {"id" : order.id,
					   "type" : order.type,
					   "quantity" : order.quantity,
					   "unit price" : order.unit_price,
					   "is executed" : order.is_executed
					  }
			df = df.append(new_row,ignore_index = True)
			
		string_rep = "BOOK: " + self.name + "\n\n" + df.to_string()
		return string_rep

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
