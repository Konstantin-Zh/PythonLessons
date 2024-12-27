
def single_root_words (root_word, *other_words):
    same_words = list()
    for i in other_words:
        if str(i).upper().find(str(root_word).upper()) >= 0 or str(root_word).upper().find(str(i).upper()) >= 0:
            same_words.append(str(i))
    return same_words

print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))