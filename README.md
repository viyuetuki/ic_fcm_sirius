<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=9A0000&height=120&section=header"/>

# 👩🏻‍💻📚 Iniciação Científica: "Estudos de Mapas Cognitivos Fuzzy para Modelagem de Problemas Inversos"

<p style='text-align: justify'> Este repositório do GitHub é destinado aos dados e experimentos realizados por mim, Vitória Yumi Uetuki Nicoleti 👩🏻‍💻, para minha iniciação científica, entitulada "Estudos de Mapas Cognitivos Fuzzy para Modelagem de Problemas Inversos", a qual realizei durante meu último ano de Bacharelado em Ciência e Tecnologia na <a href="https://ilum.cnpem.br/">Ilum Escola de Ciência</a>. Neste projeto, fui orientada pelo Professor pesquisador Doutor <a href="https://viniciuswasques.github.io/home/" >Vinícius Francisco Wasques</a> e co-orientada pelo pesquisador Doutor Eduardo Xavier Silva Miqueles.

Agradeço à Fundação de Amparo à Pesquisa do Estado de São Paulo (FAPESP), pelo financiamento do projeto referente ao processo <a href="https://bv.fapesp.br/pt/bolsas/218787/study-of-fuzzy-cognitive-maps-to-model-inverse-problems/">nº 2024/06949-7</a>.

🤔💭 Mas quem sou eu, afinal?

Caso queira saber mais sobre mim, acesse <a href="https://github.com/viyuetuki">aqui</a> meu perfil do GitHub e fique à vontade para ter mais informações e acessar os meus outros repositórios 😊.</p>

<p style='text-align: justify'><img src="https://fapesp.br/files/upload/15922/fapesp.gif" width="350" height="100" > </p>

## 🗄 Organização

<p style='text-align: justify'> Este repositório contempla as seguintes pastas:

🗃 <a href="https://github.com/viyuetuki/ic_fcm_sirius/tree/main/Raw%20Data">Raw Data</a> - É a pasta com arquivos .npy referentes às matrizes A e b do problema representativo de medições de tomografia computadorizada.

🗃 <a href="https://github.com/viyuetuki/ic_fcm_sirius/tree/main/gamma_pA">gamma_pA</a> - É a pasta com figuras em que: as imagens superiores representam as matrizes cujos elementos são apenas os gamas; e as imagens inferiores representam matrizes de A após aplicação do conceito de conectividade utilizando parâmetros γ otimizados correspondentes às tentativas da otimização por meio do Optuna.

🗃 <a href="https://github.com/viyuetuki/ic_fcm_sirius/tree/main/Histograms">Histograms</a> - É a pasta com figuras em que: as matrizes superiores indicam, visualmente, como os gamas de diferentes faixas
de valores (indicadas por diferentes cores) se distribuem na matriz; as imagens do centro são histogramas de distribuição dos gamas da tentativa divididos em 10 e 20 barras; e as imagens inferiores são histogramas de distribuição dos gamas da tentativa divididos em 5 e 2 barras (faixa de valores).

🗃 <a href="https://github.com/viyuetuki/ic_fcm_sirius/tree/main/solBonecos">solBonecos</a> -  É a pasta com figuras em que: as matrizes da esquerda são correspondentes às soluções nas dimensões (12 × 12) de cada tentativa representativa da otimização; e as matrizes da direita correspondem às soluções com um threshold = 2 nos valores dos pixels.

Outros arquivos que se encontram presentes:
    
📁 <a href="https://github.com/viyuetuki/ic_fcm_sirius/blob/main/.gitignore">.gitignore</a> - É o arquivo em que se define tudo o que vai ser ignorado neste repositório, como os checkpoints.
    
📁 <a href="https://github.com/viyuetuki/ic_fcm_sirius/blob/main/LICENSE">LICENSE</a> - É a licença utilizada para este repositório. No caso, GNU General Public License v3.0.
    
📁 <a href="https://github.com/viyuetuki/ic_fcm_sirius/blob/main/README.md">README.md</a> - É o arquivo do readme, com extensão markdown, deste repositório, que nada mais é do que exatamente o que você está lendo agora.

<!---Arquivos que precisam ser atualizados:
    
📁 <a href="https://github.com/viyuetuki/ic_fcm_sirius/blob/main/eliminacao_gaussiana.m">eliminacao_gaussiana.m</a> - É o arquivo em que definiu-se eliminação gaussiana (Octave). 

📁 <a href="https://github.com/viyuetuki/ic_fcm_sirius/blob/main/functions.py">functions.py</a> - É o arquivo em que armazenou-se parte das funções utilizadas ao longo do código (Python).

📁 <a href="https://github.com/viyuetuki/ic_fcm_sirius/blob/main/kaczmarz_method.ipynb">kaczmarz_method.ipynb</a> - É o arquivo base do desenvolvimento da iniciação científica, mas que está desatualizado com a versão final.

📁 <a href="https://github.com/viyuetuki/ic_fcm_sirius/blob/main/modular.ipynb">modular.ipynb</a> - É o arquivo base de todos os arquivos de experimento presente neste repositório.

📁 <a href="https://github.com/viyuetuki/ic_fcm_sirius/blob/main/orthogonal_projection.ipynb">orthogonal_projection.ipynb</a> - É o arquivo base de todos os arquivos de experimento presente neste repositório.
-->

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=9A0000&height=120&section=footer"/>