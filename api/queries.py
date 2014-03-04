class QuerySupplier:
    _report = ''
    _param = ''
    _queries = {} 

    def __init__(self, report):
        self.initQueries()
        self._report = report

    def query(self, param):
        if param not in self._queries.keys():
            return self._queries['default']

        return self._queries[self._report] % param

    def createSearchQuery(self):
        qry = """
            SELECT *
            FROM bdb_attrib
            WHERE value LIKE '%s'
        """

        return qry

    def createTableQuery(self):
        qry = """
            SELECT *
            FROM bdb_ob
            WHERE name LIKE '%s'
        """

        return qry


    def initQueries(self):
        qry = "SELECT 'Command unknown.'"
        self._queries = {'default' : qry}

        qry = self.createSearchQuery()
        self._queries['search'] = qry

        qry = self.createTableQuery()
        self._queries['table'] = qry


