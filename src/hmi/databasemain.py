
import pandas 
import math



def read_database_file(file_path):
    #read data from file excel
    data_base = pandas.read_excel(file_path)

    #lấy số lượng hàng trong danh sách 
    num_columns = len(data_base.columns)
    num_rows = len(data_base)
    
    #khởi tạo một dictionary để lưu trữ dữ liệu các cột
    data_list = []

    # lấy dữ liệu các cột và lưu vào dictionary
    for i in range(num_rows):
        row_data = []
        for j in range(num_columns):
            data = data_base.iat[i, j]
            data = "----" if pandas.isna(data) else data
            row_data.append(data)
        data_list.append(row_data)


    return data_list

# def read_latitude_longitude_database(file_path, nu):
#     data_base = pandas.read_excel(file_path)
    
#     data_list = []

def read_latitude_longitude_database(file_path):
    """
    Đọc dữ liệu từ file Excel và trả về nhiều hàng dưới dạng danh sách (list).
    :param file_path: đường dẫn đến file Excel
    :param sheet_name: tên sheet trong file Excel
    :param num_rows: số lượng hàng cần đọc
    :return: danh sách các hàng (mỗi hàng là một danh sách)
    """
    # Đọc dữ liệu từ file Excel
    df = pandas.read_excel(file_path)

    # Trích xuất n hàng đầu tiên
    rows = []
    for i in range(10):
        row = df.iloc[i].tolist()
        rows.append(row)

    delete_nan = [rows[i][2:] for i in range(len(rows))]

    # Tạo một mảng mới để lưu trữ kết quả
    filter = []

    # Duyệt qua từng phần tử trong mảng A
    for i in range(len(delete_nan)):
        if not all(math.isnan(x) for x in delete_nan[i]):
            # Nếu phần tử không phải là [nan, nan], thêm nó vào mảng B
            filter.append(delete_nan[i])

    return filter


path_file_database = r'src\hmi\database.xlsx'

rows = read_latitude_longitude_database(path_file_database)

print(rows)

