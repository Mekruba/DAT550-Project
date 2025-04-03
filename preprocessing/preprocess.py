import os
from xml2json import xml2json

os.makedirs("data",exist_ok=True)

xml2json("../Webis-data/extracted/articles-training-byarticle-20181122.xml","data/articles-training-byarticle.jsonl")
xml2json("../Webis-data/extracted/articles-test-byarticle-20181207.xml","data/articles-test-byarticle.jsonl")
xml2json("../Webis-data/extracted/articles-training-bypublisher-20181122.xml","data/articles-training-bypublisher.jsonl")
xml2json("../Webis-data/extracted/articles-test-bypublisher-20181212.xml","data/articles-test-bypublisher.jsonl")