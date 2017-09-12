from urllib.parse import quote

from dulwich.porcelain import open_repo
import os.path
import csv
import datetime

onaji = None


class LoggerPlugin(object):
    def __init__(self, serializer=None):
        self._path = os.getenv('REPO_HOME', '.')
        self._home = os.path.join(self._path, ".onaji")

        if not os.path.exists(self._home):
            os.mkdir(self._home)

        repo = open_repo(self._path)
        branch = repo.refs.read_ref('HEAD').decode('utf-8').rsplit('/', 1)[-1]
        self._commit = open_repo(self._path).head()
        self._file = open(os.path.join(self._home, branch + '.' + self._commit.decode('utf-8') + ".csv"), 'w')
        self._writer = csv.writer(self._file)
        self._testname = None
        if serializer:
            self._serializer = serializer
        else:
            self._serializer = lambda x: quote(repr(x))

    def pytest_runtest_setup(self, item):
        self._testname = item.name

    def pytest_unconfigure(self, config):
        self._file.close()

    def log(self, key, *values):
        """
        Log an item

        Args:
            key: 
            values: 

        """
        for v in values:
            self._writer.writerow([self._testname, quote(key), self._serializer(v)])


def pytest_configure(config):
    global onaji
    onaji = LoggerPlugin()
    config.pluginmanager.register(onaji)