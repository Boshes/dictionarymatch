products_file = open("products.txt", "r+")
listings_file = open("listings.txt", "r+")

products = []
listings = []

for product_line in products_file:
    products.append(dict(eval(product_line)))
products_file.close()

for listing_line in listings_file:
    listings.append(dict(eval(listing_line)))
listings_file.close()
    
result = []

for product in products:
    res = dict()
    res["product_name"] = product["product_name"]
    res["listings"] = []
    for listing in listings:
        if product["model"] in listing["title"] \
            or product["product_name"] in listing["title"]:
                    res["listings"].append(listing)
    result.append(res)
res_file = open("results.txt", "w")
for prod in result:
    res_file.write(str(prod)+"\n")
    
res_file.close()