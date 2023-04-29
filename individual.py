import tagger

tag_name = input("Введите название тега: ")
tagged_string = tagger.tagger(tag_name)(input("Введите строку для тегирования: "))
print(tagged_string)