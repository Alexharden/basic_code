fruits = ["apple", "orange", "apple", "banana", "apple"]
fruit = "apple"
print("刪除前的fruits", fruits)
while fruit in fruits:
    fruits.remove(fruit)
print("刪除後的fruits", fruits)
