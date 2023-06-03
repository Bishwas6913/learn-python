#   スラッシュによるエスケープ
#   \ を使えばいろんな意味になる

#   \n　による改行

slash_n = "A pen,\nA man,\nA cat,\nA house"

# print(slash_n)


#   tabキーのように　文字を分ける
slash_t1 = "\tabcd "
slash_t2 = "a\tbc"
slash_t3 ="ab\tcd"
slash_t4 ="abc\td"
slash_t5 ="abcd\t"

# print(slash_t1)
# print(slash_t2)
# print(slash_t3)
# print(slash_t4)
# print(slash_t5)

#   add slash in the string
slash_slash = "just add the \\ in the string"

# print(slash_slash)


#   add quotations in the string

add_quotation = "ths is how you add quatons \" in string"

# print(add_quotation)

raw_string = r"none of the escapes \n are usable \t \a \\ in a raw string"

# print(raw_string)


#   repeat string

na = "Na " * 4 + "\n"

sup = "Sup " * 3 +"\n"

boy = "BOY!"

print(na + sup + boy)



