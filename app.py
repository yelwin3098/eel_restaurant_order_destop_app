import eel
from helper import *


eel.init("web")


##for orders
@eel.expose
def getTablesAndDishes():
    obj={"tables":getTables(),"dishes":getDishes()}
    return obj

@eel.expose
def createOrder(dish_id,table_id,order_count):
    currentDish=findById(Dish,dish_id)
    create(Order(dish_id=dish_id,table_id=table_id,
                 price=currentDish.price ,order_count=order_count))
    return table_id;

def getOrders():
    results=all(Order)
    for result in results:
        print(f"Dish name {result.dish.name}")
        print(f"Table name {result.table.name}")

@eel.expose
def getOrderByTable(id):
    resultList=list()
    results=search(Order,id)
    for result in results:
        obj={"id":result.id,"dish_name":result.dish.name,"table_name":result.table.name,
            "price":result.price,"count":result.order_count,"status":result.status}
        resultList.append(obj)
    return resultList

@eel.expose
def updateOrderStatus(id):
    currentOrder=findById(Order,id)
    currentOrder.status=0
    updateTableStatus(currentOrder.table_id,0)
    update()

def billOut(id):
    results=search(Order,id)
    total=0
    for result in results:
        total+=result.price * result.order_count

    print(f"Bill total is : {total}")

##for Tables
@eel.expose
def createTabe(name):
    create(Table(name=name))

@eel.expose
def updateTable(id,name):
    currentTable=findById(Table,id)
    currentTable.name=name
    update()

@eel.expose
def updateTableStatus(id,status):
    currentTable=findById(Table,id)
    currentTable.status=status
    update()

@eel.expose
def getTableById(id):
    result=findById(Table,id)
    return {"id":result.id,"name":result.name,"status":result.status}

@eel.expose
def getTables():
    resultList=list()
    results=all(Table)
    for result in results:
        obj={"id":result.id,"name":result.name,"status":result.status}
        resultList.append(obj)
    return resultList

@eel.expose
def deleteTable(id):
    currentObj=findById(Table,id)
    destroy(currentObj)

##for Dishes Object
@eel.expose
def deleteDish(id):
    currentObj=findById(Dish,id)
    destroy(currentObj)

@eel.expose
def updateDish(id,name,price):
    currentDish=findById(Dish,id)
    currentDish.name=name
    currentDish.price=price
    update()

@eel.expose
def getDishById(id):
    result=findById(Dish,id)
    return {"id":result.id,"name":result.name,"price":result.price,"status":result.status}

@eel.expose
def getDishes():
    results=all(Dish)
    resultDish=list();
    for result in results:
        obj={"id":result.id,"name":result.name,"price":result.price,"status":result.status}
        resultDish.append(obj)
    return resultDish
    
@eel.expose
def createDish(name,price):
    create(Dish(name=name,price=price))

@eel.expose
def updateDishStatus(id,status):
    currentDish=findById(Dish,id)
    currentDish.status=status
    update()

eel.start("index.html")