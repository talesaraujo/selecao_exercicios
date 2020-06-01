# Exercícios Seleção
Todos os exercícios deve ser feitos em Python mas podem ser usadas bibliotecas como OpenCV, Tensorflow, Keras, etc

## 1) Programa Python

Escreva um programa em Python para renomear todos os arquivos de uma pasta para valores sequenciais. 
Ex. 

```
abc.jpg
def.jpg
egh.jpg
```

devem ser renomeados para 

```
001.jpg
002.jpg
003.jpg
```

O programa deve receber como argumentos a pasta contendo os arquivos a serem renomeados:

#### Usage

```
python 1_renomear.py --input "caminho/para/pasta"
```

## 2) Serviço Web Python

Implemente um serviço web em Python que contem um endpoint para upload de arquivo. 
O serviço deve ler o arquivo enviado e retornar em formato json o conteúdo do arquivo. Assuma que somente arquivos de texto serão testados. 

Preferencialmente usar framework Flask

## 3) Classificação de imagens

Escreva um programa em Python que recebe uma imagem como argumento, classifica o objeto contido na imagem e imprime o resultado. 

Ex1.

<p align="center">
  <img src="images/dog1.jpg" width="350" title="dog1.jpg">
  <br>
  dog1.jpg
</p>

#### Usage

```
python 3_classificar.py -i dog1.jpg

>>> "Dog"
```

Ex2.

<p align="center">
  <img src="images/cat1.jpg" width="350" title="cat1.jpg">
  <br>
  cat1.jpg
</p>

#### Usage

```
python 3_classificar.py -i cat1.jpg

>>> "Cat"
```