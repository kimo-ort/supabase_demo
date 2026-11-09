import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class VerContacto:

    def GET(self):
        datos = web.input(id=None)
        contacto = None

        if datos.id:
            modelo = ModelContactos()
            resultado = modelo.buscarContacto(datos.id)
            if resultado:
                contacto = resultado[0]

        return render.ver_contacto(contacto)