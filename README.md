# MimicEmbeddings
### Overview
The [MIMIC-III](https://mimic.physionet.org/) [NoteEvents table](https://mimic.physionet.org/mimictables/noteevents/) contains over 2 million medical notes of varying types, written by physicians, nurses, radiologists, social workers, etc. This work creates and evaluates word embeddings from these notes.

### Details
All notes are selected, and a small number of notes identified with having errors are removed. Text that has been deidentified (such as shifted dates) are removed. Crude preprocessing is done by removing some common section headers. All text is converted to lower case and tokenized. There are about 600 million tokens in total. The word2vec skip-gram model, which has [previously been identified as having better performance than CBOW in this domain](http://aclweb.org/anthology/W/W16/W16-2922.pdf), is used. A small grid search over hyperparameters is done. Intrinsic evaluation is conducted using [UMNSRS](http://rxinformatics.umn.edu/SemanticRelatednessResources.html).

### Results
The best performing set of hyperparameters on UMNSRS-rel is 300-4-20 with a ρ of 0.4980. The best performing set of hyperparameters on UMNSRS-sim is 300-50-5 with a ρ of 0.5851. However, as the minimum count gets too large, the number of unique tokens encoded by the embedding gets smaller, and more words are missing. For example, using a minimum count of 4 yields embeddings with 420,786 unique tokens, while using a minimum count of 50 yields embeddings with 80,453 unique tokens. Therefore, the 300-4-20 embedding set will be used for future modelling.
