# Ilocano-English Translator using CYK Algorithm

## Description
This project implements a simple translator between Ilocano and English languages using Context-Free Grammars (CFG) and the Cocke-Younger-Kasami (CYK) algorithm. The system validates sentences in both languages against their respective grammars and provides translations for recognized Ilocano sentences.

## Features
- Context-Free Grammar parsing using CYK algorithm
- Grammar validation for both Ilocano and English sentences
- Basic translation from Ilocano to English
- Support for imperative sentences

## Requirements
- Python 3.x
- NLTK library (`pip install nltk`)

## Project Structure
- `CYKAlgorithm.py` - Main implementation file containing the CYK algorithm and translation logic
- `english_cfg.txt` - Context-free grammar rules for English
- `english_imperative.txt` - Sample English sentences for testing
- `ilocano_cfg.txt` - Context-free grammar rules for Ilocano
- `ilocano_imperative.txt` - Sample Ilocano sentences for testing

## How It Works
1. The system reads grammar rules from text files.
2. Input sentences are tokenized using NLTK.
3. The CYK algorithm validates if sentences conform to their respective grammars.
4. For Ilocano sentences, translations to English are provided via a dictionary mapping.

## Implementation Details
The CYK algorithm is implemented in the `cyk_alg` function and works by:
1. Building a table to check if the input string belongs to the language defined by the grammar
2. Filling the table bottom-up, first with terminals and then with non-terminals
3. Determining if the input belongs to the grammar based on whether the top-level structure exists

The translation is handled by the `ilocano_to_english_translator` function using a dictionary mapping.

## Usage
Run the main script to validate and translate the example sentences:

```bash
python CYKAlgorithm.py
```

The output will show:
1. The parsing table for each input sentence
2. Whether the sentence belongs to the grammar
3. Translations for the Ilocano sentences

## Extending the Project
- Add more grammar rules to `ilocano_cfg.txt` and `english_cfg.txt`
- Extend the translation dictionary in the `ilocano_to_english_translator` function
- Add more test sentences to `ilocano_imperative.txt` and `english_imperative.txt`

## Limitations
- Currently supports only a small set of predefined sentences
- Grammar is limited to simple imperative structures
- Translation is based on exact matches rather than compositional semantics

## License
Open source