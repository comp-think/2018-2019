# -*- coding: utf-8 -*-
# Copyright (c) 2018,
# Sebastian Barzaghi <sebastian.barzaghi@studio.unibo.it>,
# Martina Dello Buono <martina.dellobuono@studio.unibo.it>,
# Fabio Mariani <fabio.mariani6@studio.unibo.it>,
# Silvio Peroni <silvio.peroni@unibo.it>
#
# Permission to use, copy, modify, and/or distribute this software for any purpose
# with or without fee is hereby granted, provided that the above copyright notice
# and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
# REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT,
# OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
# DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
# SOFTWARE.

# The following importing line is used to include in the definition of this class
# the particular functions implemented by a group. The 'my_test_group' module specified
# here is just a placeholder, since it defines only the signature of the various
# functions but it returns always None.
from my_test_group import *

from csv import DictReader
from re import search
from anytree import Node
from collections import Counter
from networkx import DiGraph


class ScholarlyNetworkEngine(object):
    def __init__(self, metadata_file_path, citation_file_path):
        self.sse = ScholarlySearchEngine(metadata_file_path)
        self.data = process_citation_data(citation_file_path)

    def citation_graph(self):
        return do_citation_graph(self.data, self.sse)

    def coupling(self, doi_1, doi_2):
        return do_coupling(self.data, self.sse, doi_1, doi_2)

    def aut_coupling(self, aut_1, aut_2):
        return do_aut_coupling(self.data, self.sse, aut_1, aut_2)

    def aut_distance(self, aut):
        return do_aut_distance(self.data, self.sse, aut)

    def find_cycles(self):
        return do_find_cycles(self.data, self.sse)

    def cit_count_year(self, aut, year):
        return do_cit_count_year(self.data, self.sse, aut, year)


