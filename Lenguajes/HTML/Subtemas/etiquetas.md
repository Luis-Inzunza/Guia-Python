# Etiquetas

## Indicar la version del HTML

Primero podemos indicar la version del HTML que estamos utilizando, en el momento de creaciond este escrito el mas usado y en web es el HTML5. por lo cual se indica de la siguiente manera ANTES de cualquier otra cosa.

`<!doctype html>`

Esto deberia estar en la primera linea de codigo

## Etiquetas de estructura basica del codigo

### `<html>`

Dentro de estas etiquetas indicamos que vamos a agregar contenido, dicho contenido se encontrara escrito en html.

```html
<!doctype html>
<html>
</html>
```

### `<head>`

Es un tipo de etiqueta que no mostrara nada en el explorador web, si no que permitira archivos del tipo javascript y/o CSS.

Tambien puede ser utilizada para darle alguna inscruccion al explorador para ejecutarla sin mostrarla en la pagina web.

Su posicion va despues de la etiqueta html.

```html
<!doctype html>
<html>
    <head>

    </head>
</html>
```

### `<title>`

Este muestra el titulo de la pestaña de la pagina web y se utiliza dentro de la etiqueta *<head>*
```html
<!doctype html>
<html>
    <head>
        <title> titulo de la pagina </title>
    </head>
</html>
```

### `<body>`

Es el contenido que se mostrara dentro de nuestra pagina web. Esta se coloca normalmente debajo de *<head>* y arriba de *</html>*

```html
<!doctype html>
<html>
    <head>
        <title> titulo de la pagina </title>
    </head>
    <body>Escribiendo en mi pagina </body>
</html>
```

![imagen](/Lenguajes/HTML/Subtemas/pagina.jpg)

## Manipulacion de texto

### `<h#>` (Titulos)  

Con esta etiqueta podemos manipular el tamaño de titulo que queramos que tenga nuestro texto. Tiene la capacidad de tener hasta 6 tipos de tamaño diferente de titulos.

```html
<!doctype html>
<html>
    <head>
        <title> titulo de la pagina </title>
    </head>
    <body>
        <h1>Titulo1</h1>
        <h2>Titulo2</h2>
        <h3>Titulo3</h3>
        <h4>Titulo4</h4>
        <h5>Titulo5</h5>
        <h6>Titulo6</h6>
    </body>
</html>
```
![imagen](/Lenguajes/HTML/Subtemas/titulos.png)

### `<p>` (parrafo)

Se utiliza para crear parrafos y su tamallo de letra es muy cercana a la de **h4**.

```html
<!doctype html>
<html>
    <head>
        <title> titulo de la pagina </title>
    </head>
    <body>
        <h1>Titulo1</h1>
        <h2>Titulo2</h2>
        <h3>Titulo3</h3>
        <h4>Titulo4</h4>
        <h5>Titulo5</h5>
        <h6>Titulo6</h6>
        <p>Hola! soy un parrafo</p>
    </body>
</html>
```
### `<br/>` (salto de linea)

Esta etiqueta se puede ir colocando mediante vas escribiendo para hacer saltos de linea.

```html
<!doctype html>
<html>
    <head>
        <title> titulo de la pagina </title>
    </head>
    <body>
        <h1>Titulo1</h1>
        <h2>Titulo2</h2>
        <h3>Titulo3</h3>
        <h4>Titulo4</h4>
        <h5>Titulo5</h5>
        <h6>Titulo6</h6>
        <p>Hola! soy un parrafo</p>
        <p>Hola! <br /> hice un salto de linea</p>
    </body>
</html>
```

### `<hr>` (linea separadora)

Con esta etiqueta puedes crear una linea que separe tu contanido
```html
<!doctype html>
<html>
    <head>
        <title> titulo de la pagina </title>
    </head>
    <body>
        <h1>Titulo1</h1>
        <h2>Titulo2</h2>
        <h3>Titulo3</h3>
        <h4>Titulo4</h4>
        <h5>Titulo5</h5>
        <h6>Titulo6</h6>
        <hr>
        <p>Hola! soy un parrafo</p>
        <p>Hola! <br /> hice un salto de linea</p>
    </body>
</html>
```
![imagen](/Lenguajes/HTML/Subtemas/linea.png)
