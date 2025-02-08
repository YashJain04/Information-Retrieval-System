import csv
import sys
import json
import datetime
import time
from ranking import normalize_scores

dataset = "scidocs"

def convert_tsv_to_qrels(tsv_path, qrels_path):
    with open(tsv_path, 'r', encoding='utf-8') as infile, open(qrels_path, 'w', encoding='utf-8') as outfile:
        tsv_reader = csv.DictReader(infile, delimiter='\t')
        for row in tsv_reader:
            outfile.write(f"{row['query-id']} 0 {row['corpus-id']} {row['score']}\n")

def progress_bar(current, total, bar_length=50):
    progress = current / total
    block = int(bar_length * progress)
    bar = '█' * block + '-' * (bar_length - block)
    percent = progress * 100
    text = f"\r{percent:.2f}%|{bar}| {current}/{total}"
    sys.stdout.write(text)
    sys.stdout.flush()

def writeResults(results_file, queries, bm25):
    beir_results = {}
    results_timestamp = "run-name"
    count = 1

    with open(results_file, 'w') as output_file:
        for query in queries:
            query_id = query['num']
            query_terms = query['title']
            progress_bar(count, len(queries))
            ranked_docs = bm25.rank_documents(query_terms)
            normalized_ranked_docs = normalize_scores(ranked_docs)
            count += 1

            if normalized_ranked_docs:  # Ensure there's at least one result
                top_doc_id, top_score = normalized_ranked_docs[0]  # Get only the top result

                if 'json' in results_file:
                    beir_results[query_id] = [(top_doc_id, top_score)]
                else:
                    result_line = f"{query_id} Q0 {top_doc_id} 1 {top_score} {results_timestamp}\n"
                    output_file.write(result_line)

        if 'json' in results_file:
            json.dump(beir_results, output_file, indent=4)

def save_results(results, output_file):
    beir_results = {}

    for query_id, docs in results.items():
        beir_results[query_id] = [(doc_id, score) for doc_id, score in docs.items()]

    with open(output_file, 'w') as file:
        json.dump(beir_results, file, indent=4)


#convert_tsv_to_qrels(dataset + '/qrels/test.tsv', dataset + '/qrels/test.qrels')
