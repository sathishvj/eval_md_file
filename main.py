import sys
import os
from os import path

# replace folder path with where you have the gcp-enablement-content git folder
gcp_enablement_content_folder="/Users/vj/coding/projects/gcp-enablement-content"

# first argument is directory
if len(sys.argv) < 2:
    print('Arg1 should be to a lab folder.')
    os._exit(1)
    if not os.path.isdir(sys.argv[1]):
        print('Arg1 does not point to a folder.')
        os._exit(1)

folder=sys.argv[1]
enmd_path=folder+path.sep+'en.md'
if not path.isfile(enmd_path):
    print('Folder does not contain an en.md file.')
    os._exit(1)

def to_titlecase(s):
    exceptions=['a', 'an', 'of', 'the', 'is', 'be']
    acronyms=['IAM']
    word_list = s.split()
    final = [word_list[0].capitalize()]
    for word in word_list[1:]:
        if word in acronyms:
            final.append(word.upper())
        elif word in exceptions:
            final.append(word)
        else:
            final.append(word.capitalize())
    return " ".join(final)

def check_words(line, n):
# check misspelt/misused words
    do_not_use_words=[
            "gcp" # use Google Cloud instead
            ]
    misspelt_words=[
            "BigQuery",
            "Bigtable"
            ]
    line = line.strip()
    if len(line)==0:
        return
    words=line.split()
    for word in words:
        if word.lower() in do_not_use_words:
            print("Error! Line", n, ": Do not use word: ", word)
        if word.lower() in (mw.lower() for mw in misspelt_words):
            if not word in misspelt_words:
                print("Error! Line", n, ": Word not correctly written: ", word)


# check format of each line
def check_line_format(line, n):
    line = line.strip()
    if len(line)==0:
        return
    elif line.startswith("![[/fragments"):
        # check if fragment exists
        fragment=line[14:-2]
        fragments_path=gcp_enablement_content_folder+path.sep+"fragments"+path.sep+fragment
        if not os.path.isdir(fragments_path):
            print("Error! Line", n, ": No fragment: ", line, fragments_path)
    #elif line.startswith("# "):
        # h1
    elif line.startswith("## "):
        # h2
        if line.startswith("## Task"):
            #print("# task title")
            # todo: check if using dot after number.
            # todo: check if number is proper.
            # check if title case. Todo: don't hardcode 10.
            t=line[10:].strip()
            if not t == to_titlecase(t):
                print("Error! Line", n, ": Not title case: ", line, " | Should be: ", to_titlecase(t))


def check_imgs(line, n):
    line = line.strip()
    if len(line)==0:
        return
    words=line.split()
    for word in words:
        if word.startswith('src="img/') or word.startswith("src='img/"):
            img_name=word[9:-1]
            img_path=folder+path.sep+"img"+path.sep+img_name
            if not os.path.isfile(img_path):
                print("Error! Line", n, ": Img does not exist: img/"+img_name)

# read all the lines from en.md
file=open(enmd_path)
lines=file.readlines()

n=0
for line in lines:
    n=n+1
    check_words(line, n)
    check_line_format(line, n)
    check_imgs(line, n)

