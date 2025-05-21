import pandas as pd
import qrcode
import os

# Carga del archivo CSV
df = pd.read_csv('Invitados.csv')

# Crea la carpeta de salida
os.makedirs('invitados', exist_ok=True)

# ✅ URL base de GitHub Pages
BASE_URL = "https://lizethdamian.github.io/xvMarlene18Oswaldo/invitados/"


# Generar QR y HTML por invitado
for _, row in df.iterrows():
    nombre = row['Familia/Nombre'].strip().replace(" ", "_")
    mesa = row['Mesa']
    invitados = row['Invitados ']
    file_name = f"{nombre}.html"
    qr_url = f"{BASE_URL}{file_name}"

    # Crear código QR
    img = qrcode.make(qr_url)
    qr_path = f"invitados/{nombre}.png"
    img.save(qr_path)

    with open(f"invitados/{file_name}", "w", encoding='utf-8') as f:
        f.write(f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Invitación para {row['Familia/Nombre']}</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <div class="ticket">
        <h1>15 años Marlene<br>18 años Oswaldo</h1>
        <h2>¡Bienvenido(a), {row['Familia/Nombre']}!</h2>
        
        <p><strong>Mesa:</strong> {mesa}</p>
        <p><strong>Invitados incluidos:</strong> {invitados}</p>
        <p><strong>La misa iniciará a las 8:00 p.m.</strong></p>
        <p><strong>Ubicación:</strong> Salón de Eventos Sociales Mirage, Estado de México</p>
        <p><a href="https://g.co/kgs/URTYSoT" target="_blank">
        📍 Ver en Google Maps
        </a></p>
        
        <div class="qr-section">
            <img src="{nombre}.png" alt="Código QR">
            <p><strong>Presenta este código al ingresar al salón</strong></p>
        </div>
    </div>
</body>
</html>""")
