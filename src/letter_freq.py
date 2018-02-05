from string import ascii_lowercase, printable

def english_chi_squared(a):
    letter_freq = {
        'a' : 8.167,
        'b' : 1.492,
        'c' : 2.782,
        'd' : 4.253,
        'e' : 12.70,
        'f' : 2.228,
        'g' : 2.015,
        'h' : 6.094,
        'i' : 6.966,
        'j' : 0.153,
        'k' : 0.772,
        'l' : 4.025,
        'm' : 2.406,
        'n' : 6.749,
        'o' : 7.507,
        'p' : 1.929,
        'q' : 0.095,
        'r' : 5.987,
        's' : 6.327,
        't' : 9.056,
        'u' : 2.758,
        'v' : 0.978,
        'w' : 2.360,
        'x' : 0.150,
        'y' : 1.974,
        'z' : 0.074,
    }


    letter_freq.update((k, v*len(a)/100) for k, v in letter_freq.items())

    for c in a:
        if not c in printable.encode('UTF-8'):
            return 1000*1000

    return sum([((letter_freq[l] - a.count(l.encode('UTF-8')))**2 / letter_freq[l])
            for l in ascii_lowercase])


