



def current_date_string(func1):
    def string1():
        print("This is", end=": ")
        print(func1(), end=". ")
        print("Thanks")
    return string1

@current_date_string
def get_date():
    """log the current date and time"""
    import datetime
    return datetime.datetime.now()

@current_date_string
def add():
    val = 5 + 5
    return val

get_date()
add()
#
# def make_db_dir():
#     """Make db directory"""
#     import os
#     if os.path.exists('./db') is True:
#         pass
#     else:
#         os.mkdir('./db')

# if __name__ == '__main__':

    # print(get_date())
    # make_db_dir()
# print(__name__)