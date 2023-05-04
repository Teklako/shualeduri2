#დავალება1
import sqlite3

conn = sqlite3.connect('survey.sqlite')
c = conn.cursor()
c.execute("SELECT COUNT(*) FROM Students WHERE SelfStudyHour < 2")
result = c.fetchone()[0]
print(f"სტუდენტების რაოდენობა, რომლებიც დღეში 2 საათზე ნაკლებს ხარჯავენ დამოუკიდებლად სწავლაში: {result}")
def count_students(device, age):
    c.execute("SELECT COUNT(*) FROM Students WHERE Device = ? AND Age = ?", (device, age))
    result = c.fetchone()[0]
    return result

device = "Smartphone"
age = 20
count = count_students(device, age)
print(f"სტუდენტების რაოდენობა, რომლებიც იყენებენ {device} და არიან {age} წლის: {count}")
c.execute("INSERT INTO Students (ID, Age, OnlineClassTime, Device, SelfStudyHour, FitnessTime, Sleep, SocialMedia, SocialMediaPlatform) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",(480, 25, 50, "Laptop", 5, 3, 8, 2, "Instagram"))

conn.commit()
conn.close()

#დავალება2
import json

with open('data.json') as file:
    data = json.load(file)

print(data['person']['address'])

friends = [(friend['name'], friend['surname']) for friend in data['person']['friends']]
print(friends)

keys = [key for key in data.keys() if isinstance(data[key], dict)]
print(f"Fields: {', '.join(keys)}")
selected_field = input("Enter the name of the field you want to view: ")
if selected_field in data:
    print(data[selected_field])
else:
    print(f"No field named '{selected_field}' found in the data.")

file.close()
