def stringSeparator(user_input):
    """
    Function to sort user string input.
    This function will only run if the user input contains words 
    that are inside the input constraints  
    """
    #input constraint
    my_input = "print happy against monkey need different effect sheep paper horse parallel journey kind account opinion lock knowledge look weather join market space married who nerve responsible payment again while rhythm prison opposite special why authority rest school operation river year shake than shame push when question road waiting Zoo respect that ring then very theory water tomorrow wheel umbrella the view walk twist unit voice waste together week weight yesterday tooth you young Zibra will yellow brain verse Xray cloud adjustment between where connection branch care needle about with addition cart button control desire Xman cloth balance"
    my_list = my_input.split(" ")

    ##spliting user input
    user_list = []
    temp = ""
    for i in user_input:
        if i == " ":
            user_list.append(temp)
            temp = ""
        else:
            temp += i 
    if temp:
        user_list.append(temp)

    def wordSorter(word):
        """
        fucntion to sort the input words
        """
        if not word:
            return []
        return (wordSorter([i for i in word[1:] if i < word[0]])
                + [word[0]] +
                wordSorter([i for i in word[1:] if i >= word[0]])
        )
    
    def combiner(word):
        """
        combine string elements
        """
        return [" ".join(word[0:])]

    #sort only if the words exist inside input constraints
    if all(elem in my_list for elem in user_list):
        sorted_list = wordSorter(user_list)
        final_list = combiner(sorted_list)
        #converting merged list into single string for output 
        print(final_list[0])
    else:
        #add indicator for unknown words
        #unknown_words = list(set(user_list) - set(my_list))
        #print("Unknown Word(s): ", unknown_words)
        print("Unknown Word(s): ")

stringSeparator("against happy effect ending")

