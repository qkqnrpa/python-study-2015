# define
quotes = "I'm bek9."
print(quotes)

double = '"I am bek9." I say.'
print(double)

escape = "\"I am bek9.\" I say."
print(escape)

multiline=""""I am bek9."
I say."""
print(multiline)

# calc
hello = "hello"
world = " world"

print("=" * 50)
print(hello + world)
print("=" * 50)

# indexing
str = "I'mma do what I wanna do"
print(str[4]) # a
print(str[-2]) # d

# slicing
print(str[9:13]) # w(9)h(10)a(11)t(12)
print(str[14:]) # I wanna do
print(str[:8]) # I'mma do

# slicing date
dat = "20151010Sunny"
year = dat[:4]
date = dat[4:8]
weather = dat[8:]
print(year, date, weather) # 2015 1010 Sunny

# replace
wrong = "Pithon"
python = wrong[:1] + 'y' + wrong[2:]
print(wrong, python)

# format
print("My favorite number is %d." % 8)
print("I like %s." % python)
print("I like %d and %s." % (8, python))
print("The important is last %d%%." % 1) # %를 나타낼 때는 \%가 아닌 %% 사용

# format figure
print("%5s" % "hi"); # ___hi
print("%-5s, world" % "hi"); # hi___, world

print("%04d" % 21); # 0021

pi = 3.1415926535
print("%0.2f" % pi) # 3.14
print("%6.2f" % pi) # __3.14

# format function
print("I like {0} and {1}.".format(8, python))
print("I like {python} and {num}.".format(python=python, num=8)) # 파라미터를 key=value로 보내야 한다.

# align
align = "align"
print("{0:<7}|{1:^7}|{2:>7}".format(align, align, align)) # align__|_align_|__align
print("{0:=^12}".format("horizon")) # ==horizon=== (가운데 정렬 시 좌우가 맞지 않으면 왼쪽으로 치우침)
print("{0:!<5}".format("hi")) # hi!!!

print("{0:0.2f}".format(pi)) # 3.14
print("{0:6.2f}".format(pi)) # __3.14

print("The ways of format are use {{index}} or {0}".format("{key}")) # 포맷스트링 내에서는 {, } 표현을 위해 {{, }} 두 번 쓴다(%%와 같은 이치).

# functions
print(python.upper()) # PYTHON
print(python.lower()) # python

print(hello.count("l")) # 2

print(str.find("'")) # 1 (없으면 -1 리턴)
print(str.index("'")) # 1 (없으면 에러)

print(quotes.replace("bek9", "Hyeonjong")) # I'm Hyeonjong.

print(",".join("apple")) # a,p,p,l,e
print(str.split()) # ["I'mma", 'do', 'what', 'I', 'wanna', 'do']

print("  hi  ".lstrip(), "  hi  ".strip(), "  hi  ".rstrip()) # hi__ hi __hi