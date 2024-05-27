<a id="topo"></a>
<h1 align="center">
  <img src="../image/plot.png" alt="plot" width=720px height=420px >
  <br>
  <!-- Estudo de Caso -->
</h1>

<div align="center">

<!-- [![Status](https://img.shields.io/badge/version-1.0-blue)]() -->
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![Static Badge](https://img.shields.io/badge/graficos-blue)

</div>


[01 - Linha, Barra e Pizza](#1)<br>
[02 - Scater Plot, Box Plot e Histogram](#2)<br>
[03 - Visualização com Pandas](#3)<br>


<a id="1"></a>

## 01 - Linha, Barra e Pizza

<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>

- Matplotlib
  - Gráfico de linha
    * Espessura da linha
    * Legenda
    * Cor
    * Estilo da linha
    * Time Series
    * Grid
    * Plot dentro de outro plot
    * Filtro de cor
    * Anotação
  - Barra
    * Cores
  - Pizza
    * Percentual
    * Explodir


<a id="2"></a>

## 02 - Scater Plot, Box Plot e Histogram

<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>

- Matplotlib
  - Scater Plot
    * Cores
    * Legenda
    * Marcadores
  - Box Plot
    * Cores
    * Marcador Outlier
  - Histogram
    * Anotação
    * Média
    * Mediana

<a id="3"></a>

## 03 - Visualização com Pandas

<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>

Configuração do pandas para formatar a saída.

* Groupby
  * Sum
* Format
* Style
* Pivot


## 04 - Interativo



  * Criando ambiente virtual:
    ```
    python3.9 -m venv venv
    ```

  * Ativando ambiente virtual:
    ```
    source venv/bin/activate
    ```

  * Desativando ambiente virtual:
    ```
    deactivate
    ```

  * Acessando o serviço:
    ```
    streamlit run Dashboard.py
    ```

  * Ativar Always rerun 

O código roda sequencial, então os objetos serão carregados pela ordem do código.

Ordem de desenvolvimento:
* Leitura dos dados 
* Criação das tabelas 
* Criar o gráfico
* Visualização

Para novas páginas criar uma pasta chamada `pages` e colocar o código dentro, o nome do arquivo python sera o nome exibido no dashboard.

Deploy<br>
Colocando as bibliotecas que foram utilizadas no arquivo `requirements.txt`.<br>
Comando para mostrar:
```
pip freeze
```

***
<div align="left">
    <a href="#topo">Voltar ao topo</a>
</div>