class ScholarlySearchEngine(object):
    """This is the class implementing the scholarly search engine, which was the project
    assigned to students of the Computational Thinking and Programming 2017/2018 course.
    It includes six methods: the constructor (__init__), search, pretty_print, publication_tree,
    top_ten_authors, and coauthor_network."""
    def __init__(self, source_csv_file_path):
        self.data = None

        with open(source_csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = DictReader(csvfile)
            self.data = [dict(x) for x in reader]

    def search(self, query, col, is_number, partial_res=None):
        result_list = list()
        if partial_res:
            data = partial_res
        else:
            data = self.data

        if " and " in query:
            subquery = query.split(' and ', 1)
            query1 = subquery[0]
            query2 = subquery[1]
            result_query1 = self.search(query1, col, is_number, partial_res)
            return self.search(query2, col, is_number, result_query1)
        elif " or " in query:
            subquery = query.split(' or ', 1)
            query1 = subquery[0]
            query2 = subquery[1]
            or_list = self.search(query1, col, is_number, partial_res)
            or_list_2 = self.search(query2, col, is_number, partial_res)
            for i in or_list_2:
                if i not in or_list:
                    or_list.append(i)
            return or_list
        elif query.startswith("not "):
            subquery = query.replace('not ', '', 1)
            if is_number:
                subquery = int(subquery)
                for row in data:
                    if subquery != int(row[col]):
                        result_list.append(row)
                return result_list
            elif col == 'authors' or 'categories' or 'keywords':
                for row in data:
                    split_list = row[col].split('; ')
                    if all(subquery.lower() not in it.lower() for it in split_list):
                        result_list.append(row)
                return result_list
            else:
                for row in data:
                    if subquery.lower() not in row[col].lower():
                        result_list.append(row)
                return result_list
        elif "*" in query:
            pattern = (query.lower()).replace('*', '[\w\s\W]*')
            if col == 'authors' or 'categories' or 'keywords':
                for row in data:
                    split_list = row[col].split('; ')
                    for it in split_list:
                        if search(pattern, it.lower()):
                            result_list.append(row)
                return result_list
            else:
                for row in data:
                    if search(pattern, row[col].lower()):
                        result_list.append(row)
            return result_list
        elif query.startswith("< "):
            if is_number:
                query = int(query.replace('< ', '', 1))
                for row in data:
                    if int(row[col]) < query:
                        result_list.append(row)
                return result_list
            elif col == 'authors' or 'categories' or 'keywords':
                query = query.replace('< ', '', 1)
                for row in data:
                    split_list = row[col].split('; ')
                    if any(it.lower() < query.lower() for it in split_list):
                        result_list.append(row)
                return result_list
            else:
                query = query.replace('< ', '', 1).lower()
                for row in data:
                    if row[col].lower() < query:
                        result_list.append(row)
                return result_list
        elif query.startswith("> "):
            if is_number:
                query = int(query.replace('> ', '', 1))
                for row in data:
                    if int(row[col]) > query:
                        result_list.append(row)
                return result_list
            elif col == 'authors' or 'categories' or 'keywords':
                query = query.replace('> ', '', 1)
                for row in data:
                    split_list = row[col].split('; ')
                    if any(it.lower() > query.lower() for it in split_list):
                        result_list.append(row)
                return result_list
            else:
                query = query.replace('> ', '', 1).lower()
                for row in data:
                    if row[col].lower() > query:
                        result_list.append(row)
                return result_list
        elif query.startswith("<= "):
            if is_number:
                query = int(query.replace('<= ', '', 1))
                for row in data:
                    if int(row[col]) <= query:
                        result_list.append(row)
                return result_list
            elif col == 'authors' or 'categories' or 'keywords':
                query = query.replace('<= ', '', 1)
                for row in data:
                    split_list = row[col].split('; ')
                    if any(it.lower() <= query.lower() for it in split_list):
                        result_list.append(row)
                return result_list
            else:
                query = query.replace('<= ', '', 1).lower()
                for row in data:
                    if row[col].lower() <= query:
                        result_list.append(row)
                return result_list
        elif query.startswith(">= "):
            if is_number:
                query = int(query.replace('>= ', '', 1))
                for row in data:
                    if int(row[col]) >= query:
                        result_list.append(row)
                return result_list
            elif col == 'authors' or 'categories' or 'keywords':
                query = query.replace('>= ', '', 1)
                for row in data:
                    split_list = row[col].split('; ')
                    if any(it.lower() >= query.lower() for it in split_list):
                        result_list.append(row)
                return result_list
            else:
                query = query.replace('>= ', '', 1).lower()
                for row in data:
                    if row[col].lower() >= query:
                        result_list.append(row)
                return result_list
        elif is_number:
            query = int(query)
            for row in data:
                if int(row[col]) == query:
                    result_list.append(row)
            return result_list
        elif col == 'authors' or 'categories' or 'keywords':
            for row in data:
                split_list = row[col].split('; ')
                if any(query.lower() in it.lower() for it in split_list):
                    result_list.append(row)
            return result_list
        else:
            for row in data:
                if query.lower() in row[col].lower():
                    result_list.append(row)
            return result_list

    def pretty_print(self, result_data):
        pretty_list = list()

        for row in result_data:
            pretty_item = ScholarlySearchEngine.__pretty_row(row)
            pretty_list.append(pretty_item)

        return pretty_list

    @staticmethod
    def __pretty_row(row):
        authors = row['authors'].split('; ')
        for position, name in enumerate(authors):
            splitname = name.split(', ')
            na = splitname[0]
            surname = splitname[1]
            if ' ' in na:
                na = na.split(' ')
                for pos, item in enumerate(na):
                    na[pos] = item[0]
                na = ''.join(na)
            else:
                na = na[0]
            final_name = surname + ' ' + na
            authors[position] = final_name
        pretty_authors = ', '.join(authors)
        pretty_item = pretty_authors + '. ' + '(' + row['year'] + ')' + '. ' + row['title'] + '. ' + row[
            'journal'] + ' ' + row['volume'] + '. ' + 'https://doi.org/' + row['doi']
        return pretty_item

    def publication_tree(self, author):
        root = Node(author)

        dict_years = dict()
        for row in self.data:
            if author in row['authors']:
                child = row['year']
                if child not in dict_years:
                    nodeyear = Node(child, parent=root)
                    dict_years[child] = nodeyear
                else:
                    nodeyear = dict_years[child]

                pretty_item = ScholarlySearchEngine.__pretty_row(row)
                Node(pretty_item, parent=nodeyear)
        return root

    def top_ten_authors(self):
        authors_list = list()

        for row in self.data:
            authors_list.extend(row['authors'].split('; '))

        return Counter(authors_list).most_common(10)

    def coauthor_network(self, author):
        coauthors = list()
        coauthor_network = DiGraph()
        coauthor_network.add_node(author)

        for row in self.data:
            if author in row['authors']:
                coauthors.extend(row['authors'].split('; '))
                coauthors.remove(author)
        counted_coauthors = Counter(coauthors).items()

        for name, count in counted_coauthors:
            coauthor_network.add_edge(author, name, co_authored_papers=count)

        return coauthor_network
