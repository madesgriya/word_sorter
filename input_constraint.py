#creating list of constraint words
my_input = "print happy against monkey need different effect sheep paper horse parallel journey kind account opinion lock knowledge look weather join market space married who nerve responsible payment again while rhythm prison opposite special why authority rest school operation river year shake than shame push when question road waiting Zoo respect that ring then very theory water tomorrow wheel umbrella the view walk twist unit voice waste together week weight yesterday tooth you young Zibra will yellow brain verse Xray cloud adjustment between where connection branch care needle about with addition cart button control desire Xman cloth balance"
my_list = []
temp = ""
for i in my_input:
    if i == " ":
        my_list.append(temp)
        temp = ""
    else:
        temp += i 
if temp:
    my_list.append(temp)
#print(len(my_list))

