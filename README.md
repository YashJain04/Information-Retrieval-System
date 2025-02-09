# Submission Details

## Students Information:
- Yash Jain : 300245571
- Tolu Emoruwa : 300230905
- Shacha Parker : 300235525

## Dividing Tasks Information:
1. Yash Jain's Work...
- Initial setup of project through GitHub and downloaded files and added documentation/comments throughout all the code
- Implementation of Ranking Algorithm BM25 (Step 3) and helped refactor indexing process by usage of dictionary methods and helped with COSINE SIM ranking implementation
- Removed a lot of the unneccessary code and functions that were not needed, and revamped proccesses, helped with the report write up, cleaned terminal output
- Compared queries and documents for Results.txt ensuring that words appeared in both for the document per query (resulting in a justifiable output)
- Conducted research on PYTREC, installed it and used it for evaluation, and usage of Stemmers and implementation of TREC_EVAL and retrieval of MAP Scores (calculated all MAP Scores and retrieved the average)
- Helped with creating sample of 100 vocabulary and retrieving top 10 scores for first 2 queries

2. Tolu Emoruwa's Work...
- Developed Step 1 by loading stopWords file, modifying tokenization function, removing stopWords and adding regex's for filtration of non-needed characters
- Helped with understanding the ranking algorithm and debugging cosine ranking slowness (implemented COSINE SIM but removed due to BM25 being the optimal algorithm and faster)
- Assisted in refining the ranking process for better retrieval accuracy (specifically step 3 and more)
- Verified and analyzed results, ensuring MAP Scores were high enough for submission and compared documents/queries ensuring words are relevant
- Contributed to the report write up with detailed explanations
- Helped with creating sample of 100 vocabulary and retrieving top 10 scores for first 2 queries

3. Shacha Parker's Work...
- Refactored Step 2 implementation for efficiency and readability
- Designed and implemented functions for retrieving only TITLES and retrieving TITLES/TEXTS, and compared MAP scores for HEAD results vs HEAD + TEXT results, and documented, commented, and added discussion
- Conducted research comparing BM25 and COSINE SIM ranking algorithms (why BM25 > COSINE SIM and why we should remove the implementation of COSINE SIM)
- Investigated and research why words are cut off (stemmers)
- Contributed to the report write up with detailed explanations and added deep documentation
- Helped with creating sample of 100 vocabulary and retrieving top 10 scores for first 2 queries

## Running Instructions:
Ensure the following is installed:
- Python Version on the host machine
- NLTK
- Tensorflow
- PYTREC_Eval
- Other missing dependencies that may arise/occur when mentioned in the terminal during the execution of the program

For execution:
1. Navigate to the `IR_Files` subfolder
2. Run the command `python3 main.py` or `python main.py` if you do not have Python 3 installed, but another version

## Functionality Of Program & Explaination Of Algorithms:
The `main.py` file contains our main program which is used for running the code. It does the following
- Sets the file paths
- Completes Step 0 (basically the code inside `parser.py` file) and calculates the time to do so
- Completes Step 1 (basically the code inside `preprocessor.py` file) and calculates the time to do so
- Completes Step 2 (basically the code inside `indexing.py` file) and calculates the time to do so
- Completes Step 3 (basically the code inside `ranking.py` file) and calculates the time to do so
- Completes Step 4 (writing results to file)
- Completes Step 5 (computing MAP scores through PYTREC_EVAL)

The `utils.py` file contains our utilities which is used for running the code. IT...
- This is a helper file that is used within `main.py` it creates progress bars for visualization in the terminal
- This file also has the `writeResults()` function which retrieves the top 1 score for the document for the specific associated query and writes the results to an output file called ***TopScoresAllQueries.txt***
- This file also has the `writeResultsTop10First2()` function which retrieves the top 10 scores for the document for the first 2 specific associated queries and writes the results to an output file called ***Top10AnswersFirst2Queries.txt***
- This file also has the `writeResultsAll()` function which retrieves all the scores for the document for all the specific associated queries and writes the results to an output file called ***AllScoresAllQueries.txt***

### 0. Step Zero Implementation (Parsing)
This step has it's functions and associated code within the parser.py file. This parser.py contains the 4 functions which help parse documents from the file (and this calls the document parsing function). It also helps parse queries from the file (and this calls the query parsing function). In essence, the purpose of this file is to read the JSON and extract information for both corpus.jsonl (documents) and queries.jsonl (queries). The data structures and algorithms used in this step are simple hashmaps that seperate the actual document number, title of the text, and the actual text body into 3 seperate keys, this is for documents. For queries, again another hashmap is used to seperate the query number and query title as keys.

This steps is before/mixed within the preprocessing (Step 1). The associated code for this step can be seen in the `parser.py` file.

### 1. Step One Implementation (Preprocessing)
Preprocessing is implemented through 2 steps (preprocessing documents) and (preprocessing queries) and is completed within the `preprocessing.py` file. This file has all the associated code and functions to complete the preprocessing step. The 2 seperate steps are highlighted below:

