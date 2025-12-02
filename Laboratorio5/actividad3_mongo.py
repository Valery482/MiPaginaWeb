from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Laboratorio5"]
coleccion = db["Estudiantes"]

coleccion.insert_many([
    {"nombre": "Juan", "edad": 20, "ciudad": "Bogotá"},
    {"nombre": "Ana", "edad": 22, "ciudad": "Medellín"},
    {"nombre": "Luis", "edad": 19, "ciudad": "Cali"}
])

print("Todos los estudiantes:")
for est in coleccion.find():
    print(est)

print("Estudiantes de Medellín:")
for est in coleccion.find({"ciudad": "Medellín"}):
    print(est)

print("Estudiantes mayores de 20 años:")
for est in coleccion.find({"edad": {"$gt": 20}}):
    print(est)
