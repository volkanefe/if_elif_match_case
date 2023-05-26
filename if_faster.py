from timeit import timeit


def test_if(text: str):
    if text == 'a':
        ...
    if text == 'b':
        ...
    if text == 'c':
        ...


def test_if_else(text: str):
    if text == 'a':
        ...
    elif text == 'b':
        ...
    elif text == 'c':
        ...
    else:
        ...
    
def test_match_case(text: str):
    match text:
        case 'a':
            ...
        case 'b':
            ...
        case 'c':
            ...
        case _:
            ...



if __name__ == '__main__':
    letter: str = 'a'

    if_chain_time: float = timeit('test_if(letter)', globals=globals())
    if_else_chain_time: float = timeit('test_if_else(letter)', globals=globals())
    if_match_case_time: float = timeit('test_match_case(letter)', globals=globals())

    print("test_if : ", round(if_chain_time, 4))
    print("test_if_else : ", round(if_else_chain_time, 4))
    print("test_match_case :", round(if_match_case_time, 4))
