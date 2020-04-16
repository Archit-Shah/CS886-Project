# Read in data from the files
f = open("../multi-news-data/train.txt.src.tokenized.fixed.cleaned.final.truncated.txt", "r")
content = f.read()
f.close()

content = content.replace("\n", "\n///////////////////////////////////////////////////////////////////////////\n")
content = content.replace("story_separator_special_tag", "\n")

# Write the pre-processed text data
f = open("../data/train.clean.txt", "w")
f.write(content)
f.close()
