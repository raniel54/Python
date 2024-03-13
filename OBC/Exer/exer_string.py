# Substituindo caractere repetido

string = "fifa 22"
char = string[0].lower()
name = string.replace(char, '$')
name = char + name[1:]
print(name)

# Troca de caracteris

st1 = 'cab ' #zyb
st2 = 'zyx'  #cax

new_st1 = st2[:2] + st1[2]
new_st2 = st1[:2] + st2[2]
print(new_st1)