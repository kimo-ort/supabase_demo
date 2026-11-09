import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class VerContacto:

    def GET(self):
        datos = web.input()
        id_contacto = datos.id

        modelo = ModelContactos()
        contacto = modelo.buscarContacto(id_contacto)[0]

        return render.ver_contacto(contacto)