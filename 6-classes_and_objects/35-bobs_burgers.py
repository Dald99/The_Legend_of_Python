class Restaurant:
    name = ""
    category = ""
    rating = 0
    delivery = False


bobs_burgers = Restaurant()
bobs_burgers.name = "Bob's Burgers"
bobs_burgers.category = "American diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False


print(vars(bobs_burgers))
