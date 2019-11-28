import re

from standard_norm import JudicialDoc

print('kaishi')

# 批量读取裁判文书
# with open('./data/path.txt', 'r', encoding='utf-8') as path_txt:
#     for doc in path_txt.readlines():
#         doc_path = doc.strip()
#         with open('./data/' + doc_path, 'r', encoding='utf-8') as doc:
#             doc_txt = doc.readlines()
#             print(doc_txt)

# inputf1 = open('./example.txt', 'r', encoding='utf-8')
# inputf2 = open('./example.txt', 'r', encoding='utf-8')
# text1 = inputf1.readlines()
# text2 = inputf2.readlines()
# print(text1)
# print(text2)
# text_dict1 = {}
# test_txt = '中国农业银行民事一审判决书巴拉巴拉'
#
#
#
# text_dict1['案件类型'] = '民事判决书'
# text_dict1['案件名称'] = text1[0].replace('')
# if (re.search(r'一审', text1[0])):
#     print('一审')
#     text_dict1['审判流程'] = '一审'
#     data_hits = re.split(r'\t', text1[1])
#     print(data_hits)
#
#
# def doc_category(str):
#     if (re.match(r'.*民事裁定书$', str)):
#         print("民事裁定书一类")
#         return 0
#     if (re.match(r'.*民事判决书$', str)):
#         print('民事判决书一类')
#         return 1

inputf1 = open('./data/example.txt', 'r', encoding='utf-8')
inputf2 = open('./data/example.txt', 'r', encoding='utf-8')
text1 = inputf1.readlines()
text2 = inputf2.readlines()


def split_txt(doc_txt: list):
    flag_list = [[] for i in range(len(doc_txt))]
    for i in range(len(doc_txt)):
        doc_txt[i] = doc_txt[i].strip()
        if (re.match(r'.*民事判决书$', doc_txt[i])):
            flag_list[i].append('pagename')
        if (re.match(r'^发布日期：.*浏览：[0-9]*次$', doc_txt[i])):
            flag_list[i].append('information')
        if (re.match(r'.*法院$', doc_txt[i]) and len(doc_txt[i] )< 30):
            flag_list[i].append('title.court_name')
        if (re.match(r'民[\s]?事[\s]?判[\s]?决[\s]?书', doc_txt[i])):
            flag_list[i].append('title.doc_type')
        if (re.match(r'（[0-9]{4}）[\w\u4e00-\u9fcc]?[0-9]+[\w\u4e00-\u9fcc]{2}[0-9]+号', doc_txt[i])):
            flag_list[i].append('title.doc_num')
        if (re.match(r'^(原告|被告|负责人|委托诉讼代理人|负责人)', doc_txt[i])):
            flag_list[i].append('head.basic_situation')
        if (re.match(r'原告[\w\u4e00-\u9fcc]+与被告[\w\u4e00-\u9fcc]+.*本院.*本案现已审理终结。$', doc_txt[i])):
            flag_list[i].append('head.summary')
        if (re.match(r'^原告[\w\u4e00-\u9fcc]*(诉称|称|请求)*判.*请求.*', doc_txt[i])):
            flag_list[i].append('facts.yuangao')
        if (re.match(r'^被告[\w\u4e00-\u9fcc]*(未到庭|未[\w\u4e00-\u9fcc]*提交书面答辩|辩称)', doc_txt[i])):
            flag_list[i].append('facts.beigao')
        if (re.search(r'经[\w\u4e00-\u9fcc]*审理查明', doc_txt[i])):
            flag_list[i].append('facts.fayuan')
        if (re.match(r'本院认为', doc_txt[i])):
            flag_list[i].append('analysis')
        if (re.search(r'依照.*[第.*条]+', doc_txt[i])):
            flag_list[i].append('law_dependence')
        if (re.match(r'^上述具有履行内容的条款，均于本判决生效之日起[\w\u4e00-\u9fcc]+内履行', doc_txt[i])):
            flag_list[i].append('verdict')
        if (re.match(r'^如果未按本判决指定的期间履行[\w\u4e00-\u9fcc]+义务，应当依照', doc_txt[i])):
            flag_list[i].append('verdict')
        if (re.search(r'案件受理费[0-9]+元.*[.*费[0-9]元]*', doc_txt[i])):
            flag_list[i].append('tail.charge')
        if (re.match(r'^如不服本判决，可在判决书送达之日起十五日内，向本院递交上诉状，并按[\w\u4e00-\u9fcc]+提出副本，上诉于', doc_txt[i])):
            flag_list[i].append('tail.notification')

    print(zip(doc_txt, flag_list))


split_txt(text1)
