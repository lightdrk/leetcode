class Min_stack:
    def __init__(self):
        self.st = []
        self.min_st = []

    def push(self,val :int)-> None:
        self.st.append(val)
        if self.min_st and self.min_st[-1] < val:
            return
        self.min_st.append(val)

    def pop(self)->None:
        if self.st.pop() == self.min_st[-1]:
            self.min_st.pop()

    def top(self)->int:
        return self.st[-1]

    def getMin(self)-> int:
        if self.min_st:
            return self.min_st[-1]
        return 0

    def print_st(self):
        print(self.st)
        print(self.min_st)

st = Min_stack()
st.push(2)
st.push(0)
st.push(3)
st.push(0)
st.print_st()
print('get min -->',st.getMin())
print('pop -->',st.pop())
print('get min -->',st.getMin())
st.print_st()
print('pop -->',st.pop())
print('get min -->',st.getMin())

print('pop -->',st.pop())
print('get min -->',st.getMin())
st.print_st()


