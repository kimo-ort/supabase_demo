import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')


class InsertarContacto:

    def GET(self):
        return render.insertar_contacto()  # type: ignore

    def POST(self):
        formulario = web.input(nombre="", email="", telefono="")

        modelo = ModelContactos()
        modelo.insertarContacto(formulario.nombre, formulario.email, formulario.telefono)

        return render.contacto_guardado()  # type: ignore