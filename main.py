import os

def make_kgrams(s, k):
    grams = []
    start, end = 0, k
    while start < len(s) - k + 1:
        grams.append(s[start:end])
        start += 1
        end += 1
    return grams


def right_weight_min(key=lambda x: x):
    def r_min(l):
        cur_min, min_index, i = float('inf'), -1, 0
        while i < len(l):
            if key(l[i]) <= cur_min:
                cur_min, min_index = key(l[i]), i
            i += 1
        return l[min_index]

    return r_min


def winnow(k_grams, k, t):
    min = right_weight_min(lambda x: x[0])
    fingerprints = []
    hashes = [(hash(k_grams[i]), i) for i in range(len(k_grams))]
    window_size = t - k + 1
    w_start, w_end = 0, window_size
    cur_min = None
    while w_end < len(hashes):
        window = hashes[w_start:w_end]
        new_min = min(window)
        if cur_min != new_min:
            fingerprints.append(new_min)
            cur_min = new_min
        w_start, w_end = w_start + 1, w_end + 1
    return fingerprints


def output_fingerprint(fingerprints, kgrams):
    fingerprint_arr = []
    for i in fingerprints:
        fingerprint_arr.append(i[0])
    return fingerprint_arr


k, t = 5, 8

f = open("input.py", "r")
input_file = f.read()
f.close()

k_grams = make_kgrams(input_file, k)
fingerprints = winnow(k_grams, k, t)
set_fingerprints = set(output_fingerprint(fingerprints, k_grams))

match_set = set(fingerprints)

file_list = os.listdir('./samples')

for file in file_list:
    f_r = open("samples/" + file, "r")
    input_file_r = f_r.read()
    f_r.close()
    k_grams = make_kgrams(input_file_r, k)
    fingerprints_r = winnow(k_grams, k, t)
    set_fingerprints_r = set(output_fingerprint(fingerprints_r, k_grams))

    unique_set_fingerprints = set_fingerprints.intersection(set_fingerprints_r)

    print('совпадение', round(len(unique_set_fingerprints) / len(set_fingerprints) * 100, 2), '%')


