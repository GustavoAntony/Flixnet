#Flixnet

## Como rodar o programa :

Primeiramente é necessário realizar a clonagem do repositório por meio do comando: git clone https://github.com/GustavoAntony/Flixnet.git . Assim como também instalar as bibliotecas necessárias e por fim executar o arquivo "demo.ipynb".

### Bibliotecas necessárias :
 * Numpy 
 * Pandas
 * matplotlib
 * copy
 * scipy

- Obs.: Para realizar a instalação de maneira automatizada basta rodar o comando pip install -r requirements.txt na raiz do projeto. 

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

### Como podemos usar esses dados para o sistema de recomentação ? 

Em sistemas de recomendação, pode-se usar a decomposição SVD para decompor uma matriz que representa as avaliações que os usuários fizeram sobre os itens em que estão interessados. Essa matriz pode ser muito grande, especialmente se houver muitos usuários e muitos itens, e pode ser difícil calcular a similaridade ou padrões entre os usuários ou entre os itens. Dessa forma, ao reduzir a dimensionalidade dessa matriz com a decomposição, é possível representar um espaço em que os usuários e os itens estão relacionados por meio de alguns poucos fatores latentes. Então, com base nesses padrões, é possível encontrar usuários com gostos e preferências semelhantes e sugerir a eles itens que outros usuários similares avaliaram positivamente. Isso é conhecido como filtragem colaborativa e é uma das principais técnicas usadas em sistemas de recomendação.

Assim, a decomposição SVD permite encontrar essas combinações lineares de perfis latentes que explicam as avaliações dos usuários. Cada usuário é representado por um vetor de coeficientes que indicam a contribuição de cada perfil latente em suas avaliações. Ao comparar esses vetores de coeficientes, podemos medir a similaridade entre os usuários e encontrar padrões e tendências em suas avaliações.

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

Ao considerarmos a matriz de usuários por filmes, que contém as notas atribuídas por cada usuário a cada filme, podemos tratá-la como uma imagem e realizar operações de compressão para reduzir os ruídos presentes nessa "imagem".

Nesse contexto, a nota desconhecida de um usuário pode ser considerada um ruído que pode ser reduzido por meio dessas operações de compressão, levando em consideração as notas atribuídas pelos outros usuários da plataforma. Dessa forma, é possível realizar uma estimativa mais precisa da nota do usuário para um determinado filme, utilizando técnicas semelhantes a de compressão de imagem.


### Estimativa dos K valores :


Para realizar a compressão de uma imagem utilizando a decomposição em valores singulares (SVD), é necessário selecionar os primeiros K autovalores da matriz diagonal $\Sigma$ e recompor a matriz com esses novos valores para obter a "imagem" comprimida. No entanto, para uma boa estimativa, é importante selecionar cuidadosamente os valores de K a serem considerados para a recomposição da matriz.

Uma análise dos valores de $\Sigma$ pode ser útil nesse processo, permitindo identificar quais autovalores são menos relevantes para a "imagem" original com ruído e podem ser descartados na recomposição da imagem. Ao selecionar um valor adequado para K, é possível realizar a compressão sem perder informações importantes da imagem e reduzir o ruído, buscando aproximar-se do valor real da "imagem".

Para escolher o valor de K adequado, é possível desconsiderar os valores muito baixos de $\Sigma$ (a partir do valor 100, por exemplo) e selecionar um valor próximo ao momento em que a curva começa a se tornar cada vez mais íngreme, ou seja, próximo ao limite em que os autovalores começam a se tornar mais relevantes para a composição da matriz inicial. Dessa forma, é possível realizar a compressão de forma eficiente, sem exagerar na redução do ruído e mantendo a essência da "imagem" original.

(Os valores de sigma estão no notbook demo.ipynb e no gráfico da imagem valores_sigma.png)


## Teste de Stress :

Foi realizado um teste de stress, no qual comparou-se o histograma gerado pelos erros obtidos após a inserção de um único dado aleatório na matriz inicial de usuários por filmes com o histograma gerado após a inserção de 50000 dados aleatórios nessa mesma matriz. Para calcular o erro no segundo histograma, foi realizado o cálculo dos erros de cada ponto modificado pelos dados "estragados", sendo aplicada uma média nesses dados de erro, a fim de obter um único número representando a média dos erros para cada iteração. Os histogramas obtidos estão sendo mostrados no código do demo.ipynb e também está salvo com o nome "Teststress.png" nos arquivos desse repositório. 


### Análise do teste :

Podemos observar que ao aumentar a quantidade de notas desconhecidadas (aumentar o ruído) fica cada vez mais dificil de estimar os valores já que estamos levando em conta os outros usuários também para essa conta, e se não conhecemos os outros usuários não temos como estimar de maneira tão certeira os outros usuários. Dessa forma é possível notar que o gráfico que foram estimadas mais notas de uma vez acaba concentrando uma quantidade maior de erros acima da faixa de dois de diferença, o que mostra essa dificuldade em prever a nota dos usuários com menos informação ( com mais ruído ).

