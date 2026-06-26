import json
import pandas as pd

def filter_arxiv():
    input_file = 'arxiv-metadata-oai-snapshot.json'
    output_file = 'cs_papers.csv'
    count = 0
    data = []

    print("Reading and filtering ArXiv dataset...")
    with open(input_file, 'r') as f:
        for line in f:
            item = json.loads(line)
            # We only want Computer Science papers
            if 'cs.' in item['categories']:
                data.append({
                    'title': item['title'],
                    'abstract': item['abstract'],
                    'doi': item.get('doi', 'N/A')
                })
                count += 1
            
            
            if count >= 10000:
                break

    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Done! Created {output_file} with {len(df)} records.")

if __name__ == "__main__":
    filter_arxiv()