def validate_pesel(num):
    pes_lst = [int(d) for d in num]
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    ilo = []
    for i in range(len(wagi)):
        ilo.append(wagi[i] * pes_lst[i])
    sum_ilo = sum(ilo)
    buff = sum_ilo % 10
    if buff != 10:
        contr_num = 10 - buff
        if contr_num ==  int(num[10]):
            return True
        return False
    contr_num = 0
    if contr_num == int(num[10]):
        return True
    return False


data = ["04312461812", "84012986920", "82072278430", "96071056215", "69032893127",
"84020411318","55102623859", "57061854141", "57082223294", "86051276344", "91081302039",
"56021561125", "92011238228", "52110316782", "95080891558", "77032312665", "77121939465"
,"58012361253","92102813947","55061485729","69081478346","99100244311"]

for i in data:
    print(i, validate_pesel(i))