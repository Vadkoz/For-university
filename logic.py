print('\n\nВводити треба тільки правильні формули, кожна операція повинна бути в окремих дужках. \n'
      'Вся формула теж має бути в дужках. Наприклад (a&(b|((-b)&(-c)))), (((x&(y|(-x)))@z)^(((a&z)^x)|(-y))). \n'
      'Вводити можна довільну кількість змінних великими та малими латинськими буквами, але по одній букві на змінну.\n'
      'Опис символів: диз"юнкція "|", кон"юнкція "&", ксор "^", заперечення "-", еквівалентність "@", імплікація ">"\n')
query = input('Введіть формулу:\n')

# query = '(a&(b|((-b)&(-c))))'
# query = '(((x&(y|(-x)))@z)^(((a&z)^x)|(-y)))'

print('Формула: ', query)
def change_oper(oper, sybmols):
    a, b = sybmols[0].replace('(', ''), sybmols[1].replace(')', '')
    if oper == '|':
        return '[' + a + '*' + b + '+' + a + '+' + b + ']'
    if oper == '&':
        return '[' + a + '*' + b + ']'
    if oper == '^':
        return '[' + a + '+' + b + ']'
    if oper == '-':
        return '[' + b + '+' + '1' + ']'
    if oper == '@':
        return '[' + a + '+' + b + '+' + '1' + ']'
    if oper == '>':
        return '[' + a + '*' + b + '+' + a + '+' + '1' + ']'

def to_bin(query):
    operators = ['|', '&', '^', '-', '@', '>']
    while '(' in query:
        for i in range(len(query)):
            if query[i] == '(':
                op = i
            if query[i] == ')':
                cl = i
                to_replace = query[op:cl+1]
                break
        to_change = ''
        for oper in operators:
            if oper in to_replace:
                to_repl_parts = to_replace.split(oper)
                to_change = oper

                break
        query = query.replace(to_replace, change_oper(to_change, to_repl_parts))

    return query

def subsets(S):
    sets = []
    len_S = len(S)
    for i in range(1 << len_S):
        subset = [S[bit] for bit in range(len_S) if i & (1 << bit)]
        sets.append(subset)
    return sets

query = to_bin(query)

query = query.replace('[', '(').replace(']', ')')
variables = []
my_ascii = [i for i in range(97, 123)] + [i for i in range(65, 91)]
for i in query:
    if ord(i) in my_ascii:
        variables.append(i)
variables = list(set(variables))
var_len = len(variables)
to_ones = subsets(variables)
vars_values = [0] * var_len
all_cases = []
all_queries = []
for subset in to_ones:
    vars_values = [0] * var_len
    for j in subset:
        vars_values[variables.index(j)] = 1
    all_cases.append(vars_values)

for i in all_cases:
    query2 = query
    for n, j in enumerate(i):
        query2 = query2.replace(variables[n], str(j))
    all_queries.append(query2)

print('Над полем GF(2): ', query)
print(variables)
results = [eval(i) % 2 for i in all_queries]
for i in range(len(all_queries)):
    print(str(all_cases[i]) + '_'*len(variables)*3 + str(results[i]))

tavtology = all(results)
if all(results):
    tavtology = 'є тавтологією.'
else:
    tavtology = 'не є тавтологією.'
print('\nРезультати наступні:', results, '\nОтже формула', tavtology)

a=input('\n\nНажміть будь-яку клавішу, щоб вийти')
