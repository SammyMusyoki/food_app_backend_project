
# from app import app
# from models import Owner, db,Restaurant,Menu,Driver,Location,Deliveries,Order,Customers,SuperAdmin,Admin
# from random import randint

# sample_data = [{
#     "owner_id" :91,
#     "name":"Kentucky Klein",
#     "email":"kfcinkenya@gmail.com",
#     "password":"dhedhuwedwu",
#     "image":"https://images.pexels.com/photos/17859453/pexels-photo-17859453/free-photo-of-women-color-light.jpeg?auto=compress&cs=tinysrgb&w=400&lazy=load"
# },{
#      "owner_id" :92,
#     "name":"Brian Waweru",
#     "email":"naivaskenya@gmail.com",
#     "password":"hdhehdiejefuhudeudd",
#     "image":"https://images.pexels.com/photos/17887967/pexels-photo-17887967.jpeg?auto=compress&cs=tinysrgb&w=400&lazy=load"},
# {
#     "owner_id" :93,
#     "name":"Wendy Kimani",
#     "email":"javahousekenya@gmail.com",
#     "password":"hdhehdieudeudd",
#     "image":"https://images.pexels.com/photos/17127836/pexels-photo-17127836/free-photo-of-evening-photo-of-a-young-woman-sitting-in-a-field.jpeg?auto=compress&cs=tinysrgb&w=400&lazy=load"
# },{
#     "owner_id" :94,
#     "name":"Lisa Gitau",
#     "email":"kelllykenya@gmail.com",
#     "password":"hdhehdiejfrjfrfrudeudd",
#     "image":"https://images.pexels.com/photos/17847846/pexels-photo-17847846/free-photo-of-sunset-fashion-beach-woman.jpeg?auto=compress&cs=tinysrgb&w=400&lazy=load"
# }
# ]

# with app.app_context():
#     owners = []
#     for owner in sample_data:
#         owner = Owner(**owner)
#         owners.append(owner)
#     db.session.add_all(owners)
#     db.session.commit()
    
    

# # sample_data2 = [
# #     {
# #       "restaurant_id": 1,
# #       "owner_id": 5,
# #       "restaurant_name": "Chicken Inn",
# #       "contact_number": "123-456-7890",
# #       "opening_hours": "08:00:00",
# #       "closing_hours": "20:00:00",
# #       "image": "",
# #       "payment_method": "Mpesa"
# #     },
# #     {
# #       "restaurant_id": 2,
# #       "owner_id": 6,
# #       "restaurant_name": "KFC",
# #       "contact_number": "987-654-3210",
# #       "opening_hours": "09:00:00",
# #       "closing_hours": "21:00:00",
# #       "image": "",
# #       "payment_method": "Stripe"
# #     },
# #     {
# #       "restaurant_id": 3,
# #       "owner_id": 7,
# #       "restaurant_name": "Naivas",
# #       "contact_number": "555-123-4567",
# #       "opening_hours": "07:30:00",
# #       "closing_hours": "19:30:00",
# #       "image": "",
# #       "payment_method": "Mpesa"
# #     },
# #     {
# #       "restaurant_id": 4,
# #       "owner_id": 8,
# #       "restaurant_name": "JavaHouse",
# #       "contact_number": "111-222-3333",
# #       "opening_hours": "10:00:00",
# #       "closing_hours":"19:00:00",
# #       "image":"",
# #       "payment_method": "Stripe"
# #     }
# #   ]
# # with app.app_context():
# #     restaurants = []
# #     for restaurant in sample_data2:
# #         restaurant = Restaurant(**restaurant)
# #         restaurants.append(restaurant)
# #     db.session.add_all(restaurants)
# #     db.session.commit()

# # sample_data3 = [
# #     {
# #       "menu_id": 1,
# #       "restaurant_id": 1,
# #       "menu_name": "Burger Combo",
# #       "description": "Delicious burger with fries and a drink",
# #       "prices": 1200
# #     },
# #     {
# #       "menu_id": 2,
# #       "restaurant_id": 1,
# #       "menu_name": "Pasta Alfredo",
# #       "description": "Creamy pasta with garlic and parmesan",
# #       "prices": 950
# #     },
# #     {
# #       "menu_id": 3,
# #       "restaurant_id": 1,
# #       "menu_name": "Sushi Platter",
# #       "description": "Assortment of fresh sushi rolls",
# #       "prices": 1800
# #     },
# #     {
# #       "menu_id": 4,
# #       "restaurant_id": 1,
# #       "menu_name": "Teriyaki Chicken",
# #       "description": "Grilled chicken in teriyaki sauce",
# #       "prices": 1300
# #     },
# #     {
# #       "menu_id": 5,
# #       "restaurant_id": 1,
# #       "menu_name": "Margherita Pizza",
# #       "description": "Classic pizza with tomato and cheese",
# #       "prices": 1000
# #     },
# #     {
# #       "menu_id": 6,
# #       "restaurant_id": 1,
# #       "menu_name": "Lasagna",
# #       "description": "Layers of pasta, meat, and cheese",
# #       "prices": 1100
# #     },
# #     {
# #       "menu_id": 7,
# #       "restaurant_id": 1,
# #       "menu_name": "Full English Breakfast",
# #       "description": "Eggs, bacon, sausages, beans, and more",
# #       "prices": 800
# #     },
# #     {
# #       "menu_id": 8,
# #       "restaurant_id": 2,
# #       "menu_name": "Steak",
# #       "description": "Grilled steak with sides",
# #       "prices": 1500
# #     },
# #     {
# #       "menu_id": 9,
# #       "restaurant_id": 2,
# #       "menu_name": "Vegetable Stir Fry",
# #       "description": "Assorted vegetables in a savory sauce",
# #       "prices": 850
# #     },
# #     {
# #       "menu_id": 10,
# #       "restaurant_id": 2,
# #       "menu_name": "Miso Soup",
# #       "description": "Traditional Japanese miso soup",
# #       "prices": 300
# #     },
    
