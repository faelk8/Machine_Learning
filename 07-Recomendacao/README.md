<a id="topo"></a>
<h1 align="center">
  <img src="../image/cluster.jpeg" alt="cluster" width=360px height=200px >
  <br>
  Clusterização
</h1>

<div align="center">

<!-- [![Status](https://img.shields.io/badge/version-1.0-blue)]() -->
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![Static Badge](https://img.shields.io/badge/Machine%20Learning-blue)

</div>

Estudo de algoritimos de clustering.

[01 - Classificação](#1)<br>
[02 - Segmentação de Cliente](#2)<br>
[03 - Extraindo Padrôes](#3)<br>
<a id="1"></a>

## 01 - Sistema de Recomendação Musical 

<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>

Sistema de recomendação musical utilizando músicas a partir do ano 2000.

* Análise 
  * Plotly
    * Correlação

* Pré Processamento
  * PCA 
  * SdandardScaler

* Modelo
  * K-Means


<a id="2"></a>

## 02 - Segmentação de Cliente

<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>

Segmentando os cliente utilizando Kmeans.

* Análise 
  * Seaborn
    * Bar Plot com percentual
    * Scatter Plot

* Modelo
  * Regra do Cotovelo
  * K-Means
  * Número ótimo de cluster

<a id="3"></a>

## 03 - Extraindo Padrôes

<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>

No final do Jupyter contém a descrição dos cluster.

* Análise exploratória
  * Missing Value
  * Normalizer

* Modelo
  * Kmeans 
    n_init=10 : Vai retornarna 10 vezes o mesmo valor

* Metricas
  * Silhouette Score: Avalia a separação e coesão dos clusters. <br>
    Mede a qualidade da separação entre os clusters. Ele avalia o quão similar um objeto é ao seu próprio cluster (coesão) em comparação com outros clusters (separação). O valor varia de -1 a 1:<br>
    * Próximo de 1: As amostras estão bem agrupadas dentro dos clusters e bem separadas de outros clusters.
    * Próximo de 0: As amostras estão na fronteira ou entre clusters.
    * Negativo: As amostras podem estar no cluster errado.

  * Davies Bouldin Score: Avalia a similaridade entre clusters.<br>
    Mede a média da "semelhança" entre cada cluster e aquele que mais se assemelha a ele. Quanto menor o valor, melhor a qualidade da segmentação. Utiza o centróide no cálculo. Ele considera:<br>
    * Dispersão dentro dos clusters: Quão compactos são os clusters.
    * Separação entre os clusters: Quão distintos são os clusters uns dos outros.

  * Calinski Harabasz Score: Avalia a dispersão dentro e entre os clusters.<br>
    Conhecido como Índice Variance Ratio Criterion, mede a razão entre a soma da dispersão entre clusters e a soma da dispersão dentro dos clusters. Quanto maior o valor, melhor a qualidade da segmentação. Ele é calculado com base em:<br>
    * Dispersão total: A soma das distâncias ao centro do cluster.
    * Dispersão entre clusters: A distância entre os centros dos clusters.

***
<div align="left">
    <a href="#topo">Voltar ao topo</a>
</div>