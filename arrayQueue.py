import array


class FullError(Exception):
    pass


class ArrayQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = array.Array(maxsize)
        self.head = 0 #【下标】计量
        self.tail = 0

    def push(self, value):
        if len(self) >=self.maxsize:
            raise FullError('Full')
        self.array[self.head % self.maxsize] = value  #求余很关键
        self.head += 1

    def __len__(self):
        return self.head - self.tail

    def pop(self, value):
        value = self.array[self.tail % self.maxsize]
        self.array[self.tail % self.maxsize] = None
        self.tail += 1
        return value

def test_queue():
    import pytest    # pip install pytest
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)

    with pytest.raises(FullError) as excinfo:   # 我们来测试是否真的抛出了异常
        q.push(size)
    assert 'full' in str(excinfo.value)

    assert len(q) == 5

    assert q.pop() == 0
    assert q.pop() == 1

    q.push(5)

    assert len(q) == 4

    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5

    assert len(q) == 0





