
products=input('enter the list of products IDs:').split()
all_ids=set(products)
duplicates=set()
#duplicates
for id in products:
    if products.count(id)>1:
        duplicates.add(id)#gets duplicates
lost_ids=all_ids-duplicates
print("LOST PRODUCT ID's:",lost_ids)

