from typing import NamedTuple

import ir_datasets
from ir_datasets.datasets.base import Dataset
from ir_datasets.formats import JsonlDocs, TrecXmlQueries


class IrDocument(NamedTuple):
    doc_id: str
    text: str

    def default_text(self):
        return self.text


class Streamer:
    def __int__(self):
        pass

    def path(self, force: bool):
        return ''


ir_datasets.registry.register('iranthology-ArMaFiRa',
                              Dataset(JsonlDocs(
                                  ir_datasets.util.fileio.RelativePath(streamer=Streamer(),
                                                                       path='/usr/lib/python3.8/site-packages/ir_datasets/datasets_in_progress/ir_documents.jsonl'),
                                  doc_cls=IrDocument, lang='en'),
                                  TrecXmlQueries(ir_datasets.util.fileio.RelativePath(streamer=Streamer(),
                                                                                      path='/usr/lib/python3.8/site-packages/ir_datasets/datasets_in_progress/ir_topics.xml'),
                                                 lang='en')))
