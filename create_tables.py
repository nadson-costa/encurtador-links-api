from app.database import engine, Base
from app.models.url import URL

def main():
    print("--- Criando tabelas no banco de dados ---")
    Base.metadata.create_all(engine)
    print("--- TABELAS CRIADAS COM SUCESSO! ---")

if __name__ == "__main__":
    main()