### 1.1 Preprocessing Documents
This step is for preprocessing documents and it is done by a few functions. In essence, we leverage a hashmap to extract the specific details about the document such as the title (which represents the HEAD key in the hashmap) and the body text (which represents the TEXT key in the hashmap). From here we simply preprocess the text within the hashmap and this includes the process of ***tokenization*** and ***stemming***. In tokenization, we utilize a regex to ensure that only alphabets are allowed, (this removes unnecessary text such as brackets, dashes, numbers, etc.). From here, we also leverage the stopWords.txt file which contains all the stopWords. We filter out any stop words from the documents. The stemming process simply utilizes a ***PorterStemmer()*** to reduce words to their root form and improve text normalization. This includes all the filtration, and from here we simply return the documents which are now cleaned and validated.

### 1.2 Preprocessing Queries
- This step is for preprocessing queries and it is done by the same similar process in which documents were validated. In a quick short summary, we leverage a hashmap to extract the specific text for the query which is simply stored as the title key. Note: We do not include the query number! Otherwise, this will filter out our queries incorrectly, and cause wrong results, as numbers are filtered returning invalid key values inside the hashmap. From there we simply, preprocess the text within the query which is the same process as preprocessing the text for documents (***tokenizing it and usage of stemmers***). We then return after all the filtration as the queries are now cleaned and validated.

This step's output is stored across 2 files and in here you can see the cleaned and validated files with stopWords removed and words that are stemmed as well as seperate entities (title and text) stored in (HEAD and text). The files are listed as below:
- `../Results_Scores/preprocessed_documents.json` (in the .gitignore because too large and can't push to github)
- `../Results_Scores/preprocessed_queries.json` (in the .gitignore because too large and can't push to github)

### 2. Step Two Implementation (Indexing)
In this step we start to build our inverted index from the cleaned and validated documents from STEP 1. We leverage a hashmap that efficiently maps each unique token to the documents in which it appears, along with the frequency of its occurrences. The `build_inverted_index` function constructs this index by iterating through the provided documents, ensuring quick lookup and retrieval of term-document associations. Additionally, the `calculate_document_lengths` function computes the length of each document, which is used when computing the BM25 score for ranking and retrieval. The process is done inside `indexing.py` and the output from this step can be seen in `../Results_Scores/inverted_index.json` (in the .gitignore because too large and can't push to github).

### 3. Step Three Implementation (Ranking & Retrieval)
In this step, we use our inverted index from STEP 2 to complete the ranking, scoring, and retrieval process much more ***efficiently***. With the `inverted_index`, we compute the document length as said before, which will be needed for the ***BM25 ranking score algorithm***. We then start our ranking process, which utilizes the BM25 ranking score algorithm to determine the most relevant documents for a given query. The BM25 ranking function assigns scores to documents based on term frequency, inverse document frequency, and document length normalization. Using the `BM25` class, we compute the **Inverse Document Frequency (IDF)** for each query term, ensuring that less frequent terms contribute more to the ranking. The **Term Frequency (TF)** component is adjusted using the `k1` and `b` parameters to balance term importance while considering document length. Once we have computed the BM25 scores for all relevant documents, we sort them in descending order to present the most relevant results first. Additionally, we apply a **score normalization function**, ensuring that the ranking values are scaled between 0 and 1, making them easier to interpret.

This step's output is stored in the `../Results_Scores/TopScoresAllQueries.txt` file and here you can see our final results. The associated code and functions for this step can be seen in the `ranking.py` file. This step also creates 2 more files `../Results_Scores/Top10AnswersFirst2Queries.txt` which is our top 10 scores for the first 2 queries and `../Results_Scores/AllScoresAllQueries.txt` which is our scores for all queries.

### 3.1 Justification of BM25 Algorithm Over Cosine Simularity 
We decided to leverage the BM25 Algorithm because it has a higher retrieval performance and also lead to faster processing times. When we implemented the COSINE SIM ranking algorithm, our code took around ~15-30 minutes to run. With the BM25 algorithm, our code was processed within seconds, thus we decided to finalize on the BM25 Algorithm and neglect the COSINE SIM algorithm.

## Mean Average Precision (MAP) Score:
Our final Mean Average Precison (MAP) Score is ~0.6 (exactly 0.59539) of how similar and accurate our measures are. This checks the correct and incorrect results of our `../Results_Scores/AllScoresAllQueries.txt` file (output from our code) and usage of PYTREC_EVAL to check that vs test.tsv file. The MAP score for every single document/query can be seen in the `MAPScores.json` file.

## Comparing Results (Title VS Title + Text)
We found that the MAP score was lower when we eliminated the body text ("TEXT") during preprocessing and kept only the title text ("TITLE") for the program to process beyond Step 1. With only the title text in the processed document, the MAP score was 0.38791. It's evident that the score was lowered by there being less text with which to match queries, causing the program to retrieve fewer relevant documents. Additionally, both the title and body text resulted in a better MAP score ~0.6 (exactly 0.59539).

The code needed to change the program to preprocess only the head text without the body is found in `main.py`. Searching the document for "head_only" will show three lines that have been commented out. If you un-comment them and comment out the original functions, it'll run preprocessing with only the head text.

## Discussion Of Results (Sample 100 Vocabulary and Top 10 Answers First 2 Queries)
... to be completed

## Files Included In The .gitignore
We have a few files in the .gitignore:
- DS._STORE (MAC OS File)
- Results_Scores/inverted_index.json (too large cannot push to github)
- Results_Scores/preprocessed_documents.json (too large cannot push to github)
- Results_Scores/preprocessed_queries.json (too large cannot push to github)
- Results_Scores/AllScoresAllQueries.txt (too large cannot push to github)
- IR_Files/__pycache__/ (not needed)