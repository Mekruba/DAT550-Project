from lxml import etree
import pandas as pd
import argparse
import os
import sys
import time
import json



def xml2json(xml_file, output_file=None, chunk_size=1000):
    """Convert XML to JSONL with memory-efficient streaming"""

    start_time = time.time()


    if not output_file:
        basename = os.path.splitext(xml_file)[0]
        output_file = f"{basename}.jsonl"
    
    # Process articles in chunks and write immediately
    with open(output_file, 'w', encoding='utf-8') as f:
        articles_buffer = []
        
        for _, element in etree.iterparse(xml_file, tag="article"):
            try:
                # Extract text efficiently (avoid XPath if possible)
                text_content = []
                for text in element.itertext():
                    if text.strip():
                        text_content.append(text.strip())
                
                article = {
                    "id": element.get("id"),
                    "published-at": element.get("published-at"),
                    "title": element.get("title"),
                    "content": " ".join(text_content),
                }
                articles_buffer.append(article)
                
                # Write in chunks to avoid memory buildup
                if len(articles_buffer) >= chunk_size:
                    for record in articles_buffer:
                        f.write(json.dumps(record, ensure_ascii=False) + '\n')
                    articles_buffer.clear()
                
            finally:
                # Crucial memory cleanup
                element.clear()
                while element.getprevious() is not None:
                    del element.getparent()[0]
        
        # Write remaining articles
        for record in articles_buffer:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')

    print(f"Success! Converted {xml_file} to {output_file}")

    end_time = time.time()
    ex_time = end_time - start_time
    print(f"Execution time: {ex_time:.2f} seconds")

    return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Filepath of XML to be parsed")
    parser.add_argument("-o","--output", help="outputname")
    
    args = parser.parse_args()


    xml2json(args.input_file,args.output)

    
    sys.exit(0)

if __name__ == "__main__":
    main()