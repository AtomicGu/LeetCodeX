s = "tocyjkdzcieoiodfpbgcncsrjbhmugdnojjddhllnofawllbhfiadgdcdjstemphmnjihecoapdjjrprrqnhgccevdarufmliqijgihhfgdcmxvicfauachlifhafpdccfseflcdgjnadfclvfmadvrnaaahahndsikzssoywakgnfjjaihtniptwoulxbaesqlkdank"
v = []
for i in range(len(s)):
    a = []
    for j in range(i + 1, len(s)):
        if s[j] > s[i]:
            a.append(j)
    v.append(a)

seqs = set()


def num_of_seqs(i, prefix=""):
    n = 0

    # 自身
    prefix = prefix + s[i]
    if prefix not in seqs:
        n += 1
        seqs.add(prefix)

    for j in v[i]:
        n += num_of_seqs(j, prefix)

    return n


n = 0
for i in range(len(s)):
    n += num_of_seqs(i)
    print(i)
print(n)

# ! 这种方法不能在比赛时间内算出结果
