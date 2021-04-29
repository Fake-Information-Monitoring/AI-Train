import jieba

from config import *


def wash_sentence(sentence) -> str:
    sentence = jieba.cut(sentence)
    article = ' '.join([word for word in sentence if word not in stop_words])  # 对语料进行分词
    return article


# def read_sensitive_words(path, type: int):
#     with open(path, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#         for i in lines:
#             article: str = i.replace('\n', '')
#             article: str = wash_sentence(sentence=article)
#             other_data_list.append(article)
#             other_type_list.append(type)
#             f.close()
#
#
# def __read_rumor(path: str, type: int):
#     rumor_dir = os.listdir(path)
#     for rumor_folder in rumor_dir:
#         with open(all_page_path + rumor_folder, "r", encoding="utf-8") as f:
#             article: str = f.read()
#             article: str = json.loads(article)['text']
#             article: str = wash_sentence(sentence=article)  # 对语料进行分词
#             rumor_data_list.append(article)
#             rumor_types_list.append(type)
#             f.close()
#
#
# def read_rumor():
#     # 读谣言标签
#     with open(chinese_rumor, 'r', encoding="utf-8") as f:
#         articles: str = f.readlines()
#         for article in articles:
#             article: str = json.loads(article)['rumorText']
#             article: str = wash_sentence(sentence=article)
#             rumor_data_list.append(article)
#             rumor_types_list.append(0)
#             f.close()
#     __read_rumor(rumor_path, 0)
#
#
# def read_non_rumors():
#     # 解析正常新闻文本
#     with open(chinese_news_non_rumor, 'r', encoding='utf-8') as f:
#         data = f.read()
#         data = re.sub('[\u3000]', '', data)
#         data = re.sub('[\ue40c]', '', data)
#         a = r'<content>(.*?)</content>'
#         slotLits = re.findall(a, data)
#         f.close()
#         samplist = sample(slotLits, len(rumor_data_list) + 10000)
#         for i in samplist:
#             rumor_data_list.append(wash_sentence(sentence=i))
#             rumor_types_list.append(1)
#     __read_rumor(non_rumor_path, 1)
#
#
# def read_rumors():
#     global stop_words
#     # 读停用词
#     stop_words = [line.strip()
#                   for line in open(chinese_stop_words, 'r', encoding='utf-8').readlines()]
#     rumor_threading = threading.Thread(target=read_rumor)
#     rumor_threading.start()
#     rumor_threading.join()
#     non_rumor_threading = threading.Thread(target=read_non_rumors)
#     non_rumor_threading.start()
#     print("read_waitting......")
#     non_rumor_threading.join()
#     print("data read OK")
#     return rumor_data_list, rumor_types_list
#
#
# def transform_tfidf(train_data, test_data):
#     tfidf = TfidfVectorizer()
#     train_vec = tfidf.fit_transform(train_data)  # 把分词文本转为tf-idf矩阵
#     save(tfidf, "./tfidf.pkl")
#     if test_data is not None:
#         return train_vec
#     test_vec = tfidf.transform(test_data) if test_data is not None else None  # 测试tf-idf
#     return train_vec, test_vec
#
#
# def split_numpy(data, types, size):
#     return train_test_split(
#         data, types, test_size=size, shuffle=True
#     )
#
#
# def read_other_data():
#     # 读取广告标签
#     read_sensitive_words(advertising_path, 2)
#     # 读取反动言论标签
#     read_sensitive_words(fuck_political_path, 3)
#     # 读取暴恐类词
#     read_sensitive_words(fear_path, 4)
#     # 读取民生类词
#     read_sensitive_words(human_path, 5)
#     # 读取涉枪涉爆违法关键词
#     read_sensitive_words(gun_fear_path, 6)
#     # 读取色情关键词
#     read_sensitive_words(H_path, 7)
#     # 读取政治类词汇标签
#     read_sensitive_words(political_path, 8)
#     return other_data_list, other_type_list
