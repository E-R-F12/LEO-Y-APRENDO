from PIL import Image, ImageDraw, ImageFont
import os

# Palabras del Bloque 2 CASA
palabras = [
"PUERTA","VENTANA","MESA","SILLA","CAMA","SOFA","COCINA","BAÑO",
"LAMPARA","ESPEJO","ARMARIO","ALMOHADA","MANTA","ALFOMBRA","CORTINA",
"TOALLA","JABON","DUCHA","FREGADERO","NEVERA","MICROONDAS","HORNO",
"SARTEN","CUCHILLO","CUCHARA","TENEDOR","PLATO","VASO","CEPILLO","ESCOBA"
]

# Crear carpeta automáticamente
ruta = "vocabulario-realista/imagenes/bloque-2-casa"
os.makedirs(ruta, exist_ok=True)

# Colores bonitos para cada tarjeta
colores = ["#ffecd2","#fcb7af","#a1c4fd","#c2e9fb","#d4fc79","#f6d365","#fbc2eb","#a6c0fe"]

for i, palabra in enumerate(palabras):
    # Crear imagen 800x600
    img = Image.new('RGB', (800, 600), color=colores[i % len(colores)])
    draw = ImageDraw.Draw(img)
    
    # Intentar cargar fuente grande, si no hay usa la por defecto
    try:
        font = ImageFont.truetype("arial.ttf", 90)
        font2 = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
        font2 = ImageFont.load_default()
    
    # Dibujar texto centrado
    # Nombre de la palabra grande
    draw.text((400, 250), palabra, fill="#1a2a5a", font=font, anchor="mm")
    draw.text((400, 350), "🏠", fill="#1a2a5a", font=font, anchor="mm")
    draw.text((400, 500), f"{i+1}. {palabra}", fill="#333333", font=font2, anchor="mm")
    
    # Borde
    draw.rectangle([0,0,799,599], outline="#1a5aa8", width=8)
    
    # Guardar con nombre exacto en minúsculas
    nombre_archivo = f"{ruta}/{palabra.lower()}.jpg"
    img.save(nombre_archivo, "JPEG", quality=95)
    print(f"✅ Creada: {nombre_archivo}")

print(f"\n¡Listo! Se crearon {len(palabras)} fotos exactas en {ruta}")
