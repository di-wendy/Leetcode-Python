##1.Data Type Conversion

           | Integer         | String        |Binary       |
--------   | --------------- | ------------- |-------------|
Integer    |      -          | str(int)      |bin(int)[2:] |
String     |    int(str)     |      -        |      -      |
Binary     |int("bianry",n=2)|      -        |      -      |

##2.String Manipulation
###2.1 Reverse a String (倒置str)
str2 = str1[::-1]

##3.Array
###3.1 Array的加减
matrix = [1,2,3]]+[2,3,4]
matrix = [1,2,3,4,5,6]

matrix = [[1,2,3]]+[[2,3,4]]
matrix = [[1,2,3],[2,3,4]]

c = np.subtract(a,b)

###3.x 技巧
判断Array是否为空集
Array != []
判断Array是否相等
np.array_equal(a,b)

###python列表去重
http://www.cnblogs.com/linxiyue/p/3912315.html


##4.Stack & Queue

##Appendix. Set Object
sets — Unordered collections of unique elements
无顺序，无indexing
