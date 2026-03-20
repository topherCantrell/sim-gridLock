
class SVGMaker:

    def __init__(self, fname):

        self.parts = {}
        cur_part = None
        with open(fname) as f:
            for line in f:
                line = line.strip()
                if line == '-->':
                    break
                if line.startswith('####'):
                    i = line.find(':')
                    name = line[4:i].strip()
                    self.parts[name] = [line[i+1:].strip().split(' '), '']
                    cur_part = name
                elif cur_part:
                    self.parts[cur_part][1] += line

    def make_part(self, name, **kwargs):
        params, text = self.parts[name]
        if len(kwargs) != len(params):
            raise Exception(f'Incorrect number of parameters for part "{name}". Expected {params}.')
        for k, v in kwargs.items():
            if k not in params:
                raise Exception(f'Unknown parameter "{k}". Expected {params}.')
            if '%'+k+'%' in text:
                text = text.replace('%'+k+'%', str(v))
            else:
                if v:
                    text = text.replace('@@'+k+'@@', '')
                    text = text.replace('@@/'+k+'@@', '')
                else:
                    i = text.find('@@'+k+'@@')
                    j = text.find('@@/'+k+'@@', i)+len(k)+5
                    text = text[:i]+text[j:]        
        return text
