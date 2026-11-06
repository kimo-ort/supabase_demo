import os 
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class ModelContactos():

    def __init__(self) -> None:
        try:
# Esta es la manera mas segura de conectarse a supabase

            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL"),
                os.environ.get("SUPABASE_KEY")
            )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")

    def obtenerContactos(self):
        # *SELECT * FROM contactos;
        response = self.supabase.table("contactos").select("*").execute()
        return response.data
    def buscarContacto(self, id_contacto: int):
        response = self.supabase.table("contactos").select("*").eq("id_contacto", id_cotacto) \
            .execute()
        return response.data
