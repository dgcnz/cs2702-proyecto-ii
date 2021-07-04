# Backend

## Setup and Installation

```bash
# Install dependencies
./scripts/install
# Create tweet jsons
./scripts/inflate_data
# Create N tweet jsons
env/bin/python3 scripts/split_data.py scripts/data1.csv scripts/data2.csv --maxn N
```

## TODO
- [ ] Store index in secondary memory
- [ ] Add tf-idf weights

## Block-based indexing

**N-th Index**: `iixb_{N}.json`
- Processes the n-th chunk of documents.

```
{
docs: {
            doc1: 10, // count of words per doc
            doc2: 20,
            ..
},
words: {
            word1:  {
                        doc1: 4, // tf of word in doc
                        doc2: 5,
                        ...
            },
            word2:  {
                        ...
            },
            ...
}
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
