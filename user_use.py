# @Time  : 2020/6/10 0010 4:36
# @Author: CaiYe
# @File  : user_use.py


# from user_class import User
import user_privileges

admin1 = user_privileges.Admin('admin', '1', 'none')
admin1.privileges.show_privileges()