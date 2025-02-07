def calculateDiscount(products, discount_func):
    return sum(discount_func(price) for price in products)


products = [100, 200, 50, 300] 
discount_20 = lambda price: price * 0.8  

total_after_discount = calculateDiscount(products, discount_20)
print(total_after_discount) 


discount_20 = lambda price: price * 0.8  
total = calculateDiscount(products, discount_20)

print(f"Montant total après réduction : {total} €")  
