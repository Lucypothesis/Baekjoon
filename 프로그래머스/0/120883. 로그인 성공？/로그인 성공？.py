import itertools

def solution(id_pw, db):
    db_1 = list(itertools.chain.from_iterable(db))
    if id_pw in db:
        answer = 'login'
    elif id_pw[0] in db_1:
            answer = 'wrong pw'
    else:
        answer = 'fail'
    return answer