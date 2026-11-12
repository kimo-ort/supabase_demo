    def POST(self):
        datos = web.input(id=None)

        if datos.id:
            modelo = ModelContactos()
            modelo.borrarContacto(datos.id)

        return render.contacto_borrado()  # type: ignore