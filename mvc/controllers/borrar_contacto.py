import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class BorrarContacto:

    def GET(self):
        datos = web.input(id=None)
        contacto = None

        if datos.id:
            modelo = ModelContactos()
            resultado = modelo.buscarContacto(datos.id)
            if resultado:
                contacto = resultado[0]

        return render.borrar_contacto(contacto)

    def POST(self):
        datos = web.input()
        id = datos.id

        modelo = ModelContactos()
        modelo.borrarContacto(id)

        raise web.seeother('/contactos')