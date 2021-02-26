# Um estudo sobre o problema dos *K* caminhos mais curtos

O problema dos *K* caminhos mais curtos acíclicos consiste em encontrar, em uma rede direcionada valorada, um conjunto de *K* rotas, minimizando o caminho percorrido entre um ponto de origem e um ponto de destino. O código foi implementado utilizando um algoritmo clássico da literatura para o problema, o algoritmo de Yen, retirado do artigo *Finding the K Shortest Loopless Paths in a Network* de 1971.

## Requirements
Para utilizar este código, você precisará de:   

[![Python Version](https://img.shields.io/badge/python-3.6.9-green)](https://www.python.org/downloads/release/python-369/)

Clone o repositório atual: 
> git clone https://github.com/quionee/k-shortest-path

Após clonar o repositório, use os seguintes comandos no diretório raíz do mesmo:

Para Linux e Mac:
```
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Para Windows:
```
> python -m venv env
> .\env\Scripts\activate.bat
> pip install -r requirements.txt
```

Assim, para executar o código, basta entrar na pasta *code* e rodar o arquivo *main*:

Para Linux e Mac:
```
$ python main.py test_instance.txt
```

Para Windows:
```
> python .\main.py test_instance.txt
```

Copyright (c) 2020 Lorena Tavares
