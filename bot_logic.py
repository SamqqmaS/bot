# bot_logic.py
import random
import string

# Función para generar una contraseña aleatoria
def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Función para obtener un emoji aleatorio
def get_random_emoji():
    emojis = ['😀', '😁', '😂', '🤣', '😃', '😄', '😅', '😆', '😇', '😍', '🥺', '🤔', '😎', '😋']
    return random.choice(emojis)

# Función para lanzar una moneda (cara o cruz)
def lanzar_moneda():
    return random.choice(['Cara', 'Cruz'])
