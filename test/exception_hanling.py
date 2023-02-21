#khối try sẽ tao ra một ngoại lệ, bỏi vì x không được xác định.
"""
try:
    print(x)
except:
    print("an exception occurred")
"""

# try:
#     print(x)
# except:
#     print("Variable x is not defined")
# finally:
#     print("Something else went wrong")

#điều này có thể hữu ích để đóng các đối tượng và dọn sạch tài nguyên
import sys
try:
    f = open("demofile.text")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")