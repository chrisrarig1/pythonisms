from pythonisms import __version__
from pythonisms.linked_list_terartor import LinkedList


def test_version():
    assert __version__ == '0.1.0'

def test_linked_list():
    col = ('Ball', 'Bat','Base','Baseball')
    ll = LinkedList(col)
    final = []
    for i in ll:
        final.append(i)
    assert final == ['Ball', 'Bat','Base','Baseball']

def test_list_comp():
    col = ('Ball', 'Bat','Base','Baseball')
    ll = LinkedList(col)
    final = []
    for i in ll:
        j = i+'s'
        final.append(j.lower())
    assert final == ['balls', 'bats','bases','baseballs']

def test_type_comp():
    col = ['Ball', 'Bat','Base','Baseball']
    ll = LinkedList(col)
    assert list(ll) == col

def test_eq():
    ll1 = LinkedList(['hi','hello','hola'])
    ll2 = LinkedList(['hi','hello','hola'])
    assert ll1 == ll2

# def test_bool():
#     ll1 = LinkedList(['hi','hello','hola'])
#     assert ll1.head == True