# #     {
# #       "menu_id": 11,
# #       "restaurant_id": 2,
# #       "menu_name": "Jollof Rice",
# #       "description": "Rice cooked with tomato sauce, spices, and vegetables",
# #       "prices": 800
# #     },
# #     {
# #       "menu_id": 12,
# #       "restaurant_id": 2,
# #       "menu_name": "Fufu with Egusi Soup",
# #       "description": "Traditional fufu served with egusi soup",
# #       "prices": 950
# #     },
# #     {
# #       "menu_id": 13,
# #       "restaurant_id": 2,
# #       "menu_name": "Injera with Doro Wat",
# #       "description": "Ethiopian sourdough flatbread with spicy chicken stew",
# #       "prices": 1200
# #     },
# #     {
# #       "menu_id": 14,
# #       "restaurant_id": 2,
# #       "menu_name": "Bunny Chow",
# #       "description": "South African curry served in a hollowed-out bread loaf",
# #       "prices": 1000
# #     },
# #     {
# #       "menu_id": 15,
# #       "restaurant_id": 2,
# #       "menu_name": "Pounded Yam with Egusi Soup",
# #       "description": "Yam pounded into a smooth dough, served with egusi soup",
# #       "prices": 900
# #     },
# #     {
# #       "menu_id": 16,
# #       "restaurant_id": 2,
# #       "menu_name": "Chapati with Sukuma Wiki",
# #       "description": "Kenyan flatbread served with collard greens",
# #       "prices": 750
# #     },
# #     {
# #       "menu_id": 17,
# #       "restaurant_id": 3,
# #       "menu_name": "Couscous with Lamb Tagine",
# #       "description": "Moroccan dish with lamb and vegetables in a flavorful stew",
# #       "prices": 1300
# #     },
# #     {
# #       "menu_id": 18,
# #       "restaurant_id": 3,
# #       "menu_name": "Samoosa",
# #       "description": "Crispy pastry filled with spiced meat or vegetables",
# #       "prices": 600
# #     },
     
# #     {
# #       "menu_id": 19,
# #       "restaurant_id": 3,
# #       "menu_name": "Original Recipe Chicken",
# #       "description": "Crispy and delicious fried chicken made with KFC's secret blend of 11 herbs and spices",
# #       "prices": 400
# #     },
# #     {
# #       "menu_id": 20,
# #       "restaurant_id": 3,
# #       "menu_name": "Zinger Burger",
# #       "description": "Spicy chicken fillet topped with lettuce, mayo, and served in a soft bun",
# #       "prices": 350
# #     },
# #     {
# #       "menu_id": 21,
# #       "restaurant_id": 3,
# #       "menu_name": "Mashed Potatoes",
# #       "description": "Creamy mashed potatoes served with KFC's signature gravy",
# #       "prices": 150
# #     },
# #     {
# #       "menu_id": 22,
# #       "restaurant_id": 3,
# #       "menu_name": "Coleslaw",
# #       "description": "Fresh coleslaw made with cabbage, carrots, and KFC's special dressing",
# #       "prices": 100
# #     },
# #     {
# #       "menu_id": 23,
# #       "restaurant_id": 3,
# #       "menu_name": "Fries",
# #       "description": "Golden and crispy French fries",
# #       "prices": 120
# #     },
    
# #     {
# #       "menu_id": 24,
# #       "restaurant_id": 4,
# #       "menu_name": "Java House Breakfast",
# #       "description": "A hearty breakfast platter with eggs, bacon, sausages, toast, and more",
# #       "prices": 600
# #     },
# #     {
# #       "menu_id": 25,
# #       "restaurant_id": 4,
# #       "menu_name": "Chicken Avocado Wrap",
# #       "description": "Grilled chicken, avocado, lettuce, and mayo wrapped in a tortilla",
# #       "prices": 450
# #     },
# #     {
# #       "menu_id": 26,
# #       "restaurant_id": 4,
# #       "menu_name": "Java Cappuccino",
# #       "description": "Signature cappuccino made with Java House's premium coffee beans",
# #       "prices": 250
# #     },
# #     {
# #       "menu_id": 27,
# #       "restaurant_id": 4,
# #       "menu_name": "Chocolate Brownie",
# #       "description": "Decadent chocolate brownie served with a scoop of ice cream",
# #       "prices": 300
# #     },
# #     {
# #       "menu_id": 28,
# #       "restaurant_id": 4,
# #       "menu_name": "Greek Salad",
# #       "description": "Fresh salad with cucumbers, tomatoes, olives, and feta cheese",
# #       "prices": 350
# #     },
    
