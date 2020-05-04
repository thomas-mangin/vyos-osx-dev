import os
from glob import glob


def location():
    here = os.path.dirname(os.path.realpath(__file__))
    return os.path.abspath(os.path.join(here, 'data.py'))


def generate(folder):
    generated = [
        '# Do not modify this file is autogenerated',
        'data = {}'
    ]

    for fname in glob(f'{folder}/*'):
        name = os.path.basename(fname)
        content = open(fname, 'r').read()
        generated.append(f'data["{name}"] = """{content}"""')

    with open(location(), 'w') as f:
        f.write('\n\n'.join(generated))


def read(data, name):
    try:
        with open(os.path.join(data, name)) as f:
            return f.read()
    except Exception as OErr:
        try:
            from vyosextra.data import data
            return data[name]
        except ImportError:
            raise OErr
