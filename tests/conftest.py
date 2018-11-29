from pytest import fixture

@fixture
def create_testfile():
    def _create_testfile(filename, line1, line2):
        with open(filename, 'w') as f:
            f.write(line1)
            f.write(line2)
    return _create_testfile

@fixture
def read_testfile():
    def _read_testfile(filename):
        with open(filename, 'r') as f:
            content = f.read()
        return float(content)
    return _read_testfile