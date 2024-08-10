#Set Comprehension

#Set Comprehension:
#11. Generate a set of odd numbers from 1 to 15 using set comprehension.
odd_numbers = {n for n in range(1, 16) if n % 2 != 0}
print(odd_numbers)

#12. Create a set of the first letter of each word in a sentence.
s="Ashutosh Patil is currently undergoing observayion period in aroha tech"
a={i[0] for i in s.split()}
print(a)

#13. Write a set comprehension to get unique vowels from a sentence.
sen="hello world...!"
v={i for i in sen if i.lower() in ['a','e','i','o','u']}
print(v)

sn="hello world...!"
vo={i:sn.count(i) for i in sn if i.lower() in ['a','e','i','o','u']}
print(vo)

#14. Build a set of square numbers from 1 to 10 using set comprehension.
sq={i**2 for i in range(1,11)}
print(sorted(sq))

#15. Generate a set of prime numbers less than 20 using set comprehension.
pm={i for i in range(1,21) if i%i==0 and i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0}
print(pm)