import web
from mvc.controllers.index import index
from mvc.models.models_contactos import contactos

render=web.template.render('mvc/views', base= 'template')

class Contactos:

    def GET(self):

model_contactos = ModelContactos()
print(model_contactos.obtenerContactos())

        return render.contactos()