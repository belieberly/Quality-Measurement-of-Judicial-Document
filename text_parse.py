import re
print('kaishi')


with open('./data/path.txt','r',encoding = 'utf-8') as path_txt:
    for doc in path_txt.readlines:
        doc_path = doc.strip()
        with open(doc_path,'r',encoding = 'utf-8') as doc:
            doc_txt = doc.readlines()


inputf1 = open('./example.txt', 'r', encoding='utf-8')
inputf2 = open('./example.txt','r',encoding = 'utf-8')
text1 = inputf1.readlines()
text2 =inputf2.readlines()
print(text1)
print(text2)
text_dict1 = { }
test_txt = '中国农业银行民事一审判决书巴拉巴拉'




text_dict1['案件类型'] = '民事判决书'
text_dict1['案件名称'] =  text1[0].replace('')
if(re.search(r'一审',text1[0])):
    print('一审')
    text_dict1['审判流程'] = '一审'
    data_hits = re.split(r'\t',text1[1])
    print(data_hits)



def doc_category(str):
    if(re.match(r'.*民事裁定书$',str)):
        print("民事裁定书一类")
        return 0
    if(re.match(r'.*民事判决书$',str)):
        print('民事判决书一类')
        return 1






