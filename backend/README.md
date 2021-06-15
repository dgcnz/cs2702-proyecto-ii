# Lab 6.1: Inverted Index

## Installation

```bash
pip3 install ntlk
pip3 install pyparsing
python3 -m nltk.downloader stopwords
python3 -m nltk.downloader punkt
```

## Usage

Run queries on the main program. Example:
```bash
python3 main.py
...

>> RET(frodo)
[0, 1, 2, 3, 4, 5]
>> OR(ANDNOT(RET(frodo), RET(legolas)), RET(legolas))
[0, 1, 2, 3, 4, 5]
>> OR(AND(RET(frodo), RET(comunidad)), RET(mordor))
[2, 3, 5]
>> AND(RET(legolas), OR(RET(hobbit), RET(anillo)))
[1, 2]
...
```

## TODO
- [ ] Update documentation with new changes
- [ ] Store index in secondary memory

## Preprocessor class

Wrapper class for text normalization functions.

```python
# Returns normalized word
Preprocessor.clean(word: str) -> str
```

```python
# Returns normalized text as list of tokens
Preprocessor.clean_text(text: str) -> List[str]
```

## Inverted Index class

```python
# Builds inverted index with set of documents, preprocessor and number of words (most frequent)
build_inverted_index(documents: List[str], p: Preprocessor, k: int) -> InvertedIndex
```

```python
# Returns indexes of documents containing word
InvertedIndex.sources(word: str) -> List[int]
```

```python
# Dumps inverted index into a file
InvertedIndex.dump(filename: str)
```

## Operators

```python
# Returns union of sorted lists a and b
OR(a: List[int], b: List[int]) -> List[int]
```

```python
# Returns conjunction of sorted lists a and b
AND(a: List[int], b: List[int]) -> List[int]
```

```python
# Returns conjunction of sorted lists a and negation of b
ANDNOT(a: List[int], b: List[int]) -> List[int]
```


## Parsing

Parsing is done with pyparsing library according to this grammar:

```
EXPR    := RET | OPRET
RET     := RET ( word )
OPRET   := OP ( EXPR , EXPR )
OP      := ANDNOT | OR | AND
```

Check parse.py for more details.


## Collaborators

- Andrea Díaz - 201720031
- Diego Cánez - 201710319
- Maor Roizman - 201810323
