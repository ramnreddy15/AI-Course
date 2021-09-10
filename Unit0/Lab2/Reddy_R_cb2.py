# Ram Reddy
# August 31st 2021

# Warmup 2
def string_times(s, n):
    return s*n

def front_times(s, n):
    return s[:3]*n

def string_bits(s):
    return s[::2]

def string_splosion(l):
    return "".join(l[:i] for i in range(len(l)+1))

def last2(s):
    return sum(s[i:i+2]==s[-2:] for i in range(len(s)-2))

def array_count9(n):
    return n.count(9)

def array_front9(n):
    return 9 in n[:4]

def array123(n):
    return any(n[i:i+3]==[1,2,3] for i in range(len(n)))

def string_match(a, b):
    return sum(a[i:i+2]==b[i:i+2] for i in range(len([b,a][a>b])-1))

# Logic 2

def make_bricks(s, b, g):
    return not(g>b*5+s or g%5>s)

def lone_sum(a, b, c):
    return sum(x for x in [a,b,c] if [a,b,c].count(x)==1)

def lucky_sum(a, b, c):
    return sum([a,b,c][:[[[3,2][c==13],1][b==13],0][a==13]])

def no_teen_sum(a, b, c):
    return a+b+c-sum([a,b,c].count(i)*i for i in [13,14,17,18,19])

def round_sum(a, b, c):
    return sum((i+5)//10*10 for i in [a,b,c])

def close_far(a, b, c):
    return abs(b-a)<=1 and abs(b-c)>=2 and abs(c-a)>=2 or abs(c-a)<=1 and abs(b-c)>=2 and abs(b-a)>=2

def make_chocolate(s, b, g):
    return [-1,g-5*[b,g//5][g//5<=b]][5*[b,g//5][g//5<=b]+s>=g]

# String 2
def double_char(s):
    return ''.join(2*i for i in s)

def count_hi(s):
    return s.count('hi')

def cat_dog(s):
    return s.count('cat')==s.count('dog')

def count_code(s):
    return sum(s[i:i+4][:2]=='co' and s[i:i+4][3]=='e' for i, j in enumerate(s[:-3].lower()))

def end_other(a, b):
    return a[-len(b)+0:].lower()==b.lower() or b[-len(a)+0:].lower()==a.lower()

def xyz_there(s):
    return 'xyz' in s.replace('.xyz','_')

# List 2

def count_evens(n):
    return len(n)-sum(i%2 for i in n)

def big_diff(n):
    return max(n)-min(n)

def centered_average(n):
    return sum(sorted(n)[1:-1])//(len(n)-2)

def sum13(n):
    return sum(j for i, j in enumerate(n) if (i==0 and j!=13) or (i>0 and j!=13 and n[i-1]!=13))

def sum67(u):
    return sum67(u[:u.index(6)]+u[u.index(7,u.index(6))+1:]) if 6 in u else sum(u)

def has22(n):
    return (2,2) in zip(n,n[1:])