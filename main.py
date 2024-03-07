#Utilice Selenium WebDriver para escribir el código y probar la URL  https://www.saucedemo.com/

# 1. vaya a https://www.saucedemo.com/ y busque los nombres de usuario y contraseñas que se muestran en la página.
# 2. Ingrese los detalles en el formulario de inicio de sesión y haga clic en el botón de inicio de sesión.
# 3. Obtenga el título de la página de inicio de sesión y guárdelo en login_header
# 4. Obtenga los titulos de los primeros cinco productos que se muestran en la pagina de inicio de sesion.
# 5. Devuelve la siguiente información en los  datos: nombres de usuario, contraseña, login_header y product_titles
# Nota: asegúrese de automatizar el proceso y no utilizar valores estáticos.


import random
import json
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configurmos la URL del sitio web
url = "https://www.saucedemo.com/"

# Inicializamos el navegador
driver = webdriver.Chrome()  # Asegúrate de tener el controlador de Chrome descargado y configurado

# Paso 1: Ir al sitio web y obtener los nombres de usuario y contraseñas
driver.get(url)

login_credentials_element = driver.find_element(By.ID, "login_credentials")
usernames = login_credentials_element.text.split('\n')[1:]

login_password_element = driver.find_element(By.CLASS_NAME, "login_password")
password = login_password_element.text.split('\n')[1]

# Paso 2: Iniciar sesión con un usuario aleatorio
username = random.choice(usernames)


# Paso 3: Iniciar sesión con el primer usuario y contraseña obtenidos
#
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")
username_input.send_keys(username) #pasamos como parametro el usario tomado aleatoriamente
password_input.send_keys(password)
login_button.click()

# Paso 4: Obtener el título de la página de inicio de sesión
login_header = driver.title

# Paso 5: Obtener los títulos de los primeros 5 productos
product_titles = []
product_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_name") # si deseas que te muestre otra caracteristica solo obtienes el elemento po ejemplo precio "inventory_item_price"
for i in range(min(5, len(product_elements))):
    product_titles.append(product_elements[i].text)

# Paso 5: Devolver la información recopilada
data = {
    "usernames": username,
    "passwords": password,
    "login_header": login_header,
    "product_titles": product_titles
}

# Convertir el diccionario a una cadena JSON
json_data = json.dumps(data)

# Imprimir la información recopilada
print("Información recopilada:")
print(json_data)

# Cerrar el navegador
driver.quit()
