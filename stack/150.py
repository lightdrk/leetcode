def eval(token):
    st = []
    operation = []
    for s in token:
        if s.isalnum():
            st.append(int(s))
        else:
            operation.append(s)
    print(st, operation)

eval(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
