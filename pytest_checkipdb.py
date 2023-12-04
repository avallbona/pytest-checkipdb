
import pytest
import ast


def pytest_addoption(parser):
    group = parser.getgroup('general')
    group.addoption(
        '--cipdb',
        action='store_true',
        dest='check_ipdb',
        help='perform ipdb sanity check on .py files'
    )


def pytest_collect_file(parent, path):
    config = parent.config
    if path.ext != '.py' or not config.option.check_ipdb:
        return
    if hasattr(CheckIpdbItem, "from_parent"):
        return CheckIpdbItem.from_parent(parent, fspath=path)
    else:
        return CheckIpdbItem(path, parent)


class CheckIpdbItem(pytest.Item, pytest.File):

    def __init__(self, fspath, parent):
        """fixing the raw content when instantiating the item

        :param fspath:
        :param parent:
        """
        self.raw_content = fspath.open().read()
        super(CheckIpdbItem, self).__init__(fspath, parent=parent)

    def runtest(self):
        t = ast.parse(self.raw_content)
        Visitor().visit(t)

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(CheckIpdbError):
            return '{} in file {}'.format(excinfo.value.args[0], self.fspath)
        return super(CheckIpdbItem, self).repr_failure(excinfo)

    def reportinfo(self):
        return self.fspath, -1, "cipdb-check"


class CheckIpdbError(Exception):
    """ indicates an error during cipdb checks. """


class Visitor(ast.NodeVisitor):

    check_functions = ['ipdb', 'pdb', 'set_trace', 'breakpoint']

    def visit_Call(self, node):
        try:
            object_to_evaluate = node.func
            try:
                attribute_to_evaluate = node.func.id
            except AttributeError:
                attribute_to_evaluate = node.func.attr
            for item in self.check_functions:
                if attribute_to_evaluate == item:
                    line_number = object_to_evaluate.lineno
                    col_number = object_to_evaluate.col_offset
                    raise CheckIpdbError('Detected {} call at line {} col {}'.format(item, line_number, col_number))
        except AttributeError:
            pass
        ast.NodeVisitor.generic_visit(self, node)
