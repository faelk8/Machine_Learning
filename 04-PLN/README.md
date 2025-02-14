<a id="topo"></a>
<h1 align="center">
  <img src="../image/pln.png" alt="machine-learning" width=720px height=450px >
  <br>
  <!-- Estudo de Caso -->
</h1>

<div align="center">

<!-- [![Status](https://img.shields.io/badge/version-1.0-blue)]() -->
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![Static Badge](https://img.shields.io/badge/NLP-blue)

</div>

# Índice
[Métricas](#metricas)<br>
[01.01 - Introdução Parte 1](#1.1)<br>
[01.02 - Introdução Parte 2](#1.2)<br>
[02 - Limpando os Dados](#2)<br>
[03 - Classificação Multi Label](#3)<br>
[04 - Corretor Ortográfico](#4)<br>


***

<a id="1.1"></a>





<a id="metricas"></a>

## Métricas
<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>
<h1 align="center">
  <img src="../image/metricas.png" alt="metricas" width=900px height=450px >
  <br>
</h1>

### Acurácis (Accuracy)
Mede a correção geral das previsões (normalmente classificações) calculando a porcentagem de previsões corretas do total de previsões.1

### F1 Score
Fornece uma abordagem mais sutil, especialmente para avaliar previsões categóricas em face de conjuntos de dados desequilibrados, combinando precisão e recuperação

### Perplexity
Mede o quão bem um LLM prevê um texto gerado por amostra, observando cada probabilidade de palavra gerada de ser a escolhida como a próxima na sequência. Em outras palavras, essa métrica quantifica a incerteza de modelotes.

### ROUGE, BLEU e METEOR
BLEU ROUGE, e METEORO são particularmente utilizados em tarefas de tradução e sumarização, onde tanto a compreensão da linguagem quanto os esforços de geração de linguagem são igualmente necessários: eles avaliam a semelhança entre textos gerados e de referência (por exemplo, fornecidos por anotadores humanos). O BLEU se concentra na precisão contando n-gramas correspondentes, sendo usado principalmente para avaliar traduções, enquanto o ROUGE mede o recall examinando unidades de linguagem sobrepostas, muitas vezes usadas para avaliar resumos. O METEOR adiciona sofisticação considerando aspectos adicionais, como sinônimos, hastes de palavras e muito mais.

### Exact Match
Uma métrica bastante direta, mas drástica, de comportamento correspondência exata (EM) é utilizado em casos de utilização de respostas a perguntas extrativas para verificar se uma resposta gerada por modelotes corresponde completamente a uma resposta de referência “gold standard”. É frequentemente usado em conjunto com a pontuação F1 para avaliar essas tarefas.



## 01.01 - Introdução Parte 1

<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>

* Bag of Words
* Matriz Esparsa
* Word Cloud
* Tokenize
* Stop Words


<a id="1.2"></a>

## 01.02 - Introdução Parte 2

<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>

* Pré processamento
* Stemmer
* TF-IDF- Vetorizar 
* Ngram


<a id="2"></a>

## 02 - Limpando os Dados

<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>


* Regex
* Padding

* Modelo
* NLTK MLE

<a id="3"></a>

## 03 - Classificação Multi Label

<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>

* One Vs Rest Classifier
* Distância Hamming
* Classifier Chain
* MLkNN

<a id="4"></a>

## 04 - Corretor Ortográfico

<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>

* Token
* Correção de Palavra


<a id="4"></a>

## 05 - Word Embedding

<div align="right">
    <a href="#topo">Voltar ao topo</a>
</div>

Tratamento de palavras raras e números na frase.

* Token
* Vetor de Palavras
* Classificação



***
<div align="left">
    <a href="#topo">Voltar ao topo</a>
</div>
