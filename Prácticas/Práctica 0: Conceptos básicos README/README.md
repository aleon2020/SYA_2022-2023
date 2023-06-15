# Ejemplo de fichero README.md
## (CC-BY-NC-SA) Julio Vega

El objetivo de este **fichero README.md de ejemplo** es conocer el uso básico de *MarkDown* para que los estudiantes se familiaricen con este lenguaje.

## 0. Introducción

Las secciones van precedidas de varias almohadillas, según el anidamiento de la sección. Se añade el número de la sección y el título.

## 1. Uso básico

### 1.1. Cursiva y negrita

Para poner un texto en cursiva, se mete este entre asteriscos simples. Por ejemplo, para escribir términos anglosajones como *dashboard* o *upgrade*.

Si quiero poner un texto en negrita, seguiremos la misma sintaxis, pero usando dobles asteriscos, por ejemplo para resaltar alguna palabra **importante**.

### 1.2. Enumerados

Simplemente, hago un listado de ítems, precedidos por su número o posición. Por ejemplo, el siguiente listado:

1. Primer ítem
2. Segundo ítem
3. Y así sucesivamente...

## 2. Incluir texto especial

### 2.1. Snippets

Un *snippet* es un trozo de código, muy útil en el contexto de programación para, por ejemplo, resaltar alguna funcionalidad del programa. En este ejemplo, exponemos un *snippet* en lenguaje Python:

```python
for fila in range(0, len(misFilas)): # recorro todas la filas del vector
    a = procesar (fila) # rellenamos toda la info de la fila "a" actual
    if (a.codigoControl == -1):
        print ("FATAL ERROR al leer fila: " + a.digito1 + " " + a.digito2 + ", " + a.tipo)
    else:
        filaValida = Convertir (a)
```

### 2.2. Instrucciones de Terminal (bash)

Si queremos incluir las instrucciones de Terminal que usamos, por ejemplo, para ejecutar nuestro programa, tenemos el entorno *bash*. Ejemplo:

```bash
make
make install
./miprograma
```

## 3. Incluir recursos

### 3.1. Imágenes

Aquí podemos ver el logo de GitHub:

![alt text](https://github.githubassets.com/images/modules/logos_page/GitHub-Logo.png "Logo de GitHub")

### 3.1. Enlaces

Recordad que podréis acceder a todas las prácticas en nuestro [repo *clases-julio*](https://github.com/clases-julio)
