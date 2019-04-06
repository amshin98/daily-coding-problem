'''
So school hit like a train and what a week oof. So my goal of doing these daily
isn't realistic because I decided to take the time I'd take to do these and
work on personal projects instead, as #learnbydoing rather than these kinds of
things. I'll still do them if I have time or the urge to, but I've been putting
some of this stuff off for a while and I gotta get it done. I should make a
blog lol.

Alright so it's sorted, that's a hint. Let's write tests first, maybe that'll
help. also O(n) so loop through list once.
'''

def first_try(test_list):
    cur_sum = 1
    for num in test_list:
        if cur_sum < num:
            return cur_sum
        cur_sum += num

    return cur_sum