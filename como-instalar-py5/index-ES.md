# Cómo instalar y empezar a usar py5

[\[Versión en inglés\]](index-EN.md)

<h1 id="toc"/>

### Muy breve resumen

- Para diseñar y experimentar con la programación creativa con Python,<br/>[siga las siguientes instrucciones](https://abav.lugaralgum.com/como-instalar-py5/#1-baixe-e-instale-o-thonny-ide);<br/>
- Si estás en Windows, [descarga y descomprime este archivo](https://www.dropbox.com/scl/fi/2mnhk1k1yj6ab55p02z6q/thonny-4-with-py5-100-windows-portable.zip?rlkey=0du7vkd2nn2etlwftqw69hq1t\&dl=0), abre `thonny.exe` y salta al paso 4*(ejecuta un pequeño ejemplo*)**¡Un problema conocido en Windows**: Si la ruta de la carpeta de Thonny y JDK Java contiene carpetas con nombres acentuados [esto rompe jpype](https://github.com/jpype-project/jpype/issues/1111) y por lo tanto rompe py5.

## ¿Qué es py5?

[**py5**](https://github.com/py5coding) es una librería⚹ que permite utilizar el vocabulario y la infraestructura gráfica de **Processing** junto con la última versión del lenguaje **Python**.

Las bibliotecas son paquetes de código con funciones complementarias ya hechas, desarrolladas de antemano, para ayudar al desarrollo de nuevos programas.

[Processing.org">**Processing**](<http://\<glossary variable=>) es una plataforma de programación libre/abierta muy utilizada por artistas y diseñadores, así como para la enseñanza de la programación en un contexto visual. Con ella se puede escribir software interactivo con los más diversos propósitos e interfaces visuales, así como exportar imágenes de mapa de bits (PNG, JPG), animaciones o archivos vectoriales 2D y 3D (PDF y SVG entre otros). La comunidad disfruta de un rico ecosistema de personas que producen recursos como ejemplos didácticos y bibliotecas de código compartidas libremente.

Processing se basa originalmente en el lenguaje de programación Java, pero hoy en día existen varios proyectos que desarrollan las ideas de Processing con otros lenguajes, como *p5js* con Javascript, *pyp5js* (combinando Python en el navegador, pyodide, y *p5js*), y ahora **py5** con Python 3.

Para usar **py5** necesitarás

- Tener un intérprete de **Python 3** (versión 3.8 o posterior);

- Instalar la librería **py5** y sus dependencias (otras librerías que necesita para funcionar, como JPype);

- Un **Java (JDK)**, que py5 necesita para la infraestructura de dibujo, y tu JPype necesita saber dónde está, a través de la variable JAVA-HOME;

- Un **IDE** (entorno de desarrollo integrado), en pocas palabras, un editor de texto adecuado para el código, que también facilita la ejecución de los programas que escribes. Algunas personas prefieren escribir Python en *Jupyter Notebooks*, eso también está bien pero no es el objetivo de este paso a paso.

La sugerencia aquí es seguir los siguientes pasos:

1. Descargar e instalar el **IDE Thonny** que viene con Python 3.10 o posterior;
2. Instalar el paquete **py5** dentro de *Thonny*;
3. Instalar la extensión (plug-in), **thonny-py5mode**. Cuando se ejecuta por primera vez, el plug-in *thonny-py5mode* instala y configura el **JDK** por ti;
4. Comprueba que todo funciona **ejecutando un pequeño ejemplo**.
5. (Extra) Aprende la diferencia entre el **modo importado** y el **modo módulo**.

Si eso no funciona, otra forma de conseguir todo lo que necesitas es seguir las instrucciones de la [documentación de py5](https://py5coding.org/content/install.html), empezando por instalar una distribución Anaconda o miniconda, que viene con un gestor de paquetes Python y *conda*, para instalar *py5*, y luego instalar también el JDK.

## 1\. Descargar e instalar el IDE Thonny

Comienza instalando el IDE **de** Thonny.

- Para Windows:
  - ¡Intenta [descargar y descomprimir este archivo](https://www.dropbox.com/scl/fi/2mnhk1k1yj6ab55p02z6q/thonny-4-with-py5-100-windows-portable.zip?rlkey=0du7vkd2nn2etlwftqw69hq1t\&dl=0), haz doble clic en thonny `.exe` y podrás saltar al paso 4!
  - o instale ejecutando el instalador [thonny-4.1.3.exe](https://github.com/thonny/thonny/releases/download/v4.1.3/thonny-4.1.3.exe) y continúe con el paso 2.
  - **Un problema conocido en Windows**: Si la ruta de la carpeta de Thonny, y del Java JDK, contiene carpetas con nombres acentuados [esto rompe jpype](https://github.com/jpype-project/jpype/issues/1111) y por lo tanto rompe py5. Si, por ejemplo, tu nombre de usuario tiene acentos, intenta mover Thonny a una carpeta directamente debajo de `C:\.`

- Para MacOS: descarga y ejecuta el instalador [thonny-4.1.3.pkg](https://github.com/thonny/thonny/releases/download/v4.1.3/thonny-4.1.3.pkg)

- Para Linux: ejecute este [script bash que descarga e instala Thonny 4.](https://github.com/thonny/thonny/releases/download/v4.1.3/thonny-4.1.3.bash)1.3

  ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/02-start-splash.png)

## 2\. Instalar la librería *py5*

Una vez abierto Thonny, selecciona *Herramientas >* *Gestionar* *paquetes*... en el menú.****

Busca la librería **py5** y pide que se instale.

## 3\. Instalar el plugin *thonny-py5mode*

Todavía en Thonny, seleccione *Herramientas* > Administrar *plug-ins*... en el menú.****

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.01-manage-plug-ins.png)

Busque el plugin **thonny-py5mode** y pida que se instale.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.02-install-plug-in.png)

Es necesario **reiniciar Thonny después de este paso**, y luego **permitir que el plugin descargue el JDK**.

Una vez reiniciado, debería aparecer un nuevo menú *py5* en la interfaz de Thonny, haga clic en la opción py5 *> Modo importado para py5* y, a continuación, haga clic en Aceptar en la ventana de diálogo.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.01-activate-imported-mode.png)

Al pulsar esta opción por primera vez, el plug-in descargará, extraerá y configurará el JDK por usted (en el directorio user-config de Thonny). Este proceso puede tardar un poco, dependiendo de tu conexión, pero sólo ocurre la primera vez que activas el menú.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.02-download-jdk.png)

Verás este aviso cuando haya terminado.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.03-download-jdk-done.png)

## 4\. Ejecuta un pequeño ejemplo

Si quieres, ejecuta el comando opcional *Apply recommended py5 settings*, que realiza algunos ajustes en tu IDE, incluyendo la activación del temita azul *Kianite*.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/05-apply-recommended-settings.png)

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.01-imported-activated.png)

Ahora lo principal: con la opción de *modo importado* activada en el menú de *py5*, puedes ejecutar el siguiente código usando el botón de la flecha verde o CTRL+R (o COMANDO+R en Mac) .

```python
def setup():
    size(300, 200)
    rect_mode(CENTER)

def draw():
    rect(mouse_x, mouse_y, 10, 10)
```

Si tienes problemas para ejecutarlo, recuerda detener cualquier otra ejecución que aún esté en marcha con el botón rojo de *stop*.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.02-running-sketch.png)

## 5\. Conoce la diferencia entre modo *importado* y modo *módulo*

### ¿Qué es el modo importado *para py5* opción proporcionada por el plug-in *thonny-py5mode*?

Cuando la opción de menú *py5 > Modo* [importado](https://py5coding.org/content/py5\_modes.html#imported-mode) *para py5* está activada, puedes escribir tus programas (que también se llaman *sketches*) de forma simplificada, esto es [modo importado](https://py5coding.org/content/py5\_modes.html#imported-mode). En este "modo" Thonny ejecutará tu código utilizando el py5 *sketch runner*, una herramienta especial que también puede ejecutarse desde la línea de comandos si no estás utilizando Thonny.

**Advertencia:** El modo *importado* no es adecuado para ejecutar código Python que no haga uso de la librería *py5*.

En este "modo importado", el vocabulario de la biblioteca *py5*, es decir, los nombres de las funciones, constantes y variables del sistema (como la posición del ratón), está disponible sin el prefijo `py5` (que es necesario en el *modo módulo*, como veremos más adelante), y su programa se ejecutará automáticamente mediante una función "run_sketch" de la biblioteca *py5*.

Con el *modo importado* activado, también puedes ejecutar sketches [en modo estático](https://py5coding.org/content/py5\_modes.html#static-mode), es decir, los que no tienen animación ni interactividad porque no tienen declarada la función `draw` (). Pero estos necesitan tener `size` () al principio.

### ¿Qué es el modo *módulo* y cómo podemos utilizarlo?

Cuando desactivas la opción de modo *importado* en el menú *py5*, devuelves a Thonny al comportamiento normal para ejecutar cualquier código Python.

En este caso, puedes usar la librería *py5* en [modo módulo](https://py5coding.org/content/py5\_modes.html#module-mode), que es como se manejan la mayoría de las librerías Python, es decir, `importando` la librería al principio con la sentencia `import`, y llamando a sus funciones con el nombre de la librería como prefijo.

```python
import py5

def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)

py5.run_sketch()
```

Ten en cuenta que necesitarás utilizar la línea `import py5` al principio de tu código, la línea py5 `.run_sketch()` al final, así como el prefijo `py5.` para todas las funciones, constantes y variables que ofrece la librería *py5*.

## Referencias útiles para utilizar py5

- [Processing-Python-py5/sumario-referencia-py5.html">Resumen traducido al portugués de la referencia de py5](<https://abav.lugaralgum.com/material-aulas/\<glossary variable=>) y [documentación oficial completa de py5, en inglés](http://py5coding.org/)
- \[Curso de Python para el diseño con py5 en Domestika]\(

[https://www.domestika.org/pt/courses/4307-design-com-python-programacao-para-um-contexto-visual/a_b_a_villares)](https://www.domestika.org/pt/courses/4307-design-com-python-programacao-para-um-contexto-visual/a_b_a_villares)

- Open courseware [Processing-Python-py5/">Introducción a la programación con Python en un contexto visual](<https://abav.lugaralgum.com/material-aulas/\<glossary variable=>) (usando py5)
- py5[Processing.py-cheat-sheet/blob/pt-br/py5/py5\_cc.pdf">quick reference](<https://github.com/villares/\<glossary variable=>) (traducido de "colinha" de Tristan Bunn)
- [ejemplos de py5 en Jupyter Notebooks](https://github.com/py5coding/py5examples)
- [foro py5](https://github.com/py5coding/py5generator/discussions)
- [Processing.org/">Foro de la Fundación Processing](<https://discourse.\<glossary variable=>)

### Agradecimientos

Un agradecimiento especial al creador de *py5*, [Jim](https://ixora.io/), a los mantenedores del IDE [Thonny](https://github.com/thonny/), y a [tabreturn](https://portfolio.tabreturn.com/) que hizo el plug-in *thonny-py5mode*, que hace la instalación y el uso de *py5* mucho más fácil, ¡sus instrucciones en inglés son el punto de partida de estas instrucciones y la fuente de todas las imágenes!

***

Alexandre B A Villares[(abav.lugaralgum.com](https://abav.lugaralgum.com)), [Licencia CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
