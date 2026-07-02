import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
print(visits.head())
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
print(cart.head())
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
print(checkout.head())
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(purchase.head())

visitCart = pd.merge(visits,cart, how="left").reset_index()
print(visitCart.head())
print(len(visitCart))
nullCartTime = visitCart.cart_time.isnull().sum()
#print(nullCartTime)
perCart = (float(nullCartTime)/len(visitCart))*100
print(perCart)

cartCheck = pd.merge(cart,checkout, how="left").reset_index()
#print(cartCheck.head())
nullCheck = cartCheck.checkout_time.isnull().sum()
perCheck = (float(nullCheck)/len(cartCheck))*100
print(perCheck)

all_data = visits.merge(cart,how='left').merge(checkout,how='left').merge(purchase,how='left')
print(all_data.head())
nullpurchase = all_data.purchase_time.notnull().sum()
notNull= all_data.checkout_time.notnull().sum()
perCheck = ((float(notNull)-float(nullpurchase))/float(notNull))*100
print(perCheck)

all_data['totalTime']=all_data.purchase_time - all_data.visit_time
print(all_data)
meantime = all_data.totalTime.mean()
print(meantime)
