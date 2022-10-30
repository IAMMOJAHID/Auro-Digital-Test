from xml.dom import minidom
file = minidom.parse('orders.xml')
AddOrder = file.getElementsByTagName('AddOrder')
DeleteOrder = file.getElementsByTagName('DeleteOrder')
AddOrder[0].attributes['book'].value

book1_sell_price=[]
book1_sell_volume=[]
book1_BUY_price=[]
book1_BUY_volume=[]

book2_sell_price=[]
book2_sell_volume=[]
book2_BUY_price=[]
book2_BUY_volume=[]

book3_sell_price=[]
book3_sell_volume=[]
book3_BUY_price=[]
book3_BUY_volume=[]

i=0
while(i<90):
    if(AddOrder[i].attributes['book'].value=="book-1"):
        if(AddOrder[i].attributes['operation'].value=="SELL"):
            book1_sell_price.append(AddOrder[i].attributes['price'].value)
            book1_sell_volume.append(AddOrder[i].attributes['volume'].value)
        else:
            book1_BUY_price.append(AddOrder[i].attributes['price'].value)
            book1_BUY_volume.append(AddOrder[i].attributes['volume'].value)
    elif(AddOrder[i].attributes['book'].value=="book-2"):
        if(AddOrder[i].attributes['operation'].value=="SELL"):
            book2_sell_price.append(AddOrder[i].attributes['price'].value)
            book2_sell_volume.append(AddOrder[i].attributes['volume'].value)
        else:
            book2_BUY_price.append(AddOrder[i].attributes['price'].value)
            book2_BUY_volume.append(AddOrder[i].attributes['volume'].value)
    elif(AddOrder[i].attributes['book'].value=="book-3"):
        if(AddOrder[i].attributes['operation'].value=="SELL"):
            book3_sell_price.append(AddOrder[i].attributes['price'].value)
            book3_sell_volume.append(AddOrder[i].attributes['volume'].value)
        else:
            book3_BUY_price.append(AddOrder[i].attributes['price'].value)
            book3_BUY_volume.append(AddOrder[i].attributes['volume'].value)
    i+=1
 
print("BOOk-1")   
for i in range(len(book1_BUY_price)):
    if(i<len(book1_sell_price)):
        print(str(book1_BUY_volume[i])+"@"+str(book1_BUY_price[i]),end="") 
    if(i<len(book1_sell_price)):
        print("             "+str(book1_sell_volume[i])+"@"+str(book1_sell_price[i]))
        
print("\n")
print("BOOk-2")   
for i in range(len(book2_BUY_price)):
    if(i<len(book2_sell_price)):
        print(str(book2_BUY_volume[i])+"@"+str(book2_BUY_price[i]),end="") 
    if(i<len(book2_sell_price)):
        print("             "+str(book2_sell_volume[i])+"@"+str(book2_sell_price[i]))
        
print("\n")
print("BOOk-3")   
for i in range(len(book3_BUY_price)):
    if(i<len(book3_sell_price)):
        print(str(book3_BUY_volume[i])+"@"+str(book3_BUY_price[i]),end="") 
    if(i<len(book3_sell_price)):
        print("             "+str(book3_sell_volume[i])+"@"+str(book3_sell_price[i]))
            
        

