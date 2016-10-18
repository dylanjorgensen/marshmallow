#https://www.youtube.com/watch?v=NIWwJbo-9_8&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=11




# # Replaces any error
# try:
#     f = open('testfile_misstyped.txt')
# except Exception:
#     print "Oops"




# Replaces specific errors
try:
    f = open('currupt_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Fina11y...")