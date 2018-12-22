## Project: Scholarly Network Engine

This directory contains some files that are useful for the implementation of the project of the course. In particular:

* The file [`sne.py`](https://comp-think.github.io/2018-2019/project/sne.py) contains the implementation of the class `ScholarlyNetworkEngine` that has been presented during the course. You have to reuse it as it is without modifying anything except the import statement which is declared in the very first line. Currently, it is importing all the functions defined in another file, i.e. `my_test_group.py`, which is a stub implementation of the functions you have to implement for developing the project - see next point.
* The file [`my_test_group.py`](https://comp-think.github.io/2018-2019/project/my_test_group.py) is a stub implementation containing the signature (i.e. the functions definition without any code in it) of all the functions you have to implement. These functions are then reused in the class `ScholarlyNetworkEngine`. Of course it is possible to add even additional functions to this file if you want. The only important thing is that the seven functions used in the aforementioned class are defined.
* The file [`execution_example.py`](https://comp-think.github.io/2018-2019/project/execution_example.py) is an example of how I will use the class `ScholarlyNetworkEngine` (and, thus, your code) for testing the various methods for searching and providing data. You can use similar instruction to test the various methods of the class that have been implemented by means of your functions. Of course, you are free to run additional (and even complex) search queries so as to properly test your project. The instruction contained in this file can be run by using the Python 3 interpreter in the shell (`python3 execution_example.py`). Note that currently the class does not work as expected since it is using the functions implemented in `my_test_group.py`, that return *None*.
* The files [`metadata_sample.csv`](https://comp-think.github.io/2018-2019/project/metadata_sample.csv) and [`citation_sample.csv`](https://comp-think.github.io/2018-2019/project/metadata_sample.csv) are comma-separated value (CSV) documents containing a sample of the data that will be used in the evaluation of your project. It is a quite small (but complete) dataset, that allows you to test properly your project.
 
 For your convenience, you should download all these files and put them in the same directory. It is worth mentioning that the description of all the functions is already provided in the [slides that introduce the project](https://comp-think.github.io/2018-2019/slides/14%20-%20Project.html). You can use the information contained there as the official documentation of the various functions.
 
 As a reminder, your project (i.e. the implementation of the seven functions including any additional ancillary function developed, if any) must be included in a single file named after your group - e.g. I used `my_test_group.py` which represents my fictional group (i.e. *My Test Group*) in the aforementioned examples. Your file should be sent by email to [silvio.peroni@unibo.it](mailto:silvio.peroni@unibo.it), from your University email account, two days before the exam session session - e.g. you have to send the project by the 23rd of January 2019 for discussing it in the session of the 25th of January 2019. As a general rule, all the members of the group must attend the session - no exception.

### Scholarly Search Engine: constructor and methods

**ScholarlySearchEngine(source_csv_file_path)**

It is a class that takes in input the path of a file in a particular format (CSV) and allows one to run particular search operations.

The input CSV file describes some metadata of existing scholarly articles published in a few academic journals, according to the following structure:

<table>
    <tr><th>title</th><th>authors</th><th>doi</th><th>abstract</th><th>categories</th><th>keywords</th><th>journal</th><th>volume</th><th>references</th><th>figures</th><th>tables</th><th>year</th></tr><tr><td>The appropriation of GitHub for curation</td><td>Yu, Wu; Na, Wang; Jessica, Kropczynski; John M., Carroll </td><td>10.7717/peerj-cs.134</td><td>GitHub is a widely used online collaborative software [...]</td><td>Human-Computer Interaction; Software Engineering</td><td>    Curation; GitHub; Appropriation</td><td>PeerJ Computer Science</td><td>3</td><td>36</td><td>1</td><td>1</td><td>2017</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
    <tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr>
</table>

<hr />

**do_search(query, col, is_number, partial_res=None)**

Parameters:
* query: the textual query (type: string);
* col: the name of the column of the data in which to search (type: string);
* is_number: says if the content of the column (and, implicitly, of the query) should be interpreted as numbers instead of simple strings (type: boolean);
* partial_res: if not None, they are a reduced set of data on which the query should be applied.

Return a selection of the data which answer to the query. All searches are case insensitive – e.g. searching for "World" will match also strings that contain "world". 

The query is a string that actually can also contain a quite complex set of operations, according to the following ones:

* boolean operator 'or': <operator> <tokens>;
* boolean operator 'and' and 'or': <tokens 1> <operator> <tokens 2>;
* comparison operator '<', '>', '<=', '>=': <operator> <tokens>.

Examples:

1. "World Wide Web": returns all the rows that contain "World Wide Web" in the field specified by the parameter `col`;
2. "World Wide Web and not Artificial Intelligence": returns all the rows that contain "World Wide Web" and do not contain "Artificial Intelligence" in the field specified by the parameter `col`; 
3. "< 2016 or > 2017": returns all the rows that contain a value lesser than "2016" or greater than "2017" in the field specified by the parameter `col`.

In addition, multiple wildcards "\*" can be used, e.g. "World\*Web" looks for all the string that matches with the word "World" followed by zero or more characters, followed by the word "Web" (examples: "World Wide Web", "World Spider Web", etc.).

If the parameter `partial_res` is specified, the search is executed on it instead of on the full dataset.

<hr />

**pretty_print(result_data)**

Parameters:

* result_data: the set of data returned by a previous run of the method `search`.

Return a list of strings for each of the results contained in `result_data` according to the following format: `<Family Name 1> <Given Name Initials 1>, [...], <Family Name N> <Given Name Initials N>. (<year>). <title>. <journal> <volume>. https://doi.org/<doi>*`

Example: `Wu Y, Wang N, Kropczynski J, Carroll JM. (2017) The appropriation of GitHub for curation. PeerJ Computer Science 3. https://doi.org/10.7717/peerj-cs.134`

<hr />

**publication_tree(author)**

Parameters:

* author: the complete name (i.e. "Given Name, Family Name") of the author for which one wants to retrieve its publication tree.

Return all the publications written by such author described by the following tree:

* root node: author name;
* children of root node: as many node as many years of author's publication;
* children of an year node: the result of the do_pretty_print function applied to the particular article written by the author and published in that year.

<hr />

**top_ten_authors()**

Return a list of tuples with two items each, where the first item is a string representing the author full name and the second item is the number of papers it has published.

The tuple in the list are sorted in descending order, starting from the author with most publication. 

<hr />

**coauthor_network(author)**

Parameters:

* author: the complete name (i.e. "Given Name, Family Name") of the author for which one wants to retrieve its coauthor network.

Return a graph having a central node for the input author and a series of additional connected nodes for each other person who co-authored a paper with the input author, where the weight of the edge connecting the input author with his co-author is the number of paper they have co-authored together.