# #     {
# #       "menu_id": 29,
# #       "restaurant_id": 4,
# #       "menu_name": "Fried Chicken Combo",
# #       "description": "Crispy fried chicken pieces served with coleslaw and fries",
# #       "prices": 450
# #     },
# #     {
# #       "menu_id": 30,
# #       "restaurant_id": 4,
# #       "menu_name": "Spicy Wings",
# #       "description": "Succulent chicken wings marinated in spicy sauce",
# #       "prices": 350
# #     },
# #     {
# #       "menu_id": 31,
# #       "restaurant_id": 4,
# #       "menu_name": "Chicken Burgers",
# #       "description": "Delicious chicken burger with lettuce, mayo, and cheese",
# #       "prices": 300
# #     },
# #     {
# #       "menu_id": 32,
# #       "restaurant_id": 3,
# #       "menu_name": "Mash and Gravy",
# #       "description": "Creamy mashed potatoes served with rich gravy",
# #       "prices": 150
# #     },
# #     {
# #       "menu_id": 33,
# #       "restaurant_id": 4,
# #       "menu_name": "Soda Drinks",
# #       "description": "Assorted sodas and soft drinks",
# #       "prices": 100
# #     },
# #   ]

# # with app.app_context():
# #     menus = []
# #     for menu in sample_data3:
# #         menu = Menu(**menu)
# #         menus.append(menu)
# #     db.session.add_all(menus)
# #     db.session.commit()
# # sample_data4 =  [
# #     {
# #       "driver_id": 1,
# #       "name": "John Doe",
# #       "email": "john@example.com",
# #       "password": "hashedpassword123",
# #       "phone_number": "+1234567890",
# #       "image": "https://example.com/images/driver1.jpg",
# #       "current_location": "123 Main St, City"
# #     },
# #     {
# #       "driver_id": 2,
# #       "name": "Jane Smith",
# #       "email": "jane@example.com",
# #       "password": "hashedpassword456",
# #       "phone_number": "+9876543210",
# #       "image": "https://example.com/images/driver2.jpg",
# #       "current_location": "456 Elm St, Town"
# #     },
# #     {
# #       "driver_id": 3,
# #       "name": "David Johnson",
# #       "email": "david@example.com",
# #       "password": "hashedpassword789",
# #       "phone_number": "+1112223333",
# #       "image": "https://example.com/images/driver3.jpg",
# #       "current_location": "789 Oak St, Village"
# #     }]

# # with app.app_context():
# #     drivers = []
# #     for driver in sample_data4:
# #         driver = Driver(**driver)
# #         drivers.append(driver)
# #     db.session.add_all(drivers)
# #     db.session.commit()



# # sample_data12 = [
# #     {
# #       "location_id": 16,
# #       "owner_id": 5,
# #       "name": "Kitusuru",
# #       "delivery_fee": 50,
# #       "restaurant_id":1
# #     },
# #     {
# #       "location_id": 20,
# #       "owner_id": 6,
# #       "name": "ValleyRoad",
# #       "delivery_fee": 75,
# #       "restaurant_id":1
# #     },
# #     {
# #       "location_id": 23,
# #       "owner_id": 7,
# #       "name": "Hurlingharm",
# #       "delivery_fee": 60,
# #       "restaurant_id":1
# #     },
# #     {
# #       "location_id": 24,
# #       "owner_id": 7,
# #       "name": "Kenol",
# #       "delivery_fee": 390,
# #       "restaurant_id":1
# #     },
# #     {
# #       "location_id": 25,
# #       "owner_id": 8,
# #       "name": "Thika",
# #       "delivery_fee": 370,
# #       "restaurant_id":2
# #     },
# #     {
# #       "location_id": 26,
# #       "owner_id": 5,
# #       "name": "Industrial Area",
# #       "delivery_fee": 55,
# #       "restaurant_id":2
# #     },
# #     {
# #       "location_id": 27,
# #       "owner_id": 6,
# #       "name": "Pangani",
# #       "delivery_fee": 65,
# #       "restaurant_id":2
# #     },
# #     {
# #       "location_id": 28,
# #       "owner_id": 7,
# #       "name": "Ngara",
# #       "delivery_fee": 80,
# #       "restaurant_id":3
      
