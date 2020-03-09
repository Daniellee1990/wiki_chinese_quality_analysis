import pandas as pd
import re
from pypinyin import lazy_pinyin, Style

def clean_chinese_characters(texts):
    new_texts = []
    """
    处理字符级汉字文本，只保留汉语字符
    :param texts: 
    :return: 
    """
    for txt in texts:
        txt = re.sub('[^\u4e00-\u9fa5^(。，！？‘“)^]', '', txt)
        new_texts.append(txt)
    return new_texts


def clean_chinese_words(texts):
    new_texts = []
    """
    处理分词后汉字文本，只保留汉语词和空格
    :param texts: 
    :return: 
    """
    for txt in texts:
        txt = re.sub('[^\u4e00-\u9fa5^(。，！？‘“)^\s]', '', txt)
        new_texts.append(' '.join(txt.split()))
    return new_texts


def parse_pinyin(texts):
    style = Style.TONE3
    py = []
    py_tone = []
    for txt in texts:
        txt = re.sub('[^\u4e00-\u9fa5]', '', txt)
        _py_tone = ' '.join(lazy_pinyin(txt, style=style))
        _py = ' '.join(lazy_pinyin(txt))
        py_tone.append(_py_tone)
        py.append(_py)
    return py, py_tone


if __name__ == '__main__':
    # df = pd.read_csv(open('../data/corpus.csv', 'r', encoding='UTF-8'))
    # texts = list(df['text'])
    # labels = list(df['label'])
    # cleaned_texts = clean_chinese_characters(texts)
    # df = pd.DataFrame({'text': cleaned_texts,  'label': labels})
    # df.to_csv('./corpus_character.csv')

    # df = pd.read_csv(open('../data/corpus_words.csv', 'r', encoding='UTF-8'))
    # texts = list(df['content'])
    # texts = clean_chinese_words(texts)
    # df = pd.DataFrame({'content': texts})
    # df.to_csv('./corpus_words.csv')

    df = pd.read_csv(open('../data/corpus.csv', 'r', encoding='UTF-8'))
    texts = list(df['text'])
    py, py_tone = parse_pinyin(texts)
    df = pd.DataFrame({'pinyin1': py, 'pinyin2': py_tone})
    df.to_csv('./corpus_pinyin.csv')
