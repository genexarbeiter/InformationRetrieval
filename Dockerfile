FROM webis/tira-ir-datasets-starter:0.0.54

COPY ir.py /usr/lib/python3.8/site-packages/ir_datasets/datasets_in_progress/
COPY ir_documents.jsonl /usr/lib/python3.8/site-packages/ir_datasets/datasets_in_progress/
COPY ir_topics.xml /usr/lib/python3.8/site-packages/ir_datasets/datasets_in_progress/

ENTRYPOINT [ "/irds_cli.sh" ]