# #     },
# #     {
# #       "location_id": 29,
# #       "owner_id": 8,
# #       "name": "University UON",
# #       "delivery_fee": 50,
# #       "restaurant_id":3
# #     },
# #     {
# #       "location_id": 40,
# #       "owner_id": 8,
# #       "name": "Kileleshwa",
# #       "delivery_fee": 70,
# #       "restaurant_id":3
# #     },
# #     {
# #       "location_id": 41,
# #       "owner_id": 5,
# #       "name": "Kahawa",
# #       "delivery_fee": 60,
# #       "restaurant_id":3
# #     },
# #     {
# #       "location_id": 42,
# #       "owner_id": 6,
# #       "name": "Ruiru",
# #       "delivery_fee": 75,
# #       "restaurant_id":4
# #     },
# #     {
# #       "location_id": 43,
# #       "owner_id": 7,
# #       "name": "Ngong Road",
# #       "delivery_fee": 70,
# #       "restaurant_id":4
# #     },
# #     {
# #       "location_id": 44,
# #       "owner_id": 6,
# #       "name": "Kilimani",
# #       "delivery_fee": 55,
# #       "restaurant_id":4
# #     },
# #     {
# #       "location_id": 45,
# #       "owner_id": 5,
# #       "name": "CBD",
# #       "delivery_fee": 65,
# #       "restaurant_id":4
# #     },
   
# #   ]
# # with app.app_context():
# #     locations = []
# #     for location in sample_data12:
# #         location = Location(**location)
# #         locations.append(location)
# #     db.session.add_all(locations)
# #     db.session.commit()

# sampledata13 = [
#     {
#       "delivery_id": 1,
#       "order_id": 2,
#       "driver_id": 1,
#       "delivery_date_and_time": "2023-08-10T09:30:00",
#       "dispatch": False,
#       "delivered": False
#     },
#     {
#       "delivery_id": 2,
#       "order_id": 2,
#       "driver_id": 3,
#       "delivery_date_and_time": "2023-08-10T12:15:00",
#       "dispatch": False,
#       "delivered": False
#     },
#     {
#       "delivery_id": 3,
#       "order_id": 3,
#       "driver_id": 2,
#       "delivery_date_and_time": "2023-08-10T15:45:00",
#       "dispatch": False,
#       "delivered": False
#     },
#     {
#       "delivery_id": 4,
#       "order_id": 4,
#       "driver_id": 2,
#       "delivery_date_and_time": "2023-08-10T18:20:00",
#       "dispatch": False,
#       "delivered": False
#     },

#   ]


# with app.app_context():
#     deliveriess = []
#     for deliveries in sampledata13:
#         deliveries = Deliveries(**deliveries)
#         deliveriess.append(deliveries)
#     db.session.add_all(deliveriess)
# #     db.session.commit()
# sample_data15 = [
#     {
#       "order_id": 1,
#       "menu_id": 1,
#       "total_price": 1500,
#       "order_date_and_time": "2023-08-10T11:30:00",
#       "address": "Nairobi, Cityville",
#       "payment_method": "Mpesa"
#     },
#     {
#       "order_id": 2,
#       "menu_id": 4,
#       "total_price": 800,
#       "order_date_and_time": "2023-08-10T14:45:00",
#       "address": "CBD, Townville",
#       "payment_method": "Stripe"
#     },
#     {
#       "order_id": 3,
#       "menu_id": 2,
#       "total_price": 1200,
#       "order_date_and_time": "2023-08-10T17:15:00",
#       "address": "ValleyRoad, Villageton",
#       "payment_method": "Stripe"
#     },
#     {
#       "order_id": 4,
#       "menu_id": 3,
#       "total_price": 950,
#       "order_date_and_time": "2023-08-10T20:00:00",
#       "address": "NgongLane, Hamletville",
#       "payment_method": "Mpesa"
#     },
   
#   ]

