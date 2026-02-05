from flask import Flask, render_template

app = Flask(__name__)

# Ruta Principal
@app.route('/')
def index():
    return render_template('index.html', breadcrumb=["Inicio"])

# Ruta Sistema de Gestión Ambiental
@app.route('/sistema-ambiental')
def sistema():
    return render_template('sistema.html', breadcrumb=["Inicio", "Sistema de Gestión Ambiental"])

# Ruta Futuro del Planeta
@app.route('/futuro')
def futuro():
    return render_template('futuro.html', breadcrumb=["Inicio", "Futuro del Planeta"])

# Ruta Las 3 R
@app.route('/tres-r')
def tres_r():
    return render_template('tres_r.html', breadcrumb=["Inicio", "Las 3 R"])

# Ruta Normatividad UTNG
@app.route('/normas-utng')
def normas():
    return render_template('normas.html', breadcrumb=["Inicio", "Normatividad UTNG"])

if __name__ == '__main__':
    app.run(debug=True)