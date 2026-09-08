from flask import Flask

app = Flask(__name__)

@app.route("/usuario/<nombre>")
def perfil_usuario(nombre):
    return f"Perfil de: <strong>{nombre}</strong>"

@app.route("/post/<id>")
def ver_post(id):
    return f"Mostrando el post: <strong>{id}</strong>"

@app.route("/categoria/<categoria>/<producto>")
def productos (categoria, producto):
    return f"Categoria: {categoria}, Producto: {producto}"

#2 rutas 
@app.route("/post/<int:post_id>")
def post_por_id(post_id):
    return f"Post ID: {post_id} => Tipo: {type(post_id).__name__}"

@app.route("/archivo/<path:ruta_archivo>")
def descargar_archivo(ruta_archivo):
    return f"Descargando: {ruta_archivo}"

if __name__ == '__main__':
    app.run(debug=True)