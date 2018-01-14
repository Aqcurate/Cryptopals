def hamming(a, b):
    res = 0
    for i, j in zip(a, b):
        val = i ^ j
        while val != 0:
            res += 1
            val &= val - 1
    return res

def guess_key_len(a, min_=2, max_=40):
    def avg_hamming(a, chunk):
        num_chunks = len(a) // chunk - 1
        return sum([hamming(a[k*chunk:(k+1)*chunk], a[(k+1)*chunk:(k+2)*chunk])
                for k in range(num_chunks)]) / (num_chunks * chunk)

    return sorted(range(min_, max_), key=lambda chunk: avg_hamming(a, chunk))

if __name__ == '__main__':
    assert(hamming(
        'this is a test'.encode('UTF-8'),
        'wokka wokka!!!'.encode('UTF-8')) == 37)

