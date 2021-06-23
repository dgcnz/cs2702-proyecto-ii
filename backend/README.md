# Backend

## Installation

```bash
./scripts/install
```

## TODO
- [ ] Store index in secondary memory
- [ ] Add tf-idf weights

## Block-based indexing

**N-th Index**: `iixb_{N}.json`
- Processes the n-th chunk of documents.

```
{
word1:  {
            [(docid1, tf(word1, docid1)), (docid2, tf(word1, docid2)), ...]
        },
word2:  {
        ...
        },
...
}
```

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
# Returns indices of documents containing word
InvertedIndex.retrieve(word: str) -> List[int]
```

```python
# Dumps inverted index into a file
InvertedIndex.dump(filename: str)
```


## Collaborators

- Andrea Díaz - 201720031
- Diego Cánez - 201710319
- Maor Roizman - 201810323
