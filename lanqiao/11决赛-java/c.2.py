s = "tocyjkdzcieoiodfpbgcncsrjbhmugdnojjddhllnofawllbhf\
iadgdcdjstemphmnjihecoapdjjrprrqnhgccevdarufmliqij\
gihhfgdcmxvicfauachlifhafpdccfseflcdgjncadfclvfmad\
vrnaaahahndsikzssoywakgnfjjaihtniptwoulxbaeqkqhfwl"
v = [1] * len(s)

for i in range(len(s)):
    for j in range(i):
        if s[j] < s[i]:
            v[i] += v[j]
        if s[j] == s[i]:
            v[i] = 0  # * 太6了

print(sum(v))

# 3616159
