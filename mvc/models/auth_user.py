from supabase import create_client, Client
from dotenv import load_dotenv

import logging

load_dotenv()

logger = logging.getLogger(__name__)

class AuthUsers:

    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )

        except Exception as error:
            logger.error(f"ERROR 100: {str(error)}")
            print(f"ERROR 100: {str(error)}")

def iniciarSesion(self, email:str, password:str)->str: 
    try:
        response= self.supabase.auth.sign_in_with_password(
             {
                "email":email,
                "password":password
             }
        )

print(f"inicio de sesionn exitoso")





if __name__ == "__main__":
    print("Autenticacion de usuarios")
    objeto = AuthUsers()
    objeto.iniciarSesion("dejah@email.com","123456789"))
