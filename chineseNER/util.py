import re
import os 
import pickle
import codecs

def zero_digits(s):
    return re.sub('\d', '0', s)

def load_sentences(path,zeros):
    sentences = []
    sentence = []
    num = 0
    for line in codecs.open(path, 'r', 'utf8'):
        num+=1
        line = zero_digits(line.rstrip()) if zeros else line.rstrip()
        # print(list(line))
        if not line:
            if len(sentence) > 0:
                if 'DOCSTART' not in sentence[0][0]:
                    sentences.append(sentence)
                sentence = []
        else:
            if line[0] == " ":
                line = "$" + line[1:]
                word = line.split()
                # word[0] = " "
            else:
                word= line.split()
            assert len(word) >= 2, print([word[0]])
            sentence.append(word)
    if len(sentence) > 0:
        if 'DOCSTART' not in sentence[0][0]:
            sentences.append(sentence)
    return sentences

def split_sent_label(data):
    sents = []
    labels = []
    for i in data:
        sent = []
        label = []
        for j in i:
            sent_ = j[0]
            label_ = j[1]
            sent.append(sent_)
            label.append(label_)
        sents.append(sent)
        labels.append(sent)
    return sents, labels

def build_vocab(sents, vocab_path):
    vocab = []
    for i in sents:
        vocab+= i
    vocab = set(vocab)
    vocab_dict = {}
    for i,j in enumerate(vocab):
        vocab_dict[j] = i
    with open(vocab_path, 'wb') as f:
        pickle.dump(vocab_dict,f)
    return vocab_dict


if __name__ == '__main__':
    path = os.path.join(os.getcwd(),'data','example.train')
    data = load_sentences(path,0)
    sents, labels = split_sent_label(data)
    vocab_path = os.path.join(os.getcwd(),'configs','vocab.pickle')
    vocab_dict = build_vocab(sents, vocab_path)
