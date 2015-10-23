# get keyboard input by function : input()
#yyn = int(input("Enter a number"));


'''
# 1. while loop
while True:
    print("running");
    continue; # 1.1. skip the loop.
    break; # 1.2. can be quit by break;
else:
    print("For loop is done");# 1.3 not executed when came out by break.
print("For loop is done");
'''

'''
# 2. for loop.
for i in range(1,5):
    print(i);
else:
    print("The for loop is over");
'''
'''
# 3. function with variable arguments
def total(initial=5, *numbers, **keyword):
    count=initial;
    for number in numbers:
        count+=number;
        print("Number",number);
    for key in keyword:
        count+=keyword[key];
        print("Key",key);
    return count;
print(total(10,1,2,3,vegatable=50,fruits=100));
'''

# 4. use of __doc__
def print_max(x,y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x=int(x);
    y=int(y);
    if x>y:
        print(x,"is maximum");
    else:
        print(y,"is maximum");

'''
# 5. use of sys
import sys
print("The command line arguments are :");
for i in sys.argv:
    print(i);
print("\n\nThe PYTHONPATH is",sys.path,"\n");
'''
'''
# 6. from.. import undesirable
from math import sqrt
print("Square root of 16 is",sqrt(16));
'''
'''
# 7. Check if i am in main.
if __name__=="__main__":
    print("HI");
'''
'''
# 8. list
shoplist=["apple", "mango", "carrot", "banana"];
print("I have",len(shoplist),"items to purchase.");
for item in shoplist:
    print(item,end=" ");
shoplist.append("rice");
shoplist.sort();
print(shoplist);

olditem=shoplist[0];
del shoplist[0];
print(olditem);
print(shoplist);
'''
'''
# 9. tuple
zoo=("python","elephant","penguin");
print(len(zoo));
n_zoo="monkey","camel",zoo;
print(len(n_zoo));
print(n_zoo);
print(n_zoo[2]);
print(n_zoo[2][2]);
print(len(n_zoo)-1+len(n_zoo[2]));
'''
'''
# 10. Dictionary
ab = {"jay" : "01022383728",
      "mom" : "01085353728",
      "dad" : "01095946112",
      "nancy" : "01027103728",
      "spam" : "070..."};

print("My number :",ab["jay"]);

del ab["spam"];
print("Nums :",len(ab));

for name, num in ab.items():
    print(name,":",num);

ab["friend"] = "01012121212";
if "friend" in ab:
    print("HERE!");
'''
'''
# 11. index access 
name = "swaroop";
print(name[0]);
'''
'''
# 12. list
alp = ["a","b","c","d","e","f"];
alp.append(["g","h"]); # add list to list
alp.extend(["i","j"]); # merge lists
print(alp[:]);
print(alp[::2]);
print(alp[:-1]);
'''
'''
# 13. set
bri = set(["aaa","bbb","ccc"]);
print("aaa" in bri);
bric = bri.copy();
bri.add("ddd");
print(bri.issuperset(bric));
bri.remove("ccc");
'''
'''
# 14. reference...
list1 = ["a","b","c"];
list1.append(["e","f"]);
list2 = list1;
list3 = list1[:]; # seems deep copy, but depth of 1
list1[3].remove("e"); # still shallow copy
list1.remove("b");

print(list1);
print(list2);
print(list3);
'''