# with app.app_context():
#     orders = []
#     for order in sample_data15:
#         order = Order(**order)
#         orders.append(order)
#     db.session.add_all(orders)
#     db.session.commit()
# # sample_data6= [
# #     {
# #       "customer_id": 31,
# #       "user_id": 1,
# #       "user_name": "Lexy Zamilla",
# #       "password": "lexyzam3764",
# #       "phone_number": "123-456-7890",
# #       "image": "https://images.pexels.com/photos/4006576/pexels-photo-4006576.jpeg?auto=compress&cs=tinysrgb&w=400"
# #     },
# #     {
# #       "customer_id": 32,
# #       "user_id": 2,
# #       "user_name": "Jane Smith",
# #       "password": "jejffrfrf",
# #       "phone_number": "987-654-3210",
# #       "image": "https://images.pexels.com/photos/3732667/pexels-photo-3732667.jpeg?auto=compress&cs=tinysrgb&w=400"
# #     },
# #     {
# #       "customer_id": 33,
# #       "user_id": 3,
# #       "user_name": "Lisa James",
# #       "password": "msjwjdjid",
# #       "phone_number": "555-555-5555",
# #       "image": "https://images.pexels.com/photos/1486213/pexels-photo-1486213.jpeg?auto=compress&cs=tinysrgb&w=400"
# #     },
# #     {
# #       "customer_id": 34,
# #       "user_id": 4,
# #       "user_name": "Wendy Jomo",
# #       "password": "jfgjtgitig",
# #       "phone_number": "123-456-7890",
# #       "image": "https://images.pexels.com/photos/2853592/pexels-photo-2853592.jpeg?auto=compress&cs=tinysrgb&w=400"
# #     },
# #     {
# #       "customer_id": 5,
# #       "user_id": 1,
# #       "user_name": "James Mureithi",
# #       "password": "djhweihdeiuh",
# #       "phone_number": "987-654-3210",
# #       "image": "https://images.pexels.com/photos/7533347/pexels-photo-7533347.jpeg?auto=compress&cs=tinysrgb&w=400"
# #     },
# #     {
# #       "customer_id": 6,
# #       "user_id": 1,
# #       "user_name": "Isaac Newton",
# #       "password": "hfjf334",
# #       "phone_number": "555-555-5555",
# #       "image": "https://images.pexels.com/photos/16055440/pexels-photo-16055440/free-photo-of-man-posing-among-banana-trees.jpeg?auto=compress&cs=tinysrgb&w=400"
# #     },
# #     {
# #       "customer_id": 7,
# #       "user_id": 2,
# #       "user_name": "Hamilton Waithera",
# #       "password": "waithera",
# #       "phone_number": "123-456-7890",
# #       "image": "https://images.pexels.com/photos/7656336/pexels-photo-7656336.jpeg?auto=compress&cs=tinysrgb&w=400"
# #     },
# #     {
# #       "customer_id": 8,
# #       "user_id": 2,
# #       "user_name": "James Kago",
# #       "password": "aroeje",
# #       "phone_number": "987-654-3210",
# #       "image": "https://images.pexels.com/photos/12495575/pexels-photo-12495575.png?auto=compress&cs=tinysrgb&w=400"
# #     },
# #     {
# #       "customer_id": 9,
# #       "user_id": 2,
# #       "user_name": "Nike Coater",
# #       "password": "cooleee",
# #       "phone_number": "555-555-5555",
# #       "image": "https://images.pexels.com/photos/16922807/pexels-photo-16922807/free-photo-of-red-dress.png?auto=compress&cs=tinysrgb&w=400"
# #     },
# #     {
# #       "customer_id": 10,
# #       "user_id": 2,
# #       "user_name": "Nazra Yaem",
# #       "password": "eliezer",
# #       "phone_number": "123-456-7890",
# #       "image": "https://images.pexels.com/photos/1848565/pexels-photo-1848565.jpeg?auto=compress&cs=tinysrgb&w=400"
# #     # },
# #     # {
# #     #   "customer_id": 11,
# #     #   "user_id": 2,
# #     #   "user_name": "jane_smith",
# #     #   "password": "hashed_password_11",
# #     #   "phone_number": "987-654-3210",
# #     #   "image": "jane_smith.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 12,
# #     #   "user_id": 2,
# #     #   "user_name": "mike_jones",
# #     #   "password": "hashed_password_12",
# #     #   "phone_number": "555-555-5555",
# #     #   "image": "mike_jones.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 13,
# #     #   "user_id": 3,
# #     #   "user_name": "john_doe",
# #     #   "password": "hashed_password_13",
# #     #   "phone_number": "123-456-7890",
# #     #   "image": "john_doe.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 14,
# #     #   "user_id": 3,
# #     #   "user_name": "jane_smith",
# #     #   "password": "hashed_password_14",
# #     #   "phone_number": "987-654-3210",
# #     #   "image": "jane_smith.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 15,
# #     #   "user_id": 3,
# #     #   "user_name": "mike_jones",
# #     #   "password": "hashed_password_3",
# #     #   "phone_number": "555-555-5555",
# #     #   "image": "mike_jones.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 16,
# #     #   "user_id": 3,
# #     #   "user_name": "john_doe",
# #     #   "password": "hashed_password_1",
# #     #   "phone_number": "123-456-7890",
# #     #   "image": "john_doe.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 17,
# #     #   "user_id": 3,
# #     #   "user_name": "jane_smith",
# #     #   "password": "hashed_password_2",
# #     #   "phone_number": "987-654-3210",
# #     #   "image": "jane_smith.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 18,
# #     #   "user_id": 3,
# #     #   "user_name": "mike_jones",
# #     #   "password": "hashed_password_3",
# #     #   "phone_number": "555-555-5555",
# #     #   "image": "mike_jones.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 19,
# #     #   "user_id": 4,
# #     #   "user_name": "john_doe",
# #     #   "password": "hashed_password_1",
# #     #   "phone_number": "123-456-7890",
# #     #   "image": "john_doe.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 20,
# #     #   "user_id": 4,
# #     #   "user_name": "jane_smith",
# #     #   "password": "hashed_password_2",
# #     #   "phone_number": "987-654-3210",
# #     #   "image": "jane_smith.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 21,
# #     #   "user_id": 4,
# #     #   "user_name": "mike_jones",
# #     #   "password": "hashed_password_3",
# #     #   "phone_number": "555-555-5555",
# #     #   "image": "mike_jones.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 22,
# #     #   "user_id": 4,
# #     #   "user_name": "john_doe",
# #     #   "password": "hashed_password_1",
# #     #   "phone_number": "123-456-7890",
# #     #   "image": "john_doe.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 23,
# #     #   "user_id": 4,
# #     #   "user_name": "jane_smith",
# #     #   "password": "hashed_password_2",
# #     #   "phone_number": "987-654-3210",
# #     #   "image": "jane_smith.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 24,
# #     #   "user_id": 4,
# #     #   "user_name": "mike_jones",
# #     #   "password": "hashed_password_3",
# #     #   "phone_number": "555-555-5555",
# #     #   "image": "mike_jones.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 25,
# #     #   "user_id": 5,
# #     #   "user_name": "john_doe",
# #     #   "password": "hashed_password_1",
# #     #   "phone_number": "123-456-7890",
# #     #   "image": "john_doe.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 26,
# #     #   "user_id": 5,
# #     #   "user_name": "jane_smith",
# #     #   "password": "hashed_password_2",
# #     #   "phone_number": "987-654-3210",
# #     #   "image": "jane_smith.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 27,
# #     #   "user_id": 5,
# #     #   "user_name": "mike_jones",
# #     #   "password": "hashed_password_3",
# #     #   "phone_number": "555-555-5555",
# #     #   "image": "mike_jones.jpg"
# #     # },
# #     # {
# #     #   "customer_id": 29,
# #     #   "user_id": 5,
# #     #   "user_name": "john_doe",
# #     #   "password": "hashed_password_1",
# #     #   "phone_number": "123-456-7890",
# #     #   "image": "john_doe.jpg"
# #     # },
    
   
# #     # {
# #     #   "customer_id": 30,
# #     #   "user_id": 5,
# #     #   "user_name": "emma_wilson",
# #     #   "password": "hashed_password_30",
# #     #   "phone_number": "111-222-3333",
# #     #   "image": "emma_wilson.jpg"
# #     }
# #   ]

