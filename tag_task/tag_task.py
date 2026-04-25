from pymonad.tools import curry

# Задание 3.1
@curry(2)
def tag(tag_name, value):
    return '<' + tag_name + '>' + value + '</' + tag_name + '>'

bold_tag = tag('b')
italic_tag = tag('i')

print(bold_tag('val'))
print(italic_tag('val'))


# Задание 3.2
@curry(3)
def tag_with_attr(tag_name, attr, value):
    res = '<' + tag_name

    for k, v in attr.items():
        res += ' ' + k + '="' + v + '"'

    res += '>' + value + '</' + tag_name + '>'
    return res

print(tag_with_attr('li', {'class': 'list-group'}, 'item 23'))

