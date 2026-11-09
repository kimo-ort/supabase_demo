import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class ActualizarContacto:

    def GET(self):
        datos = web.input()
        id = datos.id

        modelo = ModelContactos()
        contacto = modelo.ActualizarContacto(id)[0]

        return render.Actualizar_contacto(contacto)