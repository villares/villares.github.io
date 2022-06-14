----

[[versão em português](index.md)]

# How to install py5

- TL:DR; To draw and experiment some creative coding with Python [follow the instructions below](https://abav.lugaralgum.com/como-instalar-py5/index-EN.html#1-download-and-install-the-thonny-ide).

## What's this?

[py5](https://github.com/py5coding) is a <ins title="Libraries are packages of complementary software functions made by other people to help you develop your own programs" style="text-decoration:underline; text-decoration-style: dotted;">library</ins> that allows us to use the vocabulary and graphical infrastructure of Processing with the Python programming language (Python 3).

[Processing](http://processsing.org/) is a Free and Open Source (FLOSS) programming platform started in 2001 by Casey Reas e Ben Fry, widely used by artists and designers, as well as for teaching programming in a visual context. It allows you to generate interactive software with the most diverse purposes and visual interfaces, as well as exporting bitmap/raster images (like PNG and JPG), animations or 2D and 3D vector files (like PDF and SVG, among others). The community enjoys a rich ecosystem of people who produce resources such as teaching examples and freely shared code libraries.

Processing is originally based on the Java programming language, but today there are several projects that develop Processing ideas with other languages, such as *p5js* with Javascript, *Processing Python mode* (inside the Processing IDE) using Python 2.7 (Jython), and now *py5* with Python 3 (CPython).

To use *py5* you will need:

- A **Python 3** interpreter (version 3.8 or later);

- Install the **py5 library package** and its dependencies (other libraries it needs to work, such as JPype);

- A **Java** (**JDK-17**), which *py5* needs for the drawing infrastructure, and JPype needs to know where it is, looking at the JAVA-HOME environment variable;

- Optionally, an **IDE** (Integrated Development Environment), simply put, a code-appropriate text editor that lets you run the programs you write. Some people like to use *py5* on *Jupyter Notebooks*.

The suggestion here is to start by installing a specific version of the **Thonny IDE** (which comes with Python 3.8 or greater) and then an extension (plug-in), **thonny-py5mode** that will install and configure the JDK for you!

>  Another way to get everything you need, if these steps bellow fail, is to follow the instructions at the [py5 documentation](https://py5.ixora.io/content/install.html), starting with installing *miniconda*, which comes with Python and the *conda* package manager, to install *py5*, and then following the instructions for installing and setting up *Java* (*JDK-17*).

## 1. Download and install the Thonny IDE

You'll need version 3.3.7-alt (because of the version of Python it comes with).

- For Windows: [thonny-3.3.7-alt.exe](https://github.com/thonny/thonny/releases/download/v3.3.7/thonny-3.3.7-alt.exe)

- For MacOS: [thonny-3.3.7-alt.pkg](https://github.com/thonny/thonny/releases/download/v3.3.7/thonny-3.3.7-alt.pkg)

- For Linux: [thonny-3.3.7-x86_64- alt.tar.gz](https://github.com/thonny/thonny/releases/download/v3.3.7/thonny-3.3.7-x86_64-alt.tar.gz)

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/02-start-splash.png)

## 2. Install the *thonny-py5mode* plug-in

Ppen, select *Tools > Manage plug-ins...* from the menu…

![](https://lh5.googleusercontent.com/7QqZEos2zyHAKo_NYdcQsIffMfWX4A7lntYblHuZohfvAje_cjh3MkXKAw4N7H4XmAhB2_czHxsCvbLlQeY3g03hmnH-vBf9KGOlbEPptoZqirNgaAXwNLACdcB-ejhpYbxNacId3FfXv58_rA) 

Search for **thonny-py5mode** and click on the install button.

 ![](https://lh6.googleusercontent.com/Rre5zRvlhX93ZO8zW677ivLiTPUijAMNsew5rE7jZWMo6gyP0Hda9AEbeb_5QiEPuvNe---VuqBAvjpEG9oHupDhe3WGA7BvCd5Nz5OWy5CdxV0NRZiZnt0h-s5tI00EPWC14LivuQJzK7ROww) 

You need to __restart Thonny after this step!!!__

## 3. Allow the plug-in to download the JDK

Once restarted, a new *py5* menu should appear in Thonny's interface, click on the *py5 > Imported mode for py5* menu option and then click OK in the dialog window that appears.

![](https://lh3.googleusercontent.com/V9EJuIoI6s2qghaj31gRPWidWbz3bv_386mXP_In706KrYfCrJ8UaSGxZOuOUtBORRYMCnOCFanrebCGK5iI-MM4cZz3E846wJY2zi0l8ZggFTvXAuLYOjK75Cy2eackqj3m7ai1ov_IYbGdMg) 

When you first select this, the plug-in will download, extract and configure the JDK for you (in Thonny's user-config directory). This process can be quite lengthy depending on your connection, but it only happens the first time you select the menu option.

**Thonny's window will appear frozen** as it downloads and configures the JDK, don't despair!**

![](https://lh5.googleusercontent.com/3cW4nEEMWdwGf3lFSYLOLahmqWBgP7NfuAonN2Rd0IyeH9IH44Fe_aENvHxp_OTwIikhiud41L3nG0Q1KRRFj8Tou7EN9YdMkYmOgQxe2pBS6dRkNZq7AfqqS-b84x-WfDlLJ__ACiMw30tW-A) 

A message will appear when it is finished.

![](https://lh4.googleusercontent.com/LX3nhpXQSUvBK_VIKwf6gbkOSgSVO30_hi-sNLU6AtxH8scDFpUAcjUa8AuH1OYrQWuOJrMp-f1hViDKNG3wABlOMJHKGV5qzq6jFWkcuVPxLErk3FsBcO-uV-gA6H61wZ-w8oNZ5OQxcM7Bkw)

An optional step: The *Apply recommended py5 settings* makes a few configuration tweaks to your IDE, including enabling the blue Kianite theme! 

![](https://lh5.googleusercontent.com/TqdRTzve0Z18jnT-LrdIsK0SHdaynaL1SmDc5c3wx58jeMWk5neiCmvIP3vkHMMew5FCZ0nqBTY3HFdW9T6TFlAhE_TQYsASlIx9yYLGNNr9tbhcQwTrVN4QtmvyEvmzv5jAQ7zsNVrc2Egc4A)

## 4. Run a small example, learn the difference between *imported mode* and *module mode*, that's it!

With the *py5 > imported mode for py5* option on, you can run the following code using the green arrow button or CTRL+R (COMMAND+R on a Mac). Creative coders usually call their programs sketches.

```python
def setup():
    size(300, 200)
    rect_mode(CENTER)

def draw():
    square(mouse_x, mouse_y, 10)
```

If you have trouble geting your program to execute, try stopping any other execution that is still running.

![](https://lh6.googleusercontent.com/8V821bvVbtGfoqNZq4UNGWtdKS0F1BcXHFwrghG-6FmRWA2XA3N3h5mO6ltWI1J_SCklXJ2Nj1l5142njaf3DVA-U3ICt2zvRcSVy9w1ESm7F_spgfA6yjCLm6bkiosLzN92eo9sT3-fmRcc3Q)

### What is *imported mode*?

When the *py5 > Imported mode for py5* option is on, you can write your sketches in a simplified maner, called [imported mode](https://py5.ixora.io/content/py5_modes.html#imported-mode), and Thonny will run your code using the *py5 sketch runner*, a special tool that can also be called from the command line if you are not using Thonny.

In *imported mode* the vocabulary of *py5*, that is, the names of functions, constants and system variables (such as the mouse position), are available without the `py5.` prefix, and your program will be automatically executed by a `run_sketch` function from *py5*.

**This is not appropriate for executing Python code that doesn't make use of the py5 library!**

With imported mode on, you can also run [static mode](https://py5.ixora.io/content/py5_modes.html#static-mode) sketches, that is, programs without animation or interactivity because they do not have a `draw()` function defined.

### What is *module mode*?

When you disable the *imported mode for py5* menu option, you return Thonny to the normal behavior for executing any Python code.

In this case, you can use *py5* in [module mode](https://py5.ixora.io/content/py5_modes.html#module-mode), which is how most Python libraries are handled, i.e. importing the library at the beginning of the program with `import`, and calling its functions with the library name as a prefix.

```python
import py5

def setup():
    py5.size(300, 200)
    py5.rect_mode(py5.CENTER)__

def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)

py5.run_sketch()
```

Note that you will need to use `import py5` at the beginning of your code, and `py5.run_sketch()` at the end, as well as the `py5.` prefix for all functions, constants and variables offered by the *py5* library.

## Useful references for using py5

- [tabreturn's py5 quick reference](https://github.com/tabreturn/processing.py-cheat-sheet/blob/pt-br/py5/py5_cc.pdf)

- [py5 forum](https://github.com/py5coding/py5generator/discussions)

- [official py5 documentation py5](http://py5.ixora.io/)

- [examples in Jupyter Notebooks](https://github.com/py5coding/py5examples)

- [Processing Foundation Forum](https://discourse.processing.org/)

### Acknowledgments

Very special thanks to [Jim](twitter.com/py5coding), creator of py5, the maintainers of [Thonny IDE](http://twitter.com/thonnyIDE), and [tabreturn](https://twitter.com/tabreturn) who made the *thonny-py5mode* plugin, which makes installing and using py5 much easier, most of the step-by-step part and all the images came from the installing intructions at his page, I just added some context and comments!

---

Alexandre BA Villares ([abav.lugaralgum.com](https://abav.lugaralgum.com/)), [CC-BY-NC-SA-4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**
