from typing import NamedTuple

import ir_datasets
from ir_datasets.datasets.base import Dataset
from ir_datasets.formats import JsonlDocs, TrecXmlQueries


class IrDocument(NamedTuple):
    doc_id: str
    text: str

    def default_text(self):
        return self.text


ir_datasets.registry.register('iranthology-armafira', Dataset(
    JsonlDocs(ir_datasets.util.PackageDataFile(path='datasets_in_progress/ir_documents.jsonl'), doc_cls=IrDocument, lang='en'),
    TrecXmlQueries(ir_datasets.util.PackageDataFile(path='datasets_in_progress/ir_topics.xml'), lang='en')
))

