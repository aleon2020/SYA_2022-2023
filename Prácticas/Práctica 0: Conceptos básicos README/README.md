# Ejemplo de fichero README.md
## (CC-BY-NC-SA) Julio Vega

The purpose of this **sample README.md file** is to introduce students to the basics of *MarkDown* so they can become familiar with the language.

## 0. Introduction

Sections are preceded by several hash marks, depending on the nesting of the section. The section number and title are added.

## 1. Basic Use

### 1.1. Italics and Bold

To italicize text, enclose it between single asterisks. For example, to write Anglo-Saxon terms like *dashboard* or *upgrade*.

If I want to make text bold, we'll follow the same syntax, but use double asterisks, for example to highlight an **important** word.

### 1.2. Enumerated

I simply make a list of items, preceded by their number or position. For example, the following list:

1. First item
2. Second item
3. And so on...

## 2. Including special text

### 2.1. Snippets

A snippet is a piece of code, very useful in a programming context, for example, to highlight a program's functionality. In this example, we present a snippet in Python:

```python
for fila in range(0, len(misFilas)): # recorro todas la filas del vector
    a = procesar (fila) # rellenamos toda la info de la fila "a" actual
    if (a.codigoControl == -1):
        print ("FATAL ERROR al leer fila: " + a.digito1 + " " + a.digito2 + ", " + a.tipo)
    else:
        filaValida = Convertir (a)
```

### 2.2. Terminal Commands (bash)

If we want to include the Terminal commands we use, for example, to run our program, we have the *bash* environment. Example:

```bash
make
make install
./miprograma
```

## 3. Including Resources

### 3.1. Images

Here we can see the GitHub logo::

![alt text](https://github.githubassets.com/images/modules/logos_page/GitHub-Logo.png "Logo de GitHub")

### 3.1. Links

Remember that you can access all the practices on our [repo *clases-julio*](https://github.com/clases-julio)
