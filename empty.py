# =====================================
# Defining functions here
# =====================================

def add(a, b):
  return a + b
def sub(a,b):
  return a - b
#=====================================
#Defining functions here
#=====================================

def test_add():
    assert add(2, 3) == 5
    assert add('boston', 'university') == 'bostonuniversity'


def test_sub():
    assert subtract(2, 3) == -1
    assert subtract(3, 2) == 1
