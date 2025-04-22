import os
import pandas as pd
from xml2json import xml2json

os.makedirs("data",exist_ok=True)


xml2json("../Webis-data/extracted/articles-training-byarticle-20181122.xml","data/articles-training-byarticle.jsonl")
xml2json("../Webis-data/extracted/articles-test-byarticle-20181207.xml","data/articles-test-byarticle.jsonl")
xml2json("../Webis-data/extracted/articles-training-bypublisher-20181122.xml","data/articles-training-bypublisher.jsonl")
xml2json("../Webis-data/extracted/articles-test-bypublisher-20181212.xml","data/articles-test-bypublisher.jsonl")

df = pd.read_xml("../Webis-data/extracted/ground-truth-training-byarticle-20181122.xml")
df.to_json("data/ground-truth-training-byarticle.jsonl",orient="records",lines=True)

df = pd.read_xml("../Webis-data/extracted/ground-truth-training-bypublisher-20181122.xml")
df.to_json("data/ground-truth-training-bypublisher.jsonl",orient="records",lines=True)

df = pd.read_xml("../Webis-data/extracted/ground-truth-test-bypublisher-20181212.xml")
df.to_json("data/ground-truth-test-bypublisher.jsonl",orient="records",lines=True)

df = pd.read_xml("../Webis-data/extracted/ground-truth-test-byarticle-20181207.xml")
df.to_json("data/ground-truth-test-byarticle.jsonl",orient="records",lines=True)