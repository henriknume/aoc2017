def is_valid(password):
    words = password.split()
    for w in words:
        if  words.count(w) > 1:
            return False
    return True


def no_anagrams(password):
    words = password.split()
    sorted_words = []
    for w in words:
        sorted_words.append("".join(sorted(w)))
    for sw in sorted_words:
        if  sorted_words.count(sw) > 1:
            return False
    return True


def count_valid_pw(pw_list, part2):
    count = 0
    for pw in pw_list:
        if part2:
            if no_anagrams(pw):
                count += 1
        else:
            if is_valid(pw):
                count += 1
    return count


def main():
    inp = open("./d4.txt").read().splitlines()
    print "T1: %s" % is_valid("aa bb cc dd ee")
    print "T2: %s" % (is_valid("aa bb cc dd aa") == False)
    print "T3: %s" % is_valid("aa bb cc dd aaa")
    print "T4: %s" % (count_valid_pw(["aa c c", "d ee f", "a bbb bb"], False) == 2)
    print "Part 1: %d" % count_valid_pw(inp, False)
    print "T5: %s" % no_anagrams("abcde fghij")
    print "T6: %s" % (no_anagrams("abcde xyz ecdab") == False)
    print "T7: %s" % no_anagrams("a ab abc abd abf abj")
    print "T8: %s" % no_anagrams("iiii oiii ooii oooi oooo")
    print "T9: %s" % (no_anagrams("oiii ioii iioi iiio") == False)
    print "Part 2: %d" % count_valid_pw(inp, True)

if __name__ == "__main__": main()
