products=input("Enter the list of product ID:").split()

all_ids=set(products)
duplicates=set()
# Find duplicate
for id in products:
    if products.count(id)>1:
        duplicates.add(id)

lost_ids=all_ids-duplicates
print("Lost Product IDs:",lost_ids)