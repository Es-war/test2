import ChineseBreak
import pypinyin
import copy

PINYIN = [
    'a', 'o', 'e', 'ba', 'bo', 'bi', 'bu', 'pa', 'po', 'pi', 'pu',
    'ma', 'mo', 'me', 'mi', 'mu', 'fa', 'fo', 'fu', 'da', 'de',
    'di', 'du', 'ta', 'te', 'ti', 'tu', 'na', 'ne', 'ni', 'nu',
    'nv', 'la', 'lo', 'le', 'li', 'lu', 'lv', 'ga', 'ge', 'gu',
    'ka', 'ke', 'ku', 'ha', 'he', 'hu', 'ji', 'ju', 'qi', 'qu',
    'xi', 'xu', 'zha', 'zhe', 'zhi', 'zhu', 'cha', 'che', 'chi',
    'chu', 'sha', 'she', 'shi', 'shu', 'ra', 're', 'ri', 'ru',
    'za', 'ze', 'zi', 'zu', 'ca', 'ce', 'ci', 'cu', 'sa', 'se',
    'si', 'su', 'ya', 'yo', 'ye', 'yi', 'yu', 'wa', 'wo', 'wu',
    'ai', 'ei', 'ao', 'ou', 'er', 'bai', 'bei', 'bao', 'bie',
    'pai', 'pei', 'pao', 'pou', 'pie', 'mai', 'mei', 'mao', 'mou',
    'miu', 'mie', 'fei', 'fou', 'dai', 'dei', 'dui', 'dao', 'dou',
    'diu', 'die', 'tai', 'tei', 'tui', 'tao', 'tou', 'tie', 'nai',
    'nei', 'nao', 'nou', 'niu', 'nie', 'lai', 'lei', 'lao', 'lou',
    'liu', 'lie', 'gai', 'gei', 'gui', 'gao', 'gou', 'kai', 'kei',
    'kui', 'kao', 'kou', 'hai', 'hei', 'hui', 'hao', 'hou', 'jiu',
    'jie', 'jue', 'qiu', 'qie', 'que', 'xiu', 'xie', 'xue', 'zhai',
    'zhei', 'zhui', 'zhao', 'zhou', 'chai', 'chui', 'chao', 'chou',
    'shai', 'shei', 'shui', 'shao', 'shou', 'rui', 'rao', 'rou',
    'zai', 'zei', 'zui', 'zao', 'zou', 'cai', 'cei', 'cui', 'cao',
    'cou', 'sai', 'sui', 'sao', 'sou', 'yao', 'you', 'yue', 'wai',
    'wei', 'an', 'en', 'ang', 'eng', 'ban', 'ben', 'bin', 'bang',
    'beng', 'bing', 'pan', 'pen', 'pin', 'pang', 'peng', 'ping',
    'man', 'men', 'min', 'mang', 'meng', 'ming', 'fan', 'fen',
    'fang', 'feng', 'dan', 'den', 'dun', 'dang', 'deng', 'ding',
    'dong', 'tan', 'tun', 'tang', 'teng', 'ting', 'tong', 'nan',
    'nen', 'nin', 'nun', 'nang', 'neng', 'ning', 'nong', 'lan',
    'lin', 'lun', 'lang', 'leng', 'ling', 'long', 'gan', 'gen',
    'gun', 'gang', 'geng', 'gong', 'kan', 'ken', 'kun', 'kang',
    'keng', 'kong', 'han', 'hen', 'hun', 'hang', 'heng', 'hong',
    'jin', 'jun', 'jing', 'qin', 'qun', 'qing', 'xin', 'xun',
    'xing', 'zhan', 'zhen', 'zhun', 'zhang', 'zheng', 'zhong',
    'chan', 'chen', 'chun', 'chang', 'cheng', 'chong', 'shan',
    'shen', 'shun', 'shang', 'sheng', 'ran', 'ren', 'run', 'rang',
    'reng', 'rong', 'zan', 'zen', 'zun', 'zang', 'zeng', 'zong',
    'can', 'cen', 'cun', 'cang', 'ceng', 'cong', 'san', 'sen',
    'sun', 'sang', 'seng', 'song', 'yan', 'yin', 'yun', 'yang',
    'ying', 'yong', 'wan', 'wen', 'wang', 'weng', 'biao', 'bian',
    'piao', 'pian', 'miao', 'mian', 'dia', 'diao', 'dian', 'duo', 'duan',
    'tiao', 'tian', 'tuo', 'tuan', 'niao', 'nian', 'niang', 'nuo',
    'nuan', 'lia', 'liao', 'lian', 'liang', 'luo', 'luan', 'gua',
    'guo', 'guai', 'guan', 'guang', 'kua', 'kuo', 'kuai', 'kuan',
    'kuang', 'hua', 'huo', 'huai', 'huan', 'huang', 'jia', 'jiao',
    'jian', 'jiang', 'jiong', 'juan', 'qia', 'qiao', 'qian',
    'qiang', 'qiong', 'quan', 'xia', 'xiao', 'xian', 'xiang',
    'xiong', 'xuan', 'zhua', 'zhuo', 'zhuai', 'zhuan', 'zhuang',
    'chua', 'chuo', 'chuai', 'chuan', 'chuang', 'shua', 'shuo',
    'shuai', 'shuan', 'shuang', 'rua', 'ruo', 'ruan', 'zuo',
    'zuan', 'cuo', 'cuan', 'suo', 'suan', 'yuan'
]
ALPHABET = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
    'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z'
]
map_cnt = 0
alp_py_map = {}  # ????????????????????????
divsion_map = {}   # ?????????????????????

