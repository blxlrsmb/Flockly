

import sys
import os
import imp
import uuid
from BeautifulSoup import BeautifulStoneSoup
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')


class YouAreAnIdiotBeautifulSoup:
    def has_key(self, s):
        return True

    def get(self, s):
        return []


class UglySoup(BeautifulStoneSoup):
    NESTABLE_TAGS = YouAreAnIdiotBeautifulSoup()


getUniqueVarName = lambda: 'var_' + uuid.uuid4().hex

def getBlockTypes(s):
    """ feed xml string, return list of included block type"""
    soup = UglySoup(s, convertEntities=UglySoup.HTML_ENTITIES)
    names = [x['type'].partition('_')[0] for x in soup.findAll('block')]
    return names

def translate(s):
    """ feed xml string, return python code"""
    ret = ''
    soup = UglySoup(s, convertEntities=UglySoup.HTML_ENTITIES)
    var_titles = soup.findAll('title', attrs={'name': 'VAR'})
    variables = set([i.text for i in var_titles])  # remove duplicated
    for i in soup.findAll('variable', attrs={'name': 'VAR'}):
        i.setString(i['data'])
        var_titles.append(i)
# rename all variables to `var_***' using uuid
    for i in variables:
        _var_name = getUniqueVarName()
        for j in filter(lambda x: x.text == i, var_titles):
            j.setString(_var_name)
    for i in set([i.text for i in var_titles]):
        ret += (i + ' = None\n')
    for i in soup.xml.findAll('block', recursive=False):
        ret += blockToCode(i)
    return ret


def blockToCode(block):
    module_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
            './', block['type'].partition('_')[0] + '.py')
    module = imp.load_source('', module_file)
    ret = apply(getattr(module, block['type']), (block, )) + '\n'
    _next = block.find('next', recursive=False)  # recursive
    if _next:
        ret += blockToCode(_next.block)
    if ret.endswith('\n'):
        ret = ret[0:-1]
    return ret
