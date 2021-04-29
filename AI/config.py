root_path = './data/'

rumor_path = f'{root_path}Chinese_Rumor_Dataset/CED_Dataset/rumor-repost/'
non_rumor_path = f'{root_path}Chinese_Rumor_Dataset/CED_Dataset/non-rumor-repost/'
all_page_path = f'{root_path}Chinese_Rumor_Dataset/CED_Dataset/original-microblog/'

fuck_political_path = f'{root_path}敏感词库/反动词库.txt'
political_path = f'{root_path}敏感词库/政治类.txt'
H_path = f'{root_path}敏感词库/色情词库.txt'
advertising_path = f'{root_path}敏感词库/广告.txt'
fear_path = f'{root_path}敏感词库/暴恐词库.txt'
human_path = f'{root_path}敏感词库/民生词库.txt'
gun_fear_path = f'{root_path}敏感词库/涉枪涉爆违法信息关键词.txt'
fuck_url = f'{root_path}敏感词库/网址.txt'
stop_words_path = f'{root_path}停用词/'
chinese_stop_words = f'{stop_words_path}中文停用词库.txt'
path_list = {
    0: fuck_political_path,
    1: political_path,
    2: H_path,
    3: advertising_path,
    4: fear_path,
    5: human_path,
    6: gun_fear_path
}
result_ = {
    0: "政治反动信息",
    1: "政治敏感信息",
    2: "淫秽色情信息",
    3: "广告信息",
    4: "暴恐信息",
    5: "民生纠纷信息",
    6: "枪械暴乱信息",
}
result = {
    0: "谣言",
    1: "非谣言"
}
chinese_rumor = f'{root_path}中文谣言数据/rumors_v170613.json'
chinese_news_non_rumor = f'{root_path}news_tensite_xml.xml'
rumor_data_list = []
rumor_types_list = []
other_data_list = []
other_type_list = []
stop_words = []
