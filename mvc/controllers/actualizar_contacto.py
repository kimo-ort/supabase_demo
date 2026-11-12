import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class ActualizarContacto:

    def GET(self):
        datos = web.input(id=None)
        contacto = None

        if datos.id:
            modelo = ModelContactos()
            resultado = modelo.buscarContacto(datos.id)
            if resultado:
                contacto = resultado[0]

        return render.actualizar_contacto(contacto)

    def POST(self):
        datos = web.input(id=None, nombre="", email="", telefono="")

        if datos.id:
            modelo = ModelContactos()
            modelo.actualizarContacto(datos.id, datos.nombre, datos.email, datos.telefono)

        raise web.seeother('/contactos')