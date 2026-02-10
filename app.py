from flask import Flask, render_template, request # <--- Agregamos request
import requests # <--- Agregamos la librería requests

app = Flask(__name__)

# --- RUTAS ANTERIORES (NO CAMBIAN) ---
@app.route('/')
def index():
    return render_template('index.html', breadcrumb=["Inicio"])

@app.route('/sistema-ambiental')
def sistema():
    return render_template('sistema.html', breadcrumb=["Inicio", "Sistema de Gestión Ambiental"])

@app.route('/normas-utng')
def normas():
    return render_template('normas.html', breadcrumb=["Inicio", "Normatividad UTNG"])

@app.route('/futuro')
def futuro():
    return render_template('futuro.html', breadcrumb=["Inicio", "Futuro del Planeta"])

@app.route('/tres-r')
def tres_r():
    return render_template('tres_r.html', breadcrumb=["Inicio", "Las 3 R"])

# --- NUEVA RUTA PARA EL MAPA (REQUISITO DEL PDF) ---
@app.route('/puntos-verdes', methods=['GET', 'POST'])
def mapa():
    coords = None
    error = None
    lugar_buscado = ""

    # Lógica del PDF: Consumir API desde Python cuando se envía el formulario
    if request.method == 'POST':
        lugar_buscado = request.form.get('lugar')
        if lugar_buscado:
            # Cabeceras requeridas por Nominatim (Política de uso)
            headers = {'User-Agent': 'Proyecto-Escolar-UTNG-MedioAmbiente'}
            url = "https://nominatim.openstreetmap.org/search"
            params = {
                'q': lugar_buscado,
                'format': 'json',
                'limit': 1
            }
            
            try:
                response = requests.get(url, params=params, headers=headers)
                data = response.json()
                
                if data:
                    coords = {
                        'lat': data[0]['lat'],
                        'lon': data[0]['lon'],
                        'display_name': data[0]['display_name']
                    }
                else:
                    error = "No se encontró el lugar especificado."
            except Exception as e:
                error = "Error al conectar con el servicio de mapas."

    return render_template('mapa.html', 
                           breadcrumb=["Inicio", "Localizador de Zonas"], 
                           coords=coords, 
                           error=error,
                           lugar_buscado=lugar_buscado)

if __name__ == '__main__':
    app.run(debug=True)