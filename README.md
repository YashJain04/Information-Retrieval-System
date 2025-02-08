# Submission Details

## Students Information:
- Yash Jain : 300245571
- Tolu Emoruwa : 300230905
- Shacha Parker : 300235525

## Dividing Tasks Information:
1. Yash Jain's Work...
- Initial setup of project and added documentation/comments throughout all the code
- Implementation of Ranking Algorithm BM25 (Step 3) and helped refactor indexing process by usage of dictionaries
- Removed a lot of the unneccessary code and functions that were not needed, and revamped proccesses
- Compared queries and documents for Results.txt ensuring that words appeared in both for the document per query
- Conducted research on PYTREC and usage of Stemmers and implementation of TREC_EVAL and retrieval of MAP Scores

2. Tolu Emoruwa's Work...
- Developed Step 1 by removing stopWords and adding regex's for filtration
- Helped with understanding the ranking algorithm and debugging cosine ranking slowness
- Assisted in refining the ranking process for better retrieval accuracy
- Verified and analyzed results, ensuring MAP Scores were high enough for submission
- Contributed to the report write up with detailed explanations

3. Shacha Parker's Work...
- Refactored Step 2 implementation for efficiency and readability
- Designed functions for retrieving only TITLES and retrieving TITLES/TEXTS
- Conducted research comparing BM25 and COSINE SIM ranking algorithms
- Investigated and research why words are cut off (stemmers)
- Contributed to the report write up with detailed explanations

## Functionality Of Program:

## Running Instructions:


## Explaination Of Algorithms:
1. Step One Implementation (Preprocessing)
- 

2. Step Two Implementation (Indexing)

3. Step Three Implementation (Ranking & Retrieval)

## Mean Average Precision (MAP) Score:
Our final Mean Average Precison (MAP) Score is ~0.5 (exactly 0.49472) of how similar and accurate our measures are. This checks the correct and incorrect results of our Results.txt file (output from our code) and usage of PYTREC_EVAL to check that vs test.tsv file.