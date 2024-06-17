import re

print(re.search(r"[A-Z]la", "ala Ola Ela"))

print(re.match(r"[A-Z]la", "Ala Ola Ela"))
print(re.search(r"^[A-Z]la", "Ala Ola Ela"))

print(re.fullmatch(r"[A-Z]la", "Ala"))
print(re.search(r"^[A-Z]la$", "Ala"))

result = re.findall(r"[A-Z]la", "Ola ala Ela bla")
print(result)

result_iter = re.finditer(r"[A-Z]la", "Ola ala Ela bla")
for elem in result_iter:
    print(elem)

print("apple,pear,grapes,carrot.cabbage,veggies.fruit,yard".split(","))
print(re.split(r",", "apple,pear,grapes,carrot.cabbage,veggies.fruit,yard"))
print(re.split(r",|\.|\s", "apple,pear,grapes,carrot.cabbage,veggies fruit,yard"))

my_text = """
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Etiam posuere lacus quis dolor. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi leo mi, nonummy eget tristique non, rhoncus non leo! Maecenas aliquet accumsan leo. Aenean placerat. Mauris dictum facilisis augue. Mauris dolor felis, sagittis at, luctus sed, aliquam non, tellus. Nam sed tellus id magna elementum tincidunt. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Etiam posuere lacus quis dolor. Nulla est. Integer tempor. Donec quis nibh at felis congue commodo. Suspendisse nisl. Etiam neque. Sed vel lectus. Donec odio tempus molestie, porttitor ut, iaculis quis, sem. Sed ac dolor sit amet purus malesuada congue. Suspendisse sagittis ultrices augue.
Maecenas sollicitudin. Fusce suscipit libero eget elit. Curabitur sagittis hendrerit ante? Mauris dolor felis, sagittis at, luctus sed, aliquam non, tellus. Etiam bibendum elit eget erat. Nulla turpis magna, cursus sit amet, suscipit a, interdum id, felis. Maecenas ipsum velit, consectetuer eu lobortis ut, dictum at dui. Mauris dictum facilisis augue. Vivamus ac leo pretium faucibus. Etiam dui sem, fermentum vitae, sagittis id, malesuada in, quam. Maecenas ipsum velit, consectetuer eu lobortis ut, dictum at dui. Maecenas aliquet accumsan leo. Nulla non lectus sed nisl molestie malesuada. Duis condimentum augue id magna semper rutrum. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Donec ipsum massa, ullamcorper in, auctor et, scelerisque sed, est. Duis pulvinar. Fusce tellus odio, dapibus id fermentum quis, suscipit id erat. Fusce dui leo, imperdiet in, aliquam sit amet, feugiat eu, orci. Maecenas aliquet accumsan leo.
Nullam lectus justo, vulputate eget mollis sed, tempor sed magna? Duis ante orci, molestie vitae vehicula venenatis, tincidunt ac pede. Aenean vel massa quis mauris vehicula lacinia. Fusce suscipit libero eget elit. Nulla quis diam. Nullam feugiat, turpis at pulvinar vulputate, erat libero tristique tellus, nec bibendum odio risus sit amet ante. Nullam at arcu a est sollicitudin euismod. Nullam dapibus fermentum ipsum. Nulla non lectus sed nisl molestie malesuada. Fusce tellus odio, dapibus id fermentum quis, suscipit id erat. Etiam bibendum elit eget erat. Cras elementum. Etiam dui sem, fermentum vitae, sagittis id, malesuada in, quam. Donec quis nibh at felis congue commodo. Nullam dapibus fermentum ipsum. Duis ante orci, molestie vitae vehicula venenatis, tincidunt ac pede. Fusce suscipit libero eget elit. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.
Etiam posuere lacus quis dolor. Integer vulputate sem a nibh rutrum consequat! Nunc tincidunt ante vitae massa. Pellentesque sapien. Aliquam erat volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Integer pellentesque quam vel velit. Mauris metus. Maecenas fermentum, sem in pharetra pellentesque, velit turpis volutpat ante, in pharetra metus odio a lectus. Sed ac dolor sit amet purus malesuada congue. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas fermentum, sem in pharetra pellentesque, velit turpis volutpat ante, in pharetra metus odio a lectus. Fusce tellus odio, dapibus id fermentum quis, suscipit id erat. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Fusce tellus. Integer malesuada. Nullam justo enim, consectetuer nec, ullamcorper ac, vestibulum in, elit. Pellentesque sapien.
Nunc tincidunt ante vitae massa. Aenean vel massa quis mauris vehicula lacinia. Nulla turpis magna, cursus sit amet, suscipit a, interdum id, felis. Etiam bibendum elit eget erat. Etiam sapien elit, consequat eget, tristique non, venenatis quis, ante. Duis condimentum augue id magna semper rutrum. Etiam bibendum elit eget erat. In dapibus augue non sapien. Donec quis nibh at felis congue commodo. Integer rutrum, orci vestibulum ullamcorper ultricies, lacus quam ultricies odio, vitae placerat pede sem sit amet enim. Mauris tincidunt sem sed arcu. Maecenas libero. Phasellus rhoncus.
"""

sentences = re.split(r"\.|\?|!", my_text)
for sentence in sentences:
    print(sentence)

print(re.sub(r"[a-z]{8}", "dog", "Alice has elephant"))
print(re.sub(r"[A-Z][a-z]+", "****", "Alice has elephant. Peter has dog."))
print(re.subn(r"[A-Z][a-z]+", "****", "Alice has elephant. Peter has dog. I have cat."))
print(re.subn(r"[A-Z]", "****", "Alice has elephant. Peter has dog. I have cat."))

print("-"*80)
print("Grouping")

text = "Thomas W. (33), last seen in Krakow"
pattern = r"([A-Z][a-z]+ [A-Z]\.) \((\d+)\)"
match = re.search(pattern, text)
print(match)
print(match.groups)
print(match.group(0))
print(match.group(1))
print(match.group(2))

text = "Thomas (33) and Eva (24) agreed to go shopping together tomorrow"
pattern = r"([A-Z][a-z]+) \((\d+)\)"
match = re.findall(pattern, text)
print(match)
for elem in match[1]:
    print(elem)
