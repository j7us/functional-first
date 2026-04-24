from pymonad.tools import curry

# Задание 2.3.1
@curry(2)
def build_str(first, second):
    return first + ' ' + second


build_hello = build_str('Hello,')

print(build_hello('Egor'))
print(build_hello('Oleg'))



# Задание 2.3.2
@curry(4)
def build_hello_with_name_and_symbols(hello, delim, end, name):
    return hello + delim + ' ' + name + end

hello_with_name = build_hello_with_name_and_symbols('Hello', ',','!')

print(hello_with_name('Egor'))
print(hello_with_name('Oleg'))