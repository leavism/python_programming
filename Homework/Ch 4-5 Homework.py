''' Ch1 Homework
Helen Sun 1/4/2016
Giahuy Dang
'''

# Exercise 4.11
input_month, input_year = eval(input("Enter a month and year: "))

if input_month == 1:
    print("January",input_year,"has 31 days")
elif input_month == 2:
    isLeapYear = (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0)
    if isLeapYear == True:
        print("February",input_year,"has 29 days")
    else:
        print("February",input_year,"has 28 days")
elif input_month == 3:
    print("March",input_year,"has 31 days")
elif input_month == 4:
	print("April",input_year,"has 30 days")
elif input_month == 5:
	print("May",input_year,"has 31 days")
elif input_month == 6:
	print("June",input_year,"has 30 days")
elif input_month == 7:
	print("July",input_year,"has 31 days")
elif input_month == 8:
	print("August",input_year,"has 31 days")
elif input_month == 9:
	print("September",input_year,"has 30 days")
elif input_month == 10:
	print("October",input_year,"has 31 days")
elif input_month == 11:
	print("November",input_year,"has 30 days")
elif input_month == 12:
	print("December",input_year,"has 30 days")
else:
	print("You did not enter correct months and years.")

'''
Results:
Enter a month and year: 2, 2016
February 2016 has 29 days
'''

# Exercise 4.17
import random
hand_gen = random.randint(0,2)
hand_input = eval(input("scissor (0), rock(1), paper(2): "))

	#Input hand text conversion
if hand_input == 0:
	result_hand_input = "You are scissor."
elif hand_input == 1:
	result_hand_input = "You are rock."
else:
	result_hand_input = "You are paper."
	#Computer generated hand text conversion
if hand_gen == 0:
	result_hand_gen = "The computer is scissor."
elif hand_gen == 1:
	result_hand_gen = "The computer is rock."
else:
	result_hand_gen = "The computer is paper."
	#Judge determines who wins :)
draw = "It is a draw."
win = "You win."
lose = "You lose."
if hand_gen == 0:
	if hand_input == 0:
		print(result_hand_gen,result_hand_input,draw)
	elif hand_input == 1:
		print(result_hand_gen,result_hand_input,win)
	else:
		print(result_hand_gen,result_hand_input,lose)
elif hand_gen == 1:
	if hand_input == 0:
		print(result_hand_gen,result_hand_input,lose)
	elif hand_input == 1:
		print(result_hand_gen,result_hand_input,draw)
	else:
		print(result_hand_gen,result_hand_input,win)
else:
	if hand_input == 0:
		print(result_hand_gen,result_hand_input,win)
	elif hand_input == 1:
		print(result_hand_gen,result_hand_input,lose)
	else:
		print(result_hand_gen,result_hand_input,draw)

'''
Results:
scissor (0), rock(1), paper(2): 1
The computer is rock. You are rock. It is a draw.

scissor (0), rock(1), paper(2): 2
The computer is rock. You are paper You win.
 
scissor (0), rock(1), paper(2): 2
The computer is paper. You are paper. It is a draw.

scissor (0), rock(1), paper(2): 1
The computer is rock. You are rock. It is a draw.

scissor (0), rock(1), paper(2): 0
The computer is rock. You are scissor. You lose.

scissor (0), rock(1), paper(2): 1
The computer is paper. You are rock. You lose.
'''

# Exercise 5.3
print("Kilograms      Pounds")
for k in range(1, 200):
    print(format(k,"<10.0f"),format(k * 2.2,"10.1f"))

''' 
 Results:
Kilograms      Pounds
1                 2.2
2                 4.4
3                 6.6
4                 8.8
5                11.0
6                13.2
7                15.4
8                17.6
9                19.8
10               22.0
11               24.2
12               26.4
13               28.6
14               30.8
15               33.0
16               35.2
17               37.4
18               39.6
19               41.8
20               44.0
21               46.2
22               48.4
23               50.6
24               52.8
25               55.0
26               57.2
27               59.4
28               61.6
29               63.8
30               66.0
31               68.2
32               70.4
33               72.6
34               74.8
35               77.0
36               79.2
37               81.4
38               83.6
39               85.8
40               88.0
41               90.2
42               92.4
43               94.6
44               96.8
45               99.0
46              101.2
47              103.4
48              105.6
49              107.8
50              110.0
51              112.2
52              114.4
53              116.6
54              118.8
55              121.0
56              123.2
57              125.4
58              127.6
59              129.8
60              132.0
61              134.2
62              136.4
63              138.6
64              140.8
65              143.0
66              145.2
67              147.4
68              149.6
69              151.8
70              154.0
71              156.2
72              158.4
73              160.6
74              162.8
75              165.0
76              167.2
77              169.4
78              171.6
79              173.8
80              176.0
81              178.2
82              180.4
83              182.6
84              184.8
85              187.0
86              189.2
87              191.4
88              193.6
89              195.8
90              198.0
91              200.2
92              202.4
93              204.6
94              206.8
95              209.0
96              211.2
97              213.4
98              215.6
99              217.8
100             220.0
101             222.2
102             224.4
103             226.6
104             228.8
105             231.0
106             233.2
107             235.4
108             237.6
109             239.8
110             242.0
111             244.2
112             246.4
113             248.6
114             250.8
115             253.0
116             255.2
117             257.4
118             259.6
119             261.8
120             264.0
121             266.2
122             268.4
123             270.6
124             272.8
125             275.0
126             277.2
127             279.4
128             281.6
129             283.8
130             286.0
131             288.2
132             290.4
133             292.6
134             294.8
135             297.0
136             299.2
137             301.4
138             303.6
139             305.8
140             308.0
141             310.2
142             312.4
143             314.6
144             316.8
145             319.0
146             321.2
147             323.4
148             325.6
149             327.8
150             330.0
151             332.2
152             334.4
153             336.6
154             338.8
155             341.0
156             343.2
157             345.4
158             347.6
159             349.8
160             352.0
161             354.2
162             356.4
163             358.6
164             360.8
165             363.0
166             365.2
167             367.4
168             369.6
169             371.8
170             374.0
171             376.2
172             378.4
173             380.6
174             382.8
175             385.0
176             387.2
177             389.4
178             391.6
179             393.8
180             396.0
181             398.2
182             400.4
183             402.6
184             404.8
185             407.0
186             409.2
187             411.4
188             413.6
189             415.8
190             418.0
191             420.2
192             422.4
193             424.6
194             426.8
195             429.0
196             431.2
197             433.4
198             435.6
199             437.8
'''
# Exercise 5.17

i = 10
count = 0
for k in range(33, 127):
	print(chr(k), end = " ")
	count += 1
	if count % i == 0:
		print()

'''
Results:
! " # $ % & ' ( ) * 
+ , - . / 0 1 2 3 4 
5 6 7 8 9 : ; < = > 
? @ A B C D E F G H 
I J K L M N O P Q R 
S T U V W X Y Z [ \ 
] ^ _ ` a b c d e f 
g h i j k l m n o p 
q r s t u v w x y z 
{ | } ~ 
'''

# Exercise 5.29
i = 10
count = 0
for ly in range(2001, 2101):
	isLeapYear = (ly % 4 == 0 and ly % 100 != 0) or (ly % 400 == 0)
	if isLeapYear == True:
		print(ly, end = " ")
		count += 1
	if count % i == 0:
		print()

''' Results:
2004 2008 2012 2016 2020 2024 2028 2032 2036 2040 
2044 2048 2052 2056 2060 2064 2068 2072 2076 2080 
2084 2088 2092 2096
'''