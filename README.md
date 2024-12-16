# Semantic Analyser Records Retriever

This repository contains very basic Python scripts that retrieve XML metadata records from the Blue Cloud GeoDAB Catalogue Service For the Web service. 

It has downloaded all 156,717 publicly visible records and stored them in folders of 10,000 records each. This is to prevent systems failing to load directories with even larger file numbers in them.

Also in this repository are some basic file moving scripts that find records containing certain text phrases and moving them to specified folders. This is to separate out systematically-generated records, such as the _paleoclimatlog_ records.