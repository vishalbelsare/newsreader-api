#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals
from queries import CRUDQuery

class get_document_metadata(CRUDQuery):
    """ Get the metadata of a document
    """
    # https://knowledgestore.fbk.eu/nwr/worldcup-hackathon/resources?id=http://news.bbc.co.uk/sport2/hi/football/gossip_and_transfers/5137822.stm
    def __init__(self, *args, **kwargs):
        super(get_document_metadata, self).__init__(*args, **kwargs)
        self.query_title = 'Get document metadata'
        self.description = ('Get the metadata of a document, this includes title'
            ' and author where available and also a list of all the "mentions" '
            'it contains, which can be lengthy and not necessarily informative.'
            ' It uses the SPARQL DESCRIBE keyword which returns'
            ' a network not compatible with HTML display.')
        self.url = 'get_document_metadata'
        self.world_cup_example = 'get_document_metadata?uris.0=http://news.bbc.co.uk/sport2/hi/football/gossip_and_transfers/5137822.stm'
        self.cars_example = 'get_document_metadata?uris.0=http://www.newsreader-project.eu/data/cars/2003/01/04/47KW-0H00-01JV-737G.xml'
        self.ft_example = 'get_document_metadata?uris.0=http://www.newsreader-project.eu/data/2013/10/312013/10/312013/10/31/11779884.xml'
        self.wikinews_example = 'get_document_metadata?uris.0=http://en.wikinews.org/wiki/Obama,_Romney_spar_in_first_2012_U.S._presidential_debate'
        self.query_template = ("""{uri_0}""")
        self.count_template = ("""""")
        self.output = 'json'
        self.result_is_tabular = False
        self.action = "resources"

        self.jinja_template = 'table.html'

        self.headers = ['**output is a graph**']

        self.required_parameters = ["uris"]
        self.optional_parameters = []
        self.number_of_uris_required = 1

        self.query = self._build_query()

    def get_total_result_count(self, *args, **kwargs):
        """ Returns result count for query, exception for this describe query """
        return 0

    def parse_query_results(self):
        # TODO: nicely parsed needs defining; may depend on query
        """ Returns nicely parsed result of query. """
        return self.json_result
