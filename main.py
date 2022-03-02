def solution(n, k):
    st = []
    for idx, val in enumerate(n):
        while st and st[-1] < val and k > 0:
            st.pop()
            k -= 1
        if k == 0:
            st.extend([x for x in n[idx:]])
            break
        st.append(val)
    st = (st[:-k] if k > 0 else st)
    return ''.join(st)

solution("4177252841", 4)