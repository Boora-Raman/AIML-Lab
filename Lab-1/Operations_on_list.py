fruits = ["apple", "banana", "cherry", "date"]
print("Original list:", fruits)
first_fruit = fruits[0]
second_fruit = fruits[1]
print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
fruits[1] = "blueberry" 
print("Modified list:", fruits)
fruits.append("elderberry")  
print("List after adding an element:", fruits)
fruits.remove("cherry")  
print("List after removing an element:", fruits)
length_of_list = len(fruits)
print("Length of the list:", length_of_list)
fruits.sort()
print("List sorted in ascending order:", fruits)
fruits.sort(reverse=True)
print("List sorted in descending order:", fruits)