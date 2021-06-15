# Backend

## Installation

```bash
./scripts/install
```

## Testing

```bash
./scripts/run_tests
```

## TODO
- [ ] Store index in secondary memory
- [ ] Add tf-idf weights

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
# Returns indices of documents containing word
InvertedIndex.retrieve(word: str) -> List[int]
```

```python
# Returns indices of documents dictated by natural language query q
InvertedIndex.query(q: str) -> List[int]
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
