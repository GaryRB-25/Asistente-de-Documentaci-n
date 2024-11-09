import openai
import os

# Establece tu clave API (esto debe estar configurado en tu entorno, no la pongas directamente en el código)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Realizar la solicitud a la API de OpenAI para generar la documentación
response = openai.Completion.create(
    engine="text-davinci-003",  # Usa el modelo más adecuado
    prompt="Genera una documentación detallada sobre el proyecto 'Asistente de Documentación' en Python.",
    max_tokens=150  # Establece un número adecuado de tokens
)

# Mostrar la respuesta generada (esto es para ver el contenido en la consola)
print(response.choices[0].text.strip())

# Guardar la documentación en un archivo de texto
with open('C:/Users/User/Desktop/Asistente-de-Documentaci-n/documentacion_generada.txt', 'w') as file:
    file.write(response.choices[0].text.strip())  # Guardamos el texto generado en el archivo
print("Archivo generado: documentacion_generada.txt")
