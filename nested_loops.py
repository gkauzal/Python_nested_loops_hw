#1. feladat
def hwFirst(matrix):
    counter = 0
    for i in matrix:
        for j in i:
            counter += j
    return counter


print(
    hwFirst([[1, 1, 1, 2, 1], [2, 3, 2, 2, 2], [3, 3, 2, 3, 3],
             [4, 4, 4, 3, 4]]))


#2. feladat
def hwSecond(car_dic):
    for i in car_dic:
        if i['passengerQty'] < len(i['passengers']):
            print("A(z) " + i['type'] + " típusú autóban túl sok az utas!")


hwSecond([
    {
        "price": 1549,
        "passengerQty": 4,
        "currency": "EUR",
        "type": "Kia",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 1954,
        "passengerQty": 5,
        "currency": "EUR",
        "type": "Suzuki",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 2544,
        "passengerQty": 5,
        "currency": "USD",
        "type": "Opel",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 2544,
        "passengerQty": 2,
        "currency": "USD",
        "type": "Opel",
        "transmission": "manual",
        "passengers": ["Gabor", "Timea", "Miklos"]
    },
    {
        "price": 9542,
        "passengerQty": 4,
        "currency": "USD",
        "type": "Ford",
        "transmission": "automatic",
        "passengers": ["Gabor", "Timea", "Miklos"]
    },
])


#3. feladat
def hwThird(car_dic):
    usd_changer = 1.1
    for i in car_dic:
        if i['currency'] == 'EUR':
            i['price'] = int(i['price'] * usd_changer)
            i['currency'] = 'USD'
        print("A(z) " + i['type'] + " típusú autó ára:" + str(i['price']) +
              i['currency'])


hwThird([
    {
        "price": 1549,
        "passengerQty": 4,
        "currency": "EUR",
        "type": "Kia",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 1954,
        "passengerQty": 5,
        "currency": "EUR",
        "type": "Suzuki",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 2544,
        "passengerQty": 5,
        "currency": "USD",
        "type": "Opel",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 2544,
        "passengerQty": 2,
        "currency": "USD",
        "type": "Opel",
        "transmission": "manual",
        "passengers": ["Gabor", "Timea", "Miklos"]
    },
    {
        "price": 9542,
        "passengerQty": 4,
        "currency": "USD",
        "type": "Ford",
        "transmission": "automatic",
        "passengers": ["Gabor", "Timea", "Miklos"]
    },
])


#4. feladat
def hwFourth(persons, restaurants):
    for person in persons:
        for restaurant in restaurants:
            print(person + " eats " + restaurant)


persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Japanese", "American", "Mexican", "French"]

hwFourth(persons, restaurants)


#5. feladat
def hwFifth(numbers):
    for i in numbers:
        i.append(i[0] + i[1])
    return numbers


print(hwFifth([[4, 5], [7, 4], [2, 5], [9, 4]]))
