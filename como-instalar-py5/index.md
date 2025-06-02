# Como instalar e começar a usar a biblioteca py5

[[English Version](index-EN.md)] [[version en español ](index-ES.md)]

<h1 id="toc"></h1>
<!-- 
![thonny-logo](https://raw.githubusercontent.com/villares/villares.github.io/main/como-instalar-py5/thonny-logo.png) 
-->

### Resumo muito resumido

- Para desenhar e experimentar programação criativa com Python, <br> [siga as instruções abaixo](https://abav.lugaralgum.com/como-instalar-py5/#1-baixe-e-instale-o-thonny-ide);<br>
  <sub>**Um problema conhecido no Thonny**: Os gerenciadores de pacotes e de plug-in estão quebrados no Thonny 4.1.6, e em versões anteriores, devido a mudanças recentes no PyPI. O Thonny 4.1.7 corrige esses problemas.</sub>
- Se você está no Windows, [baixe e deszipe este arquivo](https://github.com/villares/thonny-portable-with-py5/releases/download/2024-12-17/thonny-417-with-py5-windows-portable.zip), abra o `thonny.exe` e pule para o passo 4 (*execute um pequeno exemplo*)!<br/>
  <sub>**Um problema conhecido no Windows**: Se o caminho da pasta do Thonny e do JDK Java contiver pastas com nomes com acento [isso quebra o jpype](https://github.com/jpype-project/jpype/issues/1111) e por isso quebra o py5.</sub> 

## O que é isso?

[**py5**](https://github.com/py5coding) é uma biblioteca<sup>⚹</sup> que permite o uso do vocabulário e da infraestrutura gráfica do **Processing** em conjunto com a mais recente versão da linguagem **Python**.

⚹ <sub>Bibliotecas são pacotinhos de código com funções complementares prontas, desenvolvidas previamente, para auxiliar o desenvolvimento de novos programas.</sub>

[**Processing**](http://processing.org) é uma plataforma livre/aberta de programação largamente utilizada por artistas e designers, assim como para o ensino de programação num contexto visual. Com ela é possível escrever softwares interativos com os mais diversos propósitos e interfaces visuais, assim como exportar imagens bitmap (PNG, JPG), animações ou arquivos vetoriais 2D e 3D (PDF e SVG entre outros). A comunidade desfruta de um rico ecossistema de pessoas que produzem recursos como exemplos didáticos e bibliotecas de código livremente compartilhadas.

Processing é baseada originalmente na linguagem de programação Java, mas hoje existem diversos projetos que desenvolvem as ideias do Processing com outras linguagens, como é o caso do *p5js* com Javascript,  *pyp5js* (combinando o Python no browser, pyodide, e *p5js*), e agora o **py5** com Python 3. 

Para usar **py5** você vai precisar:

- Ter um interpretador **Python 3** (versão 3.8 ou mais recente);

- Instalar a biblioteca **py5** e suas dependências (outras bibliotecas das quais ela precisa para funcionar, como o JPype);

- Um **Java (JDK)**, que o py5 precisa para a infraestrutura de desenho, e o seu JPype precisa saber onde ele está, por meio da variável JAVA-HOME;

- Um **IDE** (da sigla em inglês para ambiente integrado de desenvolvimento), simplificando, é um editor de texto apropriado para código, que facilita também executar os programas escritos por você. Algumas pessoas preferem escrever Python em *Jupyter Notebooks*, é legal também mas não é o foco deste passo a passo.

A sugestão aqui é seguir os seguintes passos: 

1. Baixar e instalar o **Thonny IDE** que vem com um Python 3.10 ou mais recente;
2. Dentro do *Thonny* instalar a biblioteca (package) **py5**; 
3. Instalar a extensão (plug-in), **thonny-py5mode**. Quando acionado pela primeira vez, o plug-in *thonny-py5mode* instala e configura o **JDK** para você;
4. Confira se tudo está funcioando **execute um pequeno exemplo!**
5. (Extra) Aprenda sobre a diferença entre o **imported mode** e o **module mode**.

<sub>Caso isso não dê certo, uma outra maneira de obter tudo que precisa é seguir as instruções em [py5 documentation](https://py5coding.org/content/install.html), começando por instalar uma distribuição Anaconda ou miniconda, que vem com um Python e o gerenciador de pacotes *conda*, para instalar *py5*, e depois instalar o JDK também.</sub>

## 1. Baixe e instale o Thonny IDE

Comece instalando o **Thonny IDE**.

- Para Windows:
    - Experimente [baixar e deszipar este arquivo](https://github.com/villares/thonny-portable-with-py5/releases/download/2024-12-17/thonny-417-with-py5-windows-portable.zip), faça um clique duplo em `thonny.exe` e pode pular para o passo 4!
    - ou instale executando o instalador [thonny-4.1.7.exe](https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.exe) e continue no passo 2.
     - **Um problema conhecido no Windows**: Se o caminho da pasta do Thonny, e do JDK Java, contiver pastas com nomes com acento [isso quebra o jpype](https://github.com/jpype-project/jpype/issues/1111) e por isso quebra o py5. Se, por exemplo, o seu nome de usuário tem acentos, experimente mover o Thonny para uma pasta direto em `C:\`.

- Para MacOS: baixe e exeute o instalador [thonny-4.1.7.pkg](https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.pkg) 

- Para Linux: execute este [script bash que baixa e instala o Thonny 4.1.7](https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.bash)
  
  ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/02-start-splash.png)

## 2. Instale a biblioteca *py5*

Uma vez aberto o Thonny, selecione no menu *Tools > Manage packages...* ou, em português: *Ferramentas > Gerenciar pacotes...<u></u>*

Procure a biblioteca __py5__ e peça para instalar.

## 3. Instale o plugin *thonny-py5mode*

Ainda no Thonny, selecione no menu *Tools > Manage plug-ins...* ou, em português: *Ferramentas > Gerenciar pluguins...<u></u>*

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.01-manage-plug-ins.png)

Procure o plug-in __thonny-py5mode__ e peça para instalar.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.02-install-plug-in.png)

Você precisa __reiniciar o Thonny depois deste epasso__, e em seguida, __permitir que o plug-in baixe o JDK__.

Uma vez reiniciado deve aparecer um novo menu *py5* na interface do Thonny, acione a opção  *py5 > Imported mode for py5* e depois clique em OK na janela de diálogo.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.01-activate-imported-mode.png)

Quando acionada pela primeira vez esta opção, o plug-in vai baixar, extrair e configurar o JDK para você (no diretório user-config do Thonny). Esse processo pode ser um tanto demorado, dependendo da sua conexão, mas só acontece da primeira vez que você aciona o menu.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.02-download-jdk.png)

Aparece este aviso quando terminou.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.03-download-jdk-done.png)

## 4. Execute um pequeno exemplo

Se quiser acione o comando opcional *Apply recommended py5 settings* que faz alguns ajustes no seu IDE, incluindo ativar o tema azulzinho *Kianite*.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/05-apply-recommended-settings.png)

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.01-imported-activated.png)

Agora o principal: com a opção *imported mode* acionada no menu *py5*, é possível executar o código a seguir usando o botão com a seta verde ou CTRL+R (ou COMMAND+R no Mac) .

```python
def setup():
    size(300, 200)
    rect_mode(CENTER)

def draw():
    rect(mouse_x, mouse_y, 10, 10)
```

Se tiver problemas para executar, lembre-se de parar com o botão *stop* vermelho alguma outra execução que ainda esteja rodando.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.02-running-sketch.png)

