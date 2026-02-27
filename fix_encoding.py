import os

filepath = 'index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

reps = {
    'Ã¡': 'á', 'Ã©': 'é', 'Ã­': 'í', 'Ã³': 'ó', 'Ãº': 'ú',
    'Ã±': 'ñ', 'Ã': 'Á', 'Ã‰': 'É', 'Ã\x8d': 'Í', 'Ã“': 'Ó',
    'Ãš': 'Ú', 'Ã‘': 'Ñ', 'Â¿': '¿', 'Â¡': '¡', 'Ã¯': 'ï', 'Ã¼': 'ü'
}

for k, v in reps.items():
    content = content.replace(k, v)

# Escribir con codificación utf-8 explícita
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Encoding fix complete.")
