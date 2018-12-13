from matrix_client.api import MatrixHttpApi

matrix = MatrixHttpApi("https://matrix.agetic.gob.bo", token="MDAxYmxvY2F0aW9uIGFnZXRpYy5nb2IuYm8KMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDJhY2lkIHVzZXJfaWQgPSBAamFydGVhZ2E6YWdldGljLmdvYi5ibwowMDE2Y2lkIHR5cGUgPSBhY2Nlc3MKMDAyMWNpZCBub25jZSA9ICpaY0x5ejFQejdvZyNBQU8KMDAyZnNpZ25hdHVyZSDhdBimdZFikEmjal8DmpJUawJUPUtB99-H-rLA-MbQVgo")
# response = matrix.send_message("!hDGPHqSBhpdJWNqdPI:agetic.gob.bo", "Hola mundo")
# print(matrix.get_room_messages('!hDGPHqSBhpdJWNqdPI:agetic.gob.bo','MDAxYmxvY2F0aW9uIGFnZXRpYy5nb2IuYm8KMDAxM2lkZW50aWZpZXIga2V5CjAwMTBjaWQgZ2VuID0gMQowMDJhY2lkIHVzZXJfaWQgPSBAamFydGVhZ2E6YWdldGljLmdvYi5ibwowMDE2Y2lkIHR5cGUgPSBhY2Nlc3MKMDAyMWNpZCBub25jZSA9ICpaY0x5ejFQejdvZyNBQU8KMDAyZnNpZ25hdHVyZSDhdBimdZFikEmjal8DmpJUawJUPUtB99-H-rLA-MbQVgo','f'))

# El token para el inicio es None 
# TODO: ahora lo que me falta es ir preparando la clase con los metodos necesarios
# y desarrollar la interfaz grafica
print(matrix.get_room_messages('!hDGPHqSBhpdJWNqdPI:agetic.gob.bo',None,'b'))

# print(matrix.join_room('!hDGPHqSBhpdJWNqdPI:agetic.gob.bo'))