## 5. Aprenda sobre a diferença entre o *imported mode* e o *module mode*

### O que é a opção *imported mode for py5* fornecida pelo plug-in *thonny-py5mode*?

Quando a opção do menu *py5 > Imported mode for py5* está ligada, você pode escrever os seus programas (que também são chamados de *sketches*) de uma maneira simplificada, é o [imported mode](https://py5coding.org/content/py5_modes.html#imported-mode). Neste "modo" o Thonny vai executar o seu código usando o *py5 sketch runner* (executor de sketches), uma ferramenta especial que pode também ser acionada a partir da linha de comando, caso você não esteja usando o Thonny.

**Atenção:** O *imported mode* não é apropriado para executar código Python que não faça uso da biblioteca *py5*.

Neste "modo importado" o vocabulário da biblioteca *py5*, isto é, os nomes das funções, constantes e variáveis de sistema (como a posição do mouse), fica disponível sem o prefixo `py5.` (que é necessário no *module mode*, como veremos mais a seguir), e o seu programa vai ser automaticamente executado por uma função "run_sketch" da biblioteca *py5*. 

Com o *imported mode* ativado, também podem ser executados sketches do tipo [static mode](https://py5coding.org/content/py5_modes.html#static-mode), isto é aqueles sem animação ou interatividade pois não tem uma função `draw()` declarada. Mas estes precisam ter `size()` logo no começo.

### O que é o *module mode* e como podemos usá-lo?

Quando você desativa a opção *imported mode* no menu *py5*, você devolve o Thonny ao comportamento normal para executar qualquer código Python.

Neste caso, você pode usar a biblioteca *py5* no [module mode](https://py5coding.org/content/py5_modes.html#module-mode) que é como se lida com a maior parte das bibliotecas Python, isto é, importando a bibloteca no começo com a instrução `import`, e chamando suas funções com o nome da biblioteca como prefixo.

```python
import py5

def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.square(py5.mouse_x, py5.mouse_y, 10)

py5.run_sketch()
```
Note que você vai precisar usar a linha `import py5` no começo do seu código, a linha `py5.run_sketch()` no final, assim como o prefixo `py5.` para todas as funções, constantes e variáveis oferecidas pela bibliota *py5*.

## Referências úteis para usar o py5

* [Sumário traduzido para o português da referência do py5](https://abav.lugaralgum.com/material-aulas/Processing-Python-py5/sumario-referencia-py5.html) e [documentação oficial completa do py5, em inglês](http://py5coding.org/) 
* [Curso de Python para design com py5 na Domestika](
https://www.domestika.org/pt/courses/4307-design-com-python-programacao-para-um-contexto-visual/a_b_a_villares)
* Material didático aberto [Introdução à programação com Python em um contexto visual](https://abav.lugaralgum.com/material-aulas/Processing-Python-py5/) (usando py5)
* [Referência rápida do py5](https://github.com/villares/processing.py-cheat-sheet/blob/pt-br/py5/py5_cc.pdf) (versão traduzida da "colinha" do Tristan Bunn)
* [Exemplos de py5 em Jupyter Notebooks](https://github.com/py5coding/py5examples)
* [Fórum do py5](https://github.com/py5coding/py5generator/discussions)
* [Fórum da Fundação Processing](https://discourse.processing.org/)

### Agradecimentos

Agradecimentos muito especiais ao criador do *py5*, [Jim](https://ixora.io/), aos mantenedores do IDE [Thonny](https://github.com/thonny/), e ao [tabreturn](https://portfolio.tabreturn.com/) que fez o plug-in *thonny-py5mode*, que facilita demais a instalação e uso do *py5*, as instruções em inglês dele são o ponto de partida destas instruções e fonte das imagens todas!

--- 

Alexandre B A Villares ([abav.lugaralgum.com](https://abav.lugaralgum.com)), [CC-BY-NC-SA-4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/)