# # with app.app_context():
# #     customers = []
# #     for customer in sample_data6:
# #         customer =Customers(**customer)
# #         customers.append(customer)
# #     db.session.add_all(customers)
# #     db.session.commit()



# # sample_data19 = [
# #     {
# #         "superadmin_id": 1,
# #         "customer_id": 6,
# #         "restaurant_id": 1,
# #         "owner_id": 5,
# #         "name": "Winnie Jane",
# #         "password": "adminwinnie456",
# #         "image": "https://images.pexels.com/photos/1055691/pexels-photo-1055691.jpeg?auto=compress&cs=tinysrgb&w=400"
# #     },
# #     {
# #         "superadmin_id": 2,
# #         "customer_id": 5,
# #         "restaurant_id": 2,
# #         "owner_id": 8,
# #         "name": "Chelsea Shell",
# #         "password": "adminchelseajd",
# #         "image": "https://images.pexels.com/photos/1192609/pexels-photo-1192609.jpeg?auto=compress&cs=tinysrgb&w=400"
# #     },
# #     {
# #         "superadmin_id": 3,
# #         "customer_id": 7,
# #         "restaurant_id": 4,
# #         "owner_id": 8,
# #         "name": "Wade Kamau",
# #         "password": "adjdjehdje",
# #         "image": "https://images.pexels.com/photos/2058659/pexels-photo-2058659.jpeg?auto=compress&cs=tinysrgb&w=400"
# #     }
# # ]

# # with app.app_context():
# #     for data in sample_data19:
# #         superadmin = SuperAdmin(
# #             superadmin_id=data["superadmin_id"],
# #             customer_id=data["customer_id"],
# #             restaurant_id=data["restaurant_id"],
# #             owner_id=data["owner_id"],
# #             name=data["name"],
# #             password=data["password"],
# #             image=data["image"]
# #         )
# #         db.session.add(superadmin)
    
# #     db.session.commit()
    
    
# sample_data20 = [
#     {
#         "admin_id": 1,
#         "customer_id": 6,
#         "restaurant_id": 1,
#         "owner_id": 5,
#         "name": "Lexy Jane",
#         "password": "adminwinniddde456",
#         "image": "https://images.pexels.com/photos/324030/pexels-photo-324030.jpeg?auto=compress&cs=tinysrgb&w=400"
#     },
#     {
#         "admin_id": 2,
#         "customer_id": 5,
#         "restaurant_id": 2,
#         "owner_id": 8,
#         "name": "Wesley Shell",
#         "password": "adminchelseahdhjd",
#         "image": "https://images.pexels.com/photos/1304647/pexels-photo-1304647.jpeg?auto=compress&cs=tinysrgb&w=400"
#     },
#     {
#         "admin_id": 3,
#         "customer_id": 7,
#         "restaurant_id": 4,
#         "owner_id": 8,
#         "name": "Whitney Kamau",
#         "password": "adjdjehdje",
#         "image": "https://images.pexels.com/photos/2896428/pexels-photo-2896428.jpeg?auto=compress&cs=tinysrgb&w=400"
#     }
# ]

