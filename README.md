# CoderHouse_PreEntrega1

Primera Entrega: Pablo Blanco - CODERHOUSE

Se presenta un menu con 5 opciones:
    - Crear Base: esta función verifica si la base existe y sino la crea vacía
    
    - Leer Base: verifica que la base exista, en tal caso muestra el detalle de usuarios/contraseñas guardados o la leyenda de que la base existe pero está vacía.

    - Alta Usuario: en caso qe la base exista, permite agregar un nuevo usuario/contraseña a la base verificando que el nuevo usuario no haya sido dado de alta previamente.

    - Login: si la base existe y hay usuarios dados de alta, permite simular un login identificando el usuario y comparando con la contraseña guardada.

    - Salir: finaliza la ejecución

Funciones definidas:

- def pausa(): esta función introduce una pausa hasta que se presione la barra espaciadora.
- def crearBase(): esta función valida si existe la base y sino la crea vacía.
- def abrirBase(): abre la base y retorna los datos almacenados en forma de diccionario.
- def existeBase(): verifica si la base existe, devolviendo True o False según coresponda.
- def leerBase(): verifica si existe la base y si no está vacía. Si no es así, muestra los datos almacenados.
- def alta(): verifica si la base existe. En tal caso, permite añadir usuario y contraseña nuevos para ser almacenados, verificando duplicidad de usuarios.
- def login(): verifica que la base exista y haya usuarios almacenados. Entonces, permite simular un login verificando primero la existencia del usuario y luego, si el usuario existe, que la contraseña coincida con la almacenada.
