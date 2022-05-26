----

# Como instalar o py5

### O que é isso?

[**py5**](https://py5.ixora.io) é uma biblioteca que permite o uso do vocabulário e da infraestrutura gráfica do **Processing** em conjunto com a mais recente versão da linguagem **Python**.

TL:DR; Para desenhar e trabalhar com programação criativa no Python [siga estas instruções abaixo.](https://abav.lugaralgum.com/como-instalar-py5/#1-baixe-e-intale-o-thonny-ide-vers%C3%A3o-337-alt)



[**Processing**](http://processsing.org) é uma plataforma livre/aberta de programação largamente utilizada por artistas e designers, assim como para o ensino de programação num contexto visual. Permite permite gerar softwares interativos com os mais diversos propósitos e as mais diversas interfaces visuais, assim como exportar imagens bitmap (PNG, JPG), animações ou arquivos vetoriais 2D e 3D (PDF e SVG entre outros). A comunidade desfruta de um rico ecossistema de pessoas que produzem recursos como exemplos didáticos e bibliotecas de código livremente compartilhadas.

Processing é baseada originalmente na linguagem de programação Java, mas hoje existem diversos projetos que desenvolvem as ideias do Processing com outras linguagens, como é o caso do p5js com Javascript, e o py5 com Python 3.

Para usar a py5 você vai precisar:

- Ter um interpretador **Python 3** (versão 3.8 ou mais recente);

- Instalar a biblioteca **py5** e suas dependências (outras bibliotecas das quais ela precisa para funcionar, como o JPype);

- Um **Java (JDK-17)**, que o py5 precisa para a infraestrutura de desenho, e o seu JPype precisa saber onde ele está, por meio da variável JAVA-HOME;

- Um **IDE** (da sigla em inglês para ambiente integrado de desenvolvimento), simplificando, é um editor de texto apropriado para código, que permite executar os programas escritos por você.

Vamos sugerir começar por instalar uma versão específica do **IDE Thonny** (que vem com um Python 3.8) e em seguida uma extensão (plug-in), **thonny-py5mode** que instala e configura o jdk-17 para você!

> Uma outra maneira de obter tudo que precisa é seguir as instruções em [py5 documentation](https://py5.ixora.io/content/install.html), começando por instalar uma distribuição Anaconda ou miniconda, que vem com um Python e o gerenciador de pacotes *conda* para instalar *py5* e o JDK.

#### 1. Baixe e intale o Thonny IDE, versão 3.3.7-alt

- Para Windows: [thonny-3.3.7-alt.exe](https://github.com/thonny/thonny/releases/download/v3.3.7/thonny-3.3.7-alt.exe) 

- Para MacOS: [thonny-3.3.7-alt.pkg](https://github.com/thonny/thonny/releases/download/v3.3.7/thonny-3.3.7-alt.pkg) 

- Para Linux: [thonny-3.3.7-x86_64-alt.tar.gz](https://github.com/thonny/thonny/releases/download/v3.3.7/thonny-3.3.7-x86_64-alt.tar.gz) 
  
  ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/02-start-splash.png)

#### 2. Instale o plugin *thonny-py5mode*

Uma vez aberto o Thonny, selecione no menu *Tools > Manage plug-ins...* ou, em português: *Ferramentas > Gerenciar pluguins...<u></u>*
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.01-manage-plug-ins.png)
Procure o plug-in __thonny-py5mode__ e peça para instalar.
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.02-install-plug-in.png)
Você precisa __reiniciar o Thonny depois desta etapa!!!__ 

#### 3. Permita que o plug-in baixe o JavaJDK-17

Uma vez reiniciado deve aparecer um novo menu *py5* na interface do Thonny, clique na opção  *py5 > Imported mode for py5* e OK na janela de diálogo
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.01-activate-imported-mode.png)
This will download, extract, and set up JDK-17 for you (if you need to know: the plug-in installs JDK in the Thonny user-config directory). Thonny only needs to download JDK the first time you switch to imported mode. __Thonny will appear to freeze__ for a while when it's downloading JDK (I have plans to develop a proper progress indicator later).
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.02-download-jdk.png)
You'll be notified once the download is done --
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.03-download-jdk-done.png)

Opcional: O comando *Apply recommended py5 settings* faz alguns ajustes no seu IDE, incluindo ativar o tema *Kianite*.
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/05-apply-recommended-settings.png)

**Atenção:** Quandoa a opção do menu *py5 > Imported mode for py5* está ligada, o Thonny vai executar o seu código usando a ferramenta *run_sketch* do *py5* ...
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.01-imported-activated.png)

#### 4. Aprenda a diferença entre o *imported mode* e o *module mode*, execute um pequeno exemplo e pronto, terminou!

Com a opção [imported mode](https://py5.ixora.io/content/py5_modes.html#imported-mode) acionada no menu *py5*, é possível executar o código a seguir usando o botão com a seta verde ou CTRL+R (ou COMMAND+R no Mac) .

```python
def setup():
    size(300, 200)
    rect_mode(CENTER)

def draw():
    rect(mouse_x, mouse_y, 10, 10)
```

Note que neste modo o vocabulário da biblioteca *py5*, isto é, funções, constantes e variáveis, estão disponíveis sem prefixo algum, e o seu programa vai ser executado pelo "sketch runner" da biblioteca *py5*. Isto não é apropriado para executar código Python que não faça uso de *py5*.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.02-running-sketch.png)O *imported mode* também serve para sketch do tipo [static mode](https://py5.ixora.io/content/py5_modes.html#static-mode), isto é aqueles sem a função `draw()` que permite animações e interatividade.

Se tiver problemas para executar, lembre de parar com o botão *stop* vermelho alguma execução que ainda esteja rodando.

#### O que é o *module mode*?

Quando você desativa a opção *imported mode* no menu *py5*, você devolve o Thonny ao comportamento normal para executar qualquer código Python. Neste caso, você pode então usar a biblioteca *py5* no [module mode](https://py5.ixora.io/content/py5_modes.html#module-mode) que é parecido com o que se faz com a maior parte das bibliotecas Python que você vai encontrar.

```python
import py5

def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)

py5.run_sketch()
```

 Note que você vai precisar usar a linha `import py5` no começoe e a linha `run_sketch()` no final do código, assim como o prefixo `py5.` para todas as funções, constantes e variáveis oferecidas por* py5*.

## Referências úteis para usar o py5

* [py5 cheatsheet](https://raw.githubusercontent.com/tabreturn/processing.py-cheat-sheet/master/py5/py5_cc.pdf)
* [py5 discussions/forum](https://github.com/hx2A/py5generator/discussions)
* [py5 documentation](http://py5.ixora.io/)
* [py5 examples](https://github.com/hx2A/py5examples)
* [Processing forum](https://discourse.processing.org/)

Alexandre B A Villares ([abav.lugaralgum.com](https://abav.lugaralgum.com)), [CC-BY-NC-SA-4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/)
