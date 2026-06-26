import os
import pandas as pd
import xml.etree.ElementTree as ET

def parse_medquad_xml(root_dir):
    qa_pairs = []

    
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".xml"):
                file_path = os.path.join(subdir, file)
                
                try:
                    tree = ET.parse(file_path)
                    root = tree.getroot()
                    
                    # Find all QAPair blocks in the XML
                    for qa_pair in root.findall('.//QAPair'):
                        question = qa_pair.find('Question').text
                        answer = qa_pair.find('Answer').text
                        
                        if question and answer:
                            qa_pairs.append({
                                'question': question.strip(),
                                'answer': answer.strip()
                            })
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")

    return pd.DataFrame(qa_pairs)

if __name__ == "__main__":
   
    dataset_path = "./MedQuAD-master" 
    
    print("Starting data extraction...")
    df = parse_medquad_xml(dataset_path)
    
    # Save to CSV for the Streamlit app to use
    df.to_csv("medquad_clean.csv", index=False)
    print(f"Success! Saved {len(df)} Q&A pairs to medquad_clean.csv")