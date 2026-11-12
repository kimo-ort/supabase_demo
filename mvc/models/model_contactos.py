import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos():

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL"),
                os.environ.get("SUPABASE_KEY")
            )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")

    def obtenerContactos(self):
        response = self.supabase.table("contactos").select("*").execute()
        return response.data

    def buscarContacto(self, id_contacto):
        response = self.supabase.table("contactos").select("*").eq("id", id_contacto).execute()
        return response.data

    def insertarContacto(self, nombre, email, telefono):
        response = self.supabase.table("contactos").insert({
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }).execute()
        return response.data

    def actualizarContacto(self, id_contacto, nombre, email, telefono):
        response = self.supabase.table("contactos").update({
            "nombre": nombre,
            "email": email,
            "telefono": telefono
        }).eq("id", id_contacto).execute()
        return response.data

    def borrarContacto(self, id_contacto):
        response = self.supabase.table("contactos").delete().eq("id", id_contacto).execute()
        return response.data