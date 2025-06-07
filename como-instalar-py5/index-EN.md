# How to install and start using py5

[[versão em português](index.md)]  [[version en español ](index-ES.md)]

### TL:DR;

- To draw and experiment some creative coding with Python [follow the instructions below](https://abav.lugaralgum.com/como-instalar-py5/index-EN.html#1-download-and-install-the-thonny-ide).<br/>

- If you are on Windows, try to [download and unzip this "portable Thonny" package](https://github.com/villares/thonny-portable-with-py5/releases/download/2025-05-28/thonny-417-with-py5-windows-portable.zip), double-click `thonny.exe` and skip to step 4!<br/>

 <sub>**Known solved issues**: Package manager and plug-in manager panels are broken on Thonny 4.1.6, and earlier versions, due to PyPI recent changes. Thonny 4.1.7 fixes it, and py5 0.10.6 (with jpype 1.5.2) should solve non-ASCII path issues!</sub>
  
## What's this?

[py5](https://github.com/py5coding) is a library<sup>⚹</sup> that allows us to use the vocabulary and graphical infrastructure of Processing with the Python programming language (Python 3).

⚹ <sub>Libraries are packages of complementary software functions made by other people to help you develop your own programs.</sub>

[Processing](http://processing.org/) is a Free and Open Source (FLOSS) programming platform started in 2001 by Casey Reas and Ben Fry, widely used by artists and designers, as well as for teaching programming in a visual context. It allows you to generate interactive software with the most diverse purposes and visual interfaces, as well as exporting bitmap/raster images (like PNG and JPG), animations or 2D and 3D vector files (like PDF and SVG, among others). The community enjoys a rich ecosystem of people who produce resources such as teaching examples and freely shared code libraries.

Processing is originally based on the Java programming language, but today there are several projects that develop Processing ideas with other languages, such as *p5js* with Javascript, legacy *Processing Python mode* (inside the Processing IDE) using Python 2.7 (Jython), *pyp5js* using pyodide (a Python in your browser that can talk to *p5js*), and *py5* with Python 3 (CPython).

To use *py5* you will need:

- A **Python 3** interpreter (version 3.9 or later);
- The **py5 library package** and its dependencies (other libraries it needs to work, such as JPype);
- A **Java** (**JDK**), which *py5* needs for the Processing drawing infrastructure (JPype might look at the JAVA-HOME environment variable to find it);
- Optionally, an **IDE** (Integrated Development Environment), a code-appropriate text editor that helps you write and run programs. Some people prefer to use *py5* on *Jupyter Notebooks* instead.

To get all these things, this is an overview of the steps I propose and will describe in detail below:

1. Download and install a version of the **Thonny IDE** that comes with Python 3.10 or greater;
2. Inside *Thonny*...
    - a. Install the **py5** library (using the package manager);
    - b. Install the **thonny-py5mode** plug-in (using the extension manager); 
3. Restart Thonny, activate *imported mode for py5* and let the plug-in download and configure the **JDK** for you;
4. Check if everything is working, **run a small example!**
5. (Extra) Learn about the difference betweeen **imported mode** and **module mode**. 

>  Another way to get everything you need, if these steps fail for any reason, is to follow the instructions at the [py5 documentation](https://py5coding.org/content/install.html), starting with installing *miniconda*, which comes with Python and the *conda* package manager, to install *py5*, and then following the instructions for installing and setting up *Java* (*JDK*).

### 1. Download and install the Thonny IDE


- For Windows: 

    - Try to **[download and unzip this portanble](https://github.com/villares/thonny-portable-with-py5/releases/download/2024-12-17/thonny-417-with-py5-windows-portable.zip)**, double-click `thonny.exe` and skip to step 4!
    - or get a Thonny installer from [the repository releases](https://github.com/thonny/thonny/releases/)

- For MacOS: get an installer from [the repository releases](https://github.com/thonny/thonny/releases/)

- For Linux: get the latest package from [the repository releases](https://github.com/thonny/thonny/releases/) or run the [Thonny bash script installer](https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.bash)

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/02-start-splash.png)


### 2a. Install the *py5* library

Open, select *Tools > Manage packages...* from the menu…

Search for **py5** and click on the install button.

### 2b. Install the *thonny-py5mode* plug-in

Open, select *Tools > Manage plug-ins...* from the menu…

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.01-manage-plug-ins.png)

Search for **thonny-py5mode** (it needs to be typed exactly like this) and click on the install button.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.02-install-plug-in.png)

You need to __restart Thonny after this step!!!__

### 3. Allow the *thonny-py5mode* plug-in to download the Java JDK

Once restarted, a new *py5* menu should appear in Thonny's interface, click on the *py5 > Imported mode for py5* menu option and then click OK in the dialog window that appears.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.01-activate-imported-mode.png)

When you first select this, the plug-in will download, extract and configure the JDK for you (in Thonny's user-config directory). This process can be quite lengthy depending on your connection, but it only happens the first time you select the menu option.

**Thonny's window may appear frozen** as it downloads and configures the JDK, don't despair!**

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.02-download-jdk.png)

A message will appear when it is finished.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.03-download-jdk-done.png)

You can *apply recommended py5 settings* to make a few configuration tweaks to your IDE, including enabling the blue Kianite theme! 

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/05-apply-recommended-settings.png)

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.01-imported-activated.png)


### 4. Run a small example, to check everything is working!

With the *py5 > imported mode for py5* option on, you can run the following code using the green arrow button or CTRL+R (COMMAND+R on a Mac). Creative coders usually call their programs sketches.

```python
def setup():
    size(300, 200)
    rect_mode(CENTER)

def draw():
    square(mouse_x, mouse_y, 10)
```

If you have trouble geting your program to execute, try stopping any other execution that is still running.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.02-running-sketch.png)

### 5. (Extra) Learn about the difference between *imported mode* and *module mode*

#### What is the *imported mode* feature provided by the *thonny-py5mode* plug-in?

The *thonny-py5mode* plug-in creates a *py5* menu in the Thonny interface, inside the *py5* menu, there is an *Imported mode for py5* option that can be turned on or off. When *Imported mode for py5* is on you can write your sketches in a simplified maner, called [imported mode](https://py5coding.org/content/py5_modes.html#imported-mode). It works by making Thonny run your code using the *py5 sketch runner*, a special tool that can also be called from the command line if you are not using Thonny.

**Important note:** The *imported mode* option is not appropriate for executing Python code that doesn't make use of the py5 library!

In *imported mode* the vocabulary of *py5*, that is, the names of functions, constants and system variables (such as the mouse position), are available without the `py5.` prefix (needed on *module mode*, more about it later), and your program will be automatically executed by the `run_sketch` function from *py5*.

With *imported mode* on, you can also run [static mode](https://py5coding.org/content/py5_modes.html#static-mode) sketches, that is, programs without animation or interactivity because they do not have a `draw()` function defined.

#### What is *module mode* and how can I use it?

When you disable the *imported mode for py5* menu option, you return Thonny to the normal behavior for executing any Python code.

In this case, you can use *py5* in [module mode](https://py5coding.org/content/py5_modes.html#module-mode), which is how most Python libraries are handled, i.e. importing the library at the beginning of the program with `import`, and calling its functions with the library name as a prefix.

```python
import py5

def setup():
    py5.size(300, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)

py5.run_sketch()
```

Note that you will need to use `import py5` at the beginning of your code, and `py5.run_sketch()` at the end, as well as the `py5.` prefix for all functions, constants and variables offered by the *py5* library.

### Useful resources for using py5

- [official py5 documentation py5](http://py5coding.org/)
- The py5 [discussions](https://github.com/py5coding/py5generator/discussions) forum on GitHub
- The py5 category at the [Processing Foundation Forum](https://discourse.processing.org/c/a-version-of-processing-for-python-38-to-work-with-other-popular-python-libraries-and-tools-such-as-jupyter-numpy-shapely-trimesh-matplotlib-and-pillow-built-to-work-with-popular-python-libraries-and-tools-such-as-jupyter-numpy-shapely-etc/28)
- [examples in Jupyter Notebooks](https://github.com/py5coding/py5examples)
- [tabreturn's py5 quick reference](https://github.com/tabreturn/processing.py-cheat-sheet/blob/pt-br/py5/py5_cc.pdf)
- [sketch-a-day](https://abav.lugaralgum.com/sketch-a-day), my daily drawings with code, mostly with py5!

### Acknowledgments

Very special thanks to [Jim](https://ixora.io/), creator of py5, the maintainers of [Thonny IDE](https://github.com/thonny/), and [tabreturn](https://portfolio.tabreturn.com/) who made the *thonny-py5mode* plugin, which makes installing and using py5 much easier, the inspiration and images came from the installing intructions at his page.

### Please support my work

You can support my artistic work, research and open educational resources I publish on-line with [Liberapay](https://liberapay.com/villares), [Wise](https://wise.com/pay/me/alexandrev562) (preferred) or [PayPal](https://www.paypal.com/donate/?hosted_button_id=5B4MZ78C9J724).
---

Alexandre B A Villares ([abav.lugaralgum.com](https://abav.lugaralgum.com/)), [CC-BY-NC-SA-4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/)
