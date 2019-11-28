import re
from datetime import date


# 网页标题
class PageName:
    def __init__(self, page_name_str):
        # 标题内容
        self.page_name = page_name_str


# 基本信息
class Information(object):
    def __init__(self, publish_date: date, hits=0):
        # 发布日期
        self.publish_date = publish_date
        # 点击量
        self.hits = hits


# 裁判文书正文标题
class Title:
    def __init__(self, title_str):
        self.title = title_str


# 首部
class Head:
    def __init__(self, basic_situation: str, summary: str):
        # 当事人基本情况
        self.basic_situation = {'当事人基本情况': basic_situation}
        self.summary = {'案件由来和审理经过': summary}


# 事实段落
class Facts:
    def __init__(self, yuangao_str: str = "", beigao_str: str = "", fayuan_str: str = ""):
        self.yuangao = {'原告': yuangao_str}
        self.beigao = {'被告': beigao_str}
        self.fayuan = {'法院': fayuan_str}


class Anaysis:
    def __init__(self, analysis_str: str = ""):
        self.analysis = {'分析过程（理由）': analysis_str}


class LawDependence:
    def __init__(self, law_dependence_str: str = ""):
        self.law_dependence = {'裁判依据': law_dependence_str}


class Verdict:
    def __init__(self, verdict_str: str = ''):
        self.verdict = {'判决结果': verdict_str}


class Tail:
    def __init__(self, charge_str: str = '', notification_str: str = ''):
        self.charge = {'诉讼费用负担': charge_str}
        self.notification = {'告知事项': notification_str}


class Inscription:
    def __init__(self, inscription_str: str = ""):
        self.inscription = {'落款': inscription_str}


class Appendix:
    def __init__(self, appendix_str: str = ""):
        self.appendix = {u'附录': appendix_str}


# 裁判文书
class JudicialDoc:
    def __init__(self, doc_txt: list):
        pass
    def split_txt(doc_txt: list):
        flag_list = [[] for i in range(len(doc_txt))]
        for i in range(len(doc_txt)):
            if (re.match(r'.*民事判决书$', doc_txt[i])):
                flag_list[i].append('pagename')
            if (re.match(r'^发布日期：.*浏览：[0-9]*次$', doc_txt[i])):
                flag_list[i].append('information')
            if (re.match(r'.*法院$', doc_txt[i]) and len(doc_txt[i] < 30)):
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
            if (re.match(r'^如不服本判决，可在判决书送达之日起十五日内，向本院递交上诉状，并按对方当事人或者代表人的人数提出副本，上诉于', doc_txt[i])):
                flag_list[i].append('tail.notification')

        print(zip(doc_txt, flag_list))
