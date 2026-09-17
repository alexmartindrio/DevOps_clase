from app import mensaje
def test_mensaje():
    assert mensaje() == "Hello world DevOps"
    print("Prueba exitosa")

if __name__ == "__main__":
    test_mensaje()
