import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def file1_path():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def file2_path():
    return 'tests/fixtures/file2.json'


@pytest.fixture
def file1_path_y():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def file2_path_y():
    return 'tests/fixtures/file2.yml'


def test_generate_diff_stylish(file1_path, file2_path):
    expected = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: {
            key: value
        }
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: too much
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
    group4: {
      - default: null
      + default: 
      - foo: 0
      + foo: null
      - isNested: false
      + isNested: none
      + key: false
        nest: {
          - bar: 
          + bar: 0
          - isNested: true
        }
      + someKey: true
      - type: bas
      + type: bar
    }
}"""
    assert generate_diff(file1_path, file2_path) == expected


def test_generate_diff_stylish_y(file1_path_y, file2_path_y):
    expected = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: {
            key: value
        }
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: too much
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
    group4: {
      - default: null
      + default: 
      - foo: 0
      + foo: null
      - isNested: false
      + isNested: none
      + key: false
        nest: {
          - bar: 
          + bar: 0
          - isNested: true
        }
      + someKey: true
      - type: bas
      + type: bar
    }
}"""
    assert generate_diff(file1_path_y, file2_path_y) == expected
