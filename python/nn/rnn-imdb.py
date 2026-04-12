import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.layers import Dense, Embedding, SimpleRNN
from tensorflow.keras.models import Sequential

vocabulary = 10000  # 只用词典使用频率前10000的单词
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocabulary)

# 构建字典 key为id value为单词 +3是因为0、1、2是保留的
id_to_word = {id_ + 3: word for word, id_ in imdb.get_word_index().items()}

# 0表示填充令牌"<pad>" 1表示序列开始"<sos>" 2表示未知单词"<unk>"
for id_, token in enumerate(("<pad>", "<sos>", "<unk>")):
    id_to_word[id_] = token

# 显示前5条评论的前10个单词的id表示和原文
for i in range(5):
    print(X_train[i][:10])
    print(" ".join([id_to_word[id_] for id_ in X_train[i][:10]]))
# [1, 14, 22, 16, 43, 530, 973, 1622, 1385, 65]
# <sos> this film was just brilliant casting location scenery story
# [1, 194, 1153, 194, 8255, 78, 228, 5, 6, 1463]
# <sos> big hair big boobs bad music and a giant
# [1, 14, 47, 8, 30, 31, 7, 4, 249, 108]
# <sos> this has to be one of the worst films
# [1, 4, 2, 2, 33, 2804, 4, 2040, 432, 111]
# <sos> the <unk> <unk> at storytelling the traditional sort many
# [1, 249, 1323, 7, 61, 113, 10, 10, 13, 1637]
# <sos> worst mistake of my life br br i picked


def my_pad_sequences(  # tf.keras.utils.pad_sequences用到了numpy2已经删掉的api，手动改
    sequences,
    maxlen=None,
    dtype="int32",
    padding="pre",
    truncating="pre",
    value=0.0,
):
    num_samples = len(sequences)
    lengths = []
    sample_shape = ()
    flag = True
    for x in sequences:
        try:
            lengths.append(len(x))
            if flag and len(x):
                sample_shape = np.asarray(x).shape[1:]
                flag = False
        except TypeError as e:
            raise ValueError(
                "`sequences` must be a list of iterables. "
                f"Found non-iterable: {str(x)}"
            ) from e

    if maxlen is None:
        maxlen = np.max(lengths)

    is_dtype_str = np.issubdtype(dtype, np.str_) or np.issubdtype(
        dtype, np.str_
    )
    if isinstance(value, str) and dtype != object and not is_dtype_str:
        raise ValueError(
            f"`dtype` {dtype} is not compatible with `value`'s type: "
            f"{type(value)}\nYou should set `dtype=object` for variable length "
            "strings."
        )

    x = np.full((num_samples, maxlen) + sample_shape, value, dtype=dtype)
    for idx, s in enumerate(sequences):
        if not len(s):
            continue  # empty list/array was found
        if truncating == "pre":
            trunc = s[-maxlen:]
        elif truncating == "post":
            trunc = s[:maxlen]
        else:
            raise ValueError(f'Truncating type "{truncating}" not understood')

        # check `trunc` has expected shape
        trunc = np.asarray(trunc, dtype=dtype)
        if trunc.shape[1:] != sample_shape:
            raise ValueError(
                f"Shape of sample {trunc.shape[1:]} of sequence at "
                f"position {idx} is different from expected shape "
                f"{sample_shape}"
            )

        if padding == "post":
            x[idx, : len(trunc)] = trunc
        elif padding == "pre":
            x[idx, -len(trunc):] = trunc
        else:
            raise ValueError(f'Padding type "{padding}" not understood')
    return x


X_train = my_pad_sequences(X_train, maxlen=100)
X_test = my_pad_sequences(X_test, maxlen=100)

model = Sequential()
model.add(Embedding(vocabulary, 32))
model.add(SimpleRNN(32))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])
model.fit(X_train, y_train, epochs=5, batch_size=128)
# Epoch 1/5
# 196/196 ━━━━━━━━━━ 4s 10ms/step - acc: 0.6020 - loss: 0.6403
# Epoch 2/5
# 196/196 ━━━━━━━━━━ 1s 7ms/step - acc: 0.8699 - loss: 0.3273
# Epoch 3/5
# 196/196 ━━━━━━━━━━ 1s 7ms/step - acc: 0.9195 - loss: 0.2221
# Epoch 4/5
# 196/196 ━━━━━━━━━━ 1s 7ms/step - acc: 0.9490 - loss: 0.1494
# Epoch 5/5
# 196/196 ━━━━━━━━━━ 1s 7ms/step - acc: 0.9662 - loss: 0.1084

model.evaluate(X_test, y_test, verbose=2)
# 782/782 - 2s - 2ms/step - acc: 0.8277 - loss: 0.4840
