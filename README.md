# Proyecto 2 - Recuperación de Documentos de Texto


## Datos generales
### Integrantes
- Andrea Díaz
- Diego Cánez
- Maor Roizman

## Descripción

### Objetivo del Proyecto

### Descricpión del Dominio de Datos
`Kaggle Dataset:` [All The News](https://www.kaggle.com/snapcrack/all-the-news)

## Funcionamiento

### Prepocesamiento

### Construcción del índice invertido

### Blocked Sort-Based Indexing
La complejidad teórica de la construcción de este índice es de $`O (n \log n)`$ siendo $`n`$ la cantidad de keys a ordenar en el merge y el ordenamiento de los bloques. Dentro de nuestra implementación hemos construido cada bloque en forma de .json files, de esta manera mantenemos diccionarios dentro de la memoria.

### Complejidad Algorítmica

### Manejo de memoria secundaria

### Consultas

### API

> Buscar todos los tweets relevantes.
- `Method:` GET
- `Parameters:` **text**=Lorem Ipsum...
- `Response:`
```
{
  "current_page": 1,
  "total_pages": 12,
  "tweets": [
            {
              "id": 1,
              "title": "",
              "publication": "",
              "author": "",
              "date": "",
              "text": "",
              "year": 2016.0,
              "month": 12.0,
              "content": "Lorem Ipsum..."
            },
            ...
  ]
}
```

## Frontend

## Demostración
