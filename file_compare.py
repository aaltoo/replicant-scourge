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


def file_compare(file1, file2):
    k_grams1 = make_kgrams(file1, k)
    fingerprints = winnow(k_grams1, k, t)
    set_fingerprints1 = set(output_fingerprint(fingerprints, k_grams1))

    k_grams2 = make_kgrams(file2, k)
    fingerprints = winnow(k_grams2, k, t)
    set_fingerprints2 = set(output_fingerprint(fingerprints, k_grams2))

    unique_set_fingerprints = set_fingerprints1.intersection(set_fingerprints2)

    return round(len(unique_set_fingerprints) / len(set_fingerprints1), 3)
