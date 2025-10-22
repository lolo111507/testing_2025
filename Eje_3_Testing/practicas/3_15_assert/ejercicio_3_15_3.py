# ejercicio_2_1.py
"""
Completa el sistema de inventario usando ASSERT y TRY/EXCEPT
- Usa ASSERT para validaciones que DEBEN cumplirse
- Usa TRY/EXCEPT para manejar errores de conversión
"""

def agregar_producto(nombre, precio_str, stock_str):
    try:
        # Convierte precio y stock a números (puede fallar)
        precio = float(precio_str)
        stock = int(stock_str)
        
        # TU CÓDIGO AQUÍ - Agrega asserts para:
        # ejercicio_2_1.py
        """
        Completa el sistema de inventario usando ASSERT y TRY/EXCEPT
        - Usa ASSERT para validaciones que DEBEN cumplirse
        - Usa TRY/EXCEPT para manejar errores de conversión
        """


        def agregar_producto(nombre, precio_str, stock_str):
            try:
                # Convierte precio y stock a números (puede fallar)
                precio = float(precio_str)
                stock = int(stock_str)

                # Validaciones obligatorias
                assert isinstance(nombre, str) and nombre.strip() != "", "El nombre no puede estar vacío"
                assert precio > 0, "El precio debe ser mayor que 0"
                assert stock >= 0, "El stock no puede ser negativo"

                print(f"✅ Producto agregado: {nombre}, ${precio}, Stock: {stock}")
                return True

            except ValueError as e:
                print(f"❌ Error de conversión: {e}")
                return False
            except AssertionError as e:
                print(f"⚠️ Error de validación: {e}")
                return False


        # Pruebas:
        if __name__ == "__main__":
            print("📦 Probando sistema de inventario:")

            agregar_producto("Laptop", "1000", "5")      # ✅ Válido
            agregar_producto("", "1000", "5")            # ❌ Nombre vacío
            agregar_producto("Mouse", "-10", "5")        # ❌ Precio negativo
            agregar_producto("Teclado", "50", "cinco")   # ❌ Error conversión
