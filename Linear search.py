print("****LINEAR_SEARCH_PRODUCT****")
def linear_search_product(product_list, target_product):
    indices = []
    for index, product in enumerate(product_list):
        if product == target_product:
            indices.append(index)
    return indices
products = ["grapes", "banana", "apple", "grapes", "apple"]
target = "grapes"
result = linear_search_product(products, target)
print(result)  