# with app.app_context():
#     for data in sample_data20:
#         admin = Admin(
#             admin_id=data["admin_id"],
#             customer_id=data["customer_id"],
#             restaurant_id=data["restaurant_id"],
#             owner_id=data["owner_id"],
#             name=data["name"],
#             password=data["password"],
#             image=data["image"]
#         )
#         db.session.add(admin)
    
#     db.session.commit()
# sample_data30 = [
    
#       {
#        "menu_id": 1,
#        "restaurant_id": 1,
#        "image":"https://images.pexels.com/photos/59943/pexels-photo-59943.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "menu_name": "Burger Combos",
#        "description": "Delicious burger with fries and a drink",
#        "prices": 1200
#      },
#      {
#        "menu_id": 2,
#       "image":"https://images.pexels.com/photos/3338537/pexels-photo-3338537.jpeg?auto=compress&cs=tinysrgb&w=1600",
#       "restaurant_id": 1,
#       "menu_name": "Pasta Alfredos",
#       "description": "Creamy pasta with garlic and parmesan",
#       "prices": 950
#     },
#     {
#       "menu_id": 3,
#       "image":"https://images.pexels.com/photos/1247677/pexels-photo-1247677.jpeg?auto=compress&cs=tinysrgb&w=1600",
#       "restaurant_id": 1,
#       "menu_name": "Sushi Platterr",
#       "description": "Assortment of fresh sushi rolls",
#        "prices": 1800
#      },
#      {
#        "menu_id": 4,
#        "image":"https://images.pexels.com/photos/2067473/pexels-photo-2067473.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 1,
#        "menu_name": "Teriyakie Chicken",
#        "description": "Grilled chicken in teriyaki sauce",
#        "prices": 1300
#      },
#      {
#        "menu_id": 5,
#        "image":"https://images.pexels.com/photos/3590401/pexels-photo-3590401.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 1,
#        "menu_name": "Margheritah Pizza",
#       "description": "Classic pizza with tomato and cheese",
#        "prices": 1000
#      },
#      {
#        "menu_id": 6,
#        "image":"https://images.pexels.com/photos/64208/pexels-photo-64208.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 1,
#        "menu_name": "Lasagnaa",
#        "description": "Layers of pasta, meat, and cheese",
#        "prices": 1100
#      },
#      {
#        "menu_id":7,
#        "image":"https://images.pexels.com/photos/2347311/pexels-photo-2347311.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 1,
#        "menu_name": "Full English Breakfastt",
#        "description": "Eggs, bacon, sausages, beans, and more",
#        "prices": 800
#      },
#      {
#        "menu_id": 8,
#        "image":"https://images.pexels.com/photos/128408/pexels-photo-128408.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 2,
#        "menu_name": "Steak",
#        "description": "Grilled steak with sidess",
#        "prices": 1500
#      },
#      {
#        "menu_id": 9,
#        "image":"https://images.pexels.com/photos/299347/pexels-photo-299347.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 2,
#        "menu_name": "Vegetable Stirr Fry",
#        "description": "Assorted vegetables in a savory sauce",
#        "prices": 850
#      },
#      {
#        "menu_id": 10,
#        "image":"https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 2,
#        "menu_name": "Misoh Soup",
#        "description": "Traditional Japanese miso soup",
#        "prices": 300
#      },
#      {
#        "menu_id": 11,
#        "image":"https://images.pexels.com/photos/1211887/pexels-photo-1211887.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 2,
#        "menu_name": "Jolof Rice",
#        "description": "Rice cooked with tomato sauce, spices, and vegetables",
#        "prices": 800
#      },
#      {
#        "menu_id": 12,
#        "image":"https://images.pexels.com/photos/262978/pexels-photo-262978.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 2,
#        "menu_name": "Fufuh with Egusi Soup",
#        "description": "Traditional fufu served with egusi soup",
#        "prices": 950
#      },
#      {
#        "menu_id": 13,
#        "image":"https://images.pexels.com/photos/1893569/pexels-photo-1893569.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 2,
#        "menu_name": "Injerah with Doro Wat",
#       "description": "Ethiopian sourdough flatbread with spicy chicken stew",
#        "prices": 1200
#      },
#      {
#        "menu_id": 14,
#        "image":"https://images.pexels.com/photos/1833349/pexels-photo-1833349.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 2,
#        "menu_name": "Bunnie Chow",
#        "description": "South African curry served in a hollowed-out bread loaf",
#        "prices": 1000
#      },
#      {
#        "menu_id": 15,
#        "image":"https://images.pexels.com/photos/3434523/pexels-photo-3434523.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 2,
#        "menu_name": "Pounded Yamm with Egusi Soup",
#        "description": "Yam pounded into a smooth dough, served with egusi soup",
#        "prices": 900
#      },
#      {
#        "menu_id": 16,
#        "image":"https://images.pexels.com/photos/3338537/pexels-photo-3338537.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 2,
#        "menu_name": "Chapatie with Sukuma Wiki",
#        "description": "Kenyan flatbread served with collard greens",
#        "prices": 750
#      },
#      {
#        "menu_id": 17,
#        "image":"https://images.pexels.com/photos/2689419/pexels-photo-2689419.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 3,
#        "menu_name": "Couscouse with Lamb Tagine",
#        "description": "Moroccan dish with lamb and vegetables in a flavorful stew",
#        "prices": 1300
#      },
#      {
#        "menu_id": 18,
#        "image":"https://images.pexels.com/photos/1988624/pexels-photo-1988624.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 3,
#        "menu_name": "Samoosah",
#        "description": "Crispy pastry filled with spiced meat or vegetables",
#        "prices": 600
#      },
#      {
#        "menu_id": 19,
#        "image":"https://images.pexels.com/photos/5710204/pexels-photo-5710204.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 3,
#        "menu_name": "Originall Recipe Chicken",
#        "description": "Crispy and delicious fried chicken made with KFC's secret blend of 11 herbs and spices",
#        "prices": 400
#      },
#      {
#        "menu_id": 20,
#        "image":"https://images.pexels.com/photos/3801739/pexels-photo-3801739.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 3,
#        "menu_name": "Zingar Burger",
#        "description": "Spicy chicken fillet topped with lettuce, mayo, and served in a soft bun",
#        "prices": 350
#      },
#      {
#         "menu_id": 21,
#         "image":"https://images.pexels.com/photos/1049626/pexels-photo-1049626.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 3,
#        "menu_name": "Mashed Potatoees",
#        "description": "Creamy mashed potatoes served with KFC's signature gravy",
#        "prices": 150
#      },
#      {
#        "menu_id": 22,
#        "image":"https://images.pexels.com/photos/236887/pexels-photo-236887.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 3,
#        "menu_name": "Colesslaw",
#        "description": "Fresh coleslaw made with cabbage, carrots, and KFC's special dressing",
#        "prices": 100
#     },
#      {
#        "menu_id": 23,
#        "image":"https://images.pexels.com/photos/3219483/pexels-photo-3219483.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 3,
#        "menu_name": "Friies",
#        "description": "Golden and crispy French fries",
#       "prices": 120
#      },
#      {
#        "menu_id": 24,
#        "image":"https://images.pexels.com/photos/1332275/pexels-photo-1332275.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 4,
#        "menu_name": "Java Housee Breakfast",
#        "description": "A hearty breakfast platter with eggs, bacon, sausages, toast, and more",
#        "prices": 600
#      },
#      {
#        "menu_id": 25,
#        "image":"https://images.pexels.com/photos/725997/pexels-photo-725997.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 4,
#        "menu_name": "Chicken Avocado Wrapp",
#        "description": "Grilled chicken, avocado, lettuce, and mayo wrapped in a tortilla",
#        "prices": 450
#      },
#      {
#        "menu_id": 26,
#        "image":"https://images.pexels.com/photos/806361/pexels-photo-806361.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 4,
#        "menu_name": "Java Cappuccinoh",
#        "description": "Signature cappuccino made with Java House's premium coffee beans",
#        "prices": 250
#      },
#      {
#        "menu_id": 27,
#        "image":"https://images.pexels.com/photos/1123249/pexels-photo-1123249.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 4,
#        "menu_name": "Chocolate Browniee",
#        "description": "Decadent chocolate brownie served with a scoop of ice cream",
#        "prices": 300
#      },
#      {
#        "menu_id": 28,
#        "image":"https://images.pexels.com/photos/6605652/pexels-photo-6605652.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 4,
#        "menu_name": "Greekk Salad",
#        "description": "Fresh salad with cucumbers, tomatoes, olives, and feta cheese",
#        "prices": 350
#      },
#      {
#        "menu_id": 29,
#        "image":"https://images.pexels.com/photos/8753745/pexels-photo-8753745.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 4,
#       "menu_name": "Fried Chicken Comboh",
#        "description": "Crispy fried chicken pieces served with coleslaw and fries",
#        "prices": 450
#      },
#      {
#        "menu_id": 30,
#        "image":"https://images.pexels.com/photos/2233351/pexels-photo-2233351.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 4,
#        "menu_name": "Spicy Wingss",
#        "description": "Succulent chicken wings marinated in spicy sauce",
#        "prices": 350
#      },
#      {
#        "menu_id": 31,
#        "image":"https://images.pexels.com/photos/6607314/pexels-photo-6607314.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 4,
#        "menu_name": "Chicken Burgerss",
#        "description": "Delicious chicken burger with lettuce, mayo, and cheese",
#        "prices": 300
#      },
#      {
#        "menu_id": 32,
#        "image":"https://images.pexels.com/photos/6287539/pexels-photo-6287539.jpeg?auto=compress&cs=tinysrgb&w=1600",
#        "restaurant_id": 3,
#        "menu_name": "Mashed and Gravy",
#        "description": "Creamy mashed potatoes served with rich gravy",
#        "prices": 150
#      }
#    ]

# with app.app_context():
#     menus = []
#     for menu in sample_data30:
#         menu = Menu(**menu)
#         menus.append(menu)
#     db.session.add_all(menus)
#     db.session.commit()