import web

from mvc.controllers.index import index
from mvc.controllers.contactos import contactos

urls = (
   '/','Index'
   '/contactos','mvc.controllers.contactos.contactos',

)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()