file_org = "./requirements.txt"
file_org_add = "./org_add.txt"
file_ans = "./ans.txt"


class Word:
    def __init__(self, word):
        self.original_word = word

    def produce_sensitive_word(self):
        global map_cnt
        word = list(self.original_word)

        for index in range(len(word)):
            each = word[index]
            # ????????????
            if (u'\u4e00' <= each <= u'\u9fa5') or (u'\u3400' <= each <= u'\u4db5'):
                # print("??????????????????")
                li = []
                py = pypinyin.lazy_pinyin(each)
                py = py[0]
                # ??????
                li.append(py)
                # ????????????
                li.append(list(py))
                # ?????????
                li.append(py[0])

                # ????????????????????????
                if ChineseBreak.is_breakable(each):
                    sub_li = []
                    parts = ChineseBreak.get_part(each)
                    for part in parts:
                        if part not in divsion_map:
                            map_cnt += 1
                            divsion_map[part] = map_cnt
                        sub_li.append(part)
                    li.append(sub_li)
                word[index] = li

        sensitive_word = []
        for each in word:
            # ??????
            if isinstance(each, list):
                if len(sensitive_word) == 0:
                    for i in each:
                        if isinstance(i, list):
                            sensitive_word.append(i)
                        else:
                            sensitive_word.append([i])
                else:
                    new_sensitive_word = []
                    pre = sensitive_word
                    for one in each:
                        new = copy.deepcopy(pre)
                        for exited_one in new:
                            if isinstance(one, list):
                                for i in one:
                                    exited_one.append(i)
                            else:
                                exited_one.append(one)
                        new_sensitive_word += new
                    sensitive_word = new_sensitive_word
            # ????????????
            else:
                if len(sensitive_word) == 0:
                    sensitive_word.append([each])
                else:
                    sensitive_word[0].append(each)
        return sensitive_word


class Check:
    def __init__(self):
        # ????????????????????????????????????
        self.word_cnt = 0
        # ?????????????????????
        self.original_word = []
        # ??????????????????????????????
        self.sensitive_word = []

    def read_words(self):
        try:
            with open(file_org, 'r+', encoding='utf-8') as org:
                words = org.readlines()
                for word in words:
                    word = word.replace('\r', '').replace('\n', '')
                    # ????????????????????????
                    self.original_word.append(word)
                    word = Word(word)
                    # ????????????????????????????????????
                    deformations = word.produce_sensitive_word()
                    # ????????????????????????????????????????????????????????????????????????????????????
                    for deformation in deformations:
                        word_list = []
                        for each in deformation:
                            if each in alp_py_map:
                                word_list.append(alp_py_map[each])
                            elif each in divsion_map:
                                word_list.append(divsion_map[each])
                        self.sensitive_word.append([word_list, self.word_cnt])
                    self.word_cnt += 1
                # print(self.sensitive_word)
        except OSError as reason:
            print('????????????????????????\n?????????????????????' + str(reason))


def init_map():
    global map_cnt
    for letter in ALPHABET:
        map_cnt += 1
        alp_py_map[letter] = map_cnt
    for py in PINYIN:
        map_cnt += 1
        alp_py_map[py] = map_cnt


def main():
    # try:
    #     with open('./requirements.txt', 'r+', encoding='utf-8') as words:
    #         lines = words.readlines()
    #         for line in lines:
    #             line = line.replace('\r', '').replace('\n', '')
    #             for each in line:
    #                 ChineseBreak.test(each)
    # except OSError as reason:
    #     print('???????????????\n?????????????????????' + str(reason))
    init_map()
    checker = Check()
    checker.read_words()


if __name__ == '__main__':
    main()
