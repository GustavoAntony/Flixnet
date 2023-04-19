#Flixnet

## Como rodar o programa :

Primeiramente é necessário realizar a clonagem do repositório por meio do comando: git clone https://github.com/GustavoAntony/Flixnet.git . Assim como também instalar as bibliotecas necessárias e por fim executar o arquivo "demo.ipynb".

### Bibliotecas necessárias :
 * Numpy 
 * Pandas
 * matplotlib
 * copy
 * scipy

- Obs.: Para realizar a instalação de maneira automatizada basta rodar o comando pip install -r requiriments.txt na raiz do projeto. 

### Execução:

- Para executar, basta rodar o arquivo "demo.ipynb"

## Considerações iniciais :  

________________________
### Composição dos usuários : 

A ideia do sistema de recomendação é que existem "perfis" típicos de usuários. Os perfis, para este problema, são vetores que mostram que notas são tipicamente atribuídas para cada filme por usuários daquele perfil. Por exemplo, talvez tenhamos dois perfis e três filmes, e nesse caso poderíamos ter os perfis:


Cada usuário desse sistema é formado por uma combinação linear de perfis típicos. E, neste caso, os perfis, para este problema, são vetores que mostram que notas são tipicamente atribuídas para cada filme por usuários daquele perfil. Assim, podemos modelar da seguinte forma :

* $p_0 = [2, 5, 2]$, isto é, o perfil $0$ é de uma pessoa que gosta muito do filme $f_1$, e
* $p_1 = [5, 0, 4]$, isto é, o perfil $1$ é de uma pessoa que gosta dos filmes $f_0$ e $f_2$. 

* $u_0 = 0.1 p_0 + 0.9 p_1$, para um usuário muito próximo de $p_1$ mas distante de $p_0$,
* $u_1 = 0.1 p_0 + 0.1 p_1$, para um usuário distante tanto de $p_0$ quanto de $p_1$,

e assim por diante.

### Decomposição em valors singulares (SVD):

Então, o que precisamos é de uma maneira de mapear usuários para perfis, e então perfis para filmes. Precisamos então *decompor* nossa matriz $A$ de usuários $\times$ filmes em componentes:

$
A = X Y Z,
$

onde:
* $A$ tem uma linha por usuário e uma coluna por filme,
* $X$ tem uma linha por usuário e uma coluna por perfil,
* $Y$ é quadrada e mapeia perfis para perfis,
* $Z$ tem uma linha por perfil e uma coluna por filme.


### Compressão :

Ao tratar essa matriz de usuários por filmes que contém as notas de que cada user deu para cada filme como se fosse uma imagem, é possível realizar operações de compressão para redução de ruídos nessa "imagem". Dessa forma, ao considerar a nota desconhecida como um ruído é possível fazer a estimativa atravéz dessa operação levando em consideração as notas dos outros usuários da plataforma.

### Estimativa dos K valores :


Para realizar a compressão, é necessário zerar uma certa quantidade de autovalores da matriz $\Sigma$ que é obtida pós decomposição e posteriormente recompor a matriz com esse novo valor obtendo a matriz ou a "imagem" comprimida e, se tudo der certo, esperamos também encontrar um valor mais próximo da realidade ao invés de um ruído ainda maior. Mas para uma boa estimativa é nessessário escolher bem os K primeiros valores que vão ser considerados para a recomposição da matriz e para isso fizemos uma análise de como esses valores se comportam. Após a observação do gráfico de como os valores de $\Sigma$ se comportam é possível notar que existem muitos valores que não são relevantes e que se retirados não vão alterar tanto a matriz original (com ruído). Dessa forma, é necessário selecionar um valor para K que de fato nos ajude a comprimir essa "imagem" e reduzir o ruído, por isso, podemos desconsiderar o intervalo em que os valores são muito baixos (valores de 150 adiante) e podemos selcionar o valor que está perto do momento em que a curva passa a ser cada vez mais ingrime, perto do limite em que os valores K passam a ser muito relevantes para aquela "imagem", realizando então essa compressão sem perder a essência, e dessa forma podemos reduzir o ruído tentando aproximar ao máximo do valor real, sem exagerar para que não seja obtido um valor com um ruído maior que o anterior. 