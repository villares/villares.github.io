----

[[English Version](index-EN.md)]

# Como instalar e começar a usar a biblioteca py5

### TL:DR;

- Para desenhar e experimentar programação criativa com Python [siga estas instruções abaixo.](https://abav.lugaralgum.com/como-instalar-py5/#1-baixe-e-instale-o-thonny-ide-vers%C3%A3o-337-alt)
- Se você está no Windos, [baixe e deszipe este arquivo](https://www.dropbox.com/s/3ue4cx3yf372teg/thonny-4-with-py5-windows-portable.zip?dl=0) e pule para o passo 5!

## O que é isso?

[**py5**](https://github.com/py5coding) é uma 
<ins title="bibliotecas são pacotes de funções complementares prontas, ou desenvolvidas por outras pessoas, para auxiliar o desenvolvimento de novos programas." style="text-decoration:underline; text-decoration-style: dotted;">biblioteca</ins> que permite o uso do vocabulário e da infraestrutura gráfica do **Processing** em conjunto com a mais recente versão da linguagem **Python**.

[**Processing**](http://processsing.org) é uma plataforma livre/aberta de programação largamente utilizada por artistas e designers, assim como para o ensino de programação num contexto visual. Com ela é possível escrever softwares interativos com os mais diversos propósitos e interfaces visuais, assim como exportar imagens bitmap (PNG, JPG), animações ou arquivos vetoriais 2D e 3D (PDF e SVG entre outros). A comunidade desfruta de um rico ecossistema de pessoas que produzem recursos como exemplos didáticos e bibliotecas de código livremente compartilhadas.

Processing é baseada originalmente na linguagem de programação Java, mas hoje existem diversos projetos que desenvolvem as ideias do Processing com outras linguagens, como é o caso do p5js com Javascript, e o py5 com Python 3. 

Para usar py5 você vai precisar:

- Ter um interpretador **Python 3** (versão 3.8 ou mais recente);

- Instalar a biblioteca **py5** e suas dependências (outras bibliotecas das quais ela precisa para funcionar, como o JPype);

- Um **Java (JDK)**, que o py5 precisa para a infraestrutura de desenho, e o seu JPype precisa saber onde ele está, por meio da variável JAVA-HOME;

- Um **IDE** (da sigla em inglês para ambiente integrado de desenvolvimento), simplificando, é um editor de texto apropriado para código, que facilita tamb executar os programas escritos por você.

A sugestão aqui é seguir os seguintes passos: 

1. Baixar e instalar o **Thonny IDE** que vem com um Python 3.8 ou mais recente;
2. Dentro do *Thonny* instalar a extensão (plug-in), **thonny-py5mode**;
3. Deixar o plug-in *thonny-py5mode* instalar e configurar o **JDK** para você;
4. Conferir se tudo está funciando **executando um pequeno exemplo!**
5. (Exta) Aprenda sobre a diferencça entre o **imported mode** e o **module mode**.

> Uma outra maneira de obter tudo que precisa é seguir as instruções em [py5 documentation](https://py5coding.org/content/install.html), começando por instalar uma distribuição Anaconda ou miniconda, que vem com um Python e o gerenciador de pacotes *conda*, para instalar *py5*, e depois instalar o JDK também.

## 1. Baixe e instale o Thonny IDE

- Para Windows:
    - Experimente [baixa e deszipar este arquivo](https://www.dropbox.com/s/3ue4cx3yf372teg/thonny-
    - ou [thonny-3.3.7-alt.exe](https://github.com/thonny/thonny/releases/download/v3.3.7/thonny-3.3.7-alt.exe) 
4-with-py5-windows-portable.zip?dl=0) e pode pular para o passo 5!

- Para MacOS: [thonny-3.3.7-alt.pkg](https://github.com/thonny/thonny/releases/download/v3.3.7/thonny-3.3.7-alt.pkg) 

- Para Linux: [thonny-3.3.7-x86_64-alt.tar.gz](https://github.com/thonny/thonny/releases/download/v3.3.7/thonny-3.3.7-x86_64-alt.tar.gz) 
  
  ![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/02-start-splash.png)

## 2. Instale o plugin *thonny-py5mode*

Uma vez aberto o Thonny, selecione no menu *Tools > Manage plug-ins...* ou, em português: *Ferramentas > Gerenciar pluguins...<u></u>*
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.01-manage-plug-ins.png)
Procure o plug-in __thonny-py5mode__ e peça para instalar.
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/03.02-install-plug-in.png)
Você precisa __reiniciar o Thonny depois desta etapa!!!__ 

## 3. Permita que o plug-in baixe o JDK

Uma vez reiniciado deve aparecer um novo menu *py5* na interface do Thonny, acione a opção  *py5 > Imported mode for py5* e depois clique em OK na janela de diálogo.
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.01-activate-imported-mode.png)
Quando acionada pela primeira vez esta opção, o plug-in vai baixar, extrair e configurar o JDK para você (no diretório user-config do Thonny). Esse processo pode ser um tanto demorado, dependendo da sua conexão, mas só acontece da primeira vez que você aciona o menu.

**A janela do Thonny pode parecer congelada** enquanto ele baixa e configura, não se desespere!
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.02-download-jdk.png)
Aparece este aviso quando terminou.
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/04.03-download-jdk-done.png)

Um ajuste opcional: O comando *Apply recommended py5 settings* faz alguns ajustes no seu IDE, incluindo ativar o tema azulzinho *Kianite*.
![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/05-apply-recommended-settings.png)

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.01-imported-activated.png)

## 4. Execute um pequeno exemplo! 

Com a opção *imported mode* acionada no menu *py5*, é possível executar o código a seguir usando o botão com a seta verde ou CTRL+R (ou COMMAND+R no Mac) .

```python
def setup():
    size(300, 200)
    rect_mode(CENTER)

def draw():
    rect(mouse_x, mouse_y, 10, 10)
```

Se tiver problemas para executar, lembre-se de parar com o botão *stop* vermelho alguma outra execução que ainda esteja rodando.

![](https://raw.githubusercontent.com/tabreturn/thonny-py5mode/main/screenshots/06.02-running-sketch.png)

## 5. Veja a diferença entre o *imported mode* e o *module mode*

### O que é o a função *imported mode* fornecida pelo plug-in *thonny-py5mode*?

Quando a opção do menu *py5 > Imported mode for py5* está ligada, você pode escrever os seus programas (que também chamamos de *sketches*) de uma maneira simplificada, é o [imported mode](https://py5coding.org/content/py5_modes.html#imported-mode). Neste "modo" o Thonny vai executar o seu código usando o *py5 sketch runner* (executor de sketches), uma ferramenta especial que pode também ser acionada a partir da linha de comando, caso você não esteja usando o Thonny.

**Atenção:** O *imported mode* não é apropriado para executar código Python que não faça uso da biblioteca *py5*.

Neste "modo importado" o vocabulário da biblioteca *py5*, isto é, os nomes das funções, constantes e variáveis de sistema (como a posição do mouse), fica disponível sem o prefixo `py5.`, e o seu programa vai ser automativamente executado por uma função "run_sketch" da biblioteca *py5*. 

Com o *imported mode* ativado, também podem ser executados sketches do tipo [static mode](https://py5coding.org/content/py5_modes.html#static-mode), isto é aqueles sem animação ou interatividade pois não tem uma função `draw()` declarada.

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

* [referência rápida do py5 (colinha)](https://github.com/villares/processing.py-cheat-sheet/blob/pt-br/py5/py5_cc.pdf)
* [fórum do py5](https://github.com/py5coding/py5generator/discussions)
* [documentação oficial do py5](http://py5coding.org/)
* [exemplos de py5 em Jupyter Notebooks](https://github.com/py5coding/py5examples)
* [Fórum da Fundação Processing](https://discourse.processing.org/)

### Agradecimentos

Agradecimentos muito especiais ao criador do *py5*, [Jim](https://twitter.com/py5coding), aos mantenedores do IDE [Thonny](https://twitter.com/thonnyIDE), e ao [tabreturn](https://twitter.com/tabreturn) que fez o plug-in *thonny-py5mode*, que facilita demais a instalação e uso do *py5*, as instruções em inglês dele são o ponto de partida destas instruções e fonte das imagens todas!

---

Alexandre B A Villares ([abav.lugaralgum.com](https://abav.lugaralgum.com)), [CC-BY-NC-SA-4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/)
