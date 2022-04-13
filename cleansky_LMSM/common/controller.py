import cleansky_LMSM.common.database as database
import cleansky_LMSM.common.model as model
import cleansky_LMSM.common.view as view
import logging


class RightsGraph:
    """
    该类实现了权限的展示和查询的数据结构，使用图结构存储用户和设备的多对多关系

    成员介绍：

    element_dict : 字典类型， 某一用户-->该用户拥有权限的所有设备
    {user_id--->(role_id, ele_type, ele_id)}

    person_dict : 字典类型， 某一设备-->所有对该设备拥有权限的用户
    {(ele_type, ele_id)--->(user_id, role)}

    mat : user_right 表查询出的二维矩阵

    sparse_mat : mat所对应的稀疏矩阵
    (user_id, role_id, element_type(排除前两列的矩阵), element_id)
    """
    def __init__(self):
        self.element_dict, self.person_dict, self.mat, self.sparse_mat = {}, {}, [], []
        # 用来记录全部用户的集合
        self.user_set = set()
        self.admin_set = set()

    def update_graph(self, data):
        """
        稀疏矩阵元素 - (user_id, role_id, element_type(排除前两列的矩阵), element_id)
        """
        self.element_dict, self.person_dict, self.mat, self.sparse_mat = {}, {}, [], []
        self.mat = data

        for vet in self.mat:

            if vet[1] == 6:
                # self.sparse_mat.append((vet[0], vet[1], None, None))
                # 添加没有权限的员工进入用户集合
                self.user_set.add(vet[0])
                continue

            if vet[1] == 1:
                # 添加管理员
                self.admin_set.add(vet[0])

            for item in vet[2:]:
                # 添加其他成员
                if item is not None:

                    self.sparse_mat.append((vet[0], vet[1], vet[2:].index(item), item))
                    self.user_set.add(vet[0])

                    if (vet[2:].index(item), item) in self.person_dict.keys():
                        self.person_dict[(vet[2:].index(item), item)].append((vet[0], vet[1]))
                    else:
                        self.person_dict[(vet[2:].index(item), item)] = [(vet[0], vet[1])]

                    if (vet[0],) in self.element_dict.keys():
                        self.element_dict[(vet[0],)].append((vet[1], vet[2:].index(item), item))
                    else:
                        self.element_dict[(vet[0],)] = [(vet[1], vet[2:].index(item), item)]

        # logging.info("graph updated")
        # print(self)
        self.print_admin_set()
        self.print_user_set()
        self.print_sparse_mat()
        self.print_ele_dict()
        self.print_per_dict()

    def __repr__(self):
        # 很奇怪，重载会报错
        print("\n---------------------------")
        # print(self.__class__)
        self.print_admin_set()
        self.print_user_set()
        self.print_sparse_mat()
        self.print_ele_dict()
        self.print_per_dict()
        print("----------------------------\n")

    def print_admin_set(self):
        print("admin_set : ")
        print(self.admin_set)

    def print_user_set(self):
        print("user_set : ")
        print(self.user_set)

    def get_user_right(self, uid):
        """
        查找某个用户节点的所有的邻接element节点
        """
        return self.element_dict[(uid,)]

    def get_right_tables(self, tup):
        """
        输入： tup = (element_type_id, element_ref_id)
        查找某个元素节点的全部领接person节点
        这个接口的名字起的不好
        """
        return self.person_dict[tup]

    def get_total_info_of_node(self, model_object, tup):
        """
        return None or [element_type, element_id, role, uname]
        返回的是字符串数组
        """
        if tup in self.sparse_mat:
            uname = model_object.model_get_username_by_uid(uid=tup[0])[0][0]
            # 传入的是四元祖
            info = model_object.tools_get_elements_info(list(tup))
            return info + [uname]
        else:
            return None

    def get_certain_element_owner_set(self, tup):
        """传入的是元素tuple, 返回的是拥有这个元素的uid集合"""
        owner_set = set()
        if tup in self.person_dict.keys():
            for item in self.person_dict[tup]:
                owner_set.add(item[0])
        return owner_set

    def get_certian_element_others_set(self, tup):
        """
        传入元素元组，返回拥有者和其他人的集合
        """
        owner_set = self.get_certain_element_owner_set(tup)
        other_set = self.user_set - owner_set
        return other_set

    def print_matrix(self):
        print('mat = :')
        print(self.mat)

    def print_sparse_mat(self):
        print('sparse_mat = :(user_id, role_id, element_type(排除前两列的矩阵), element_id)')
        print(self.sparse_mat)

    def print_ele_dict(self):
        print('ele_dict = :{user_id--->(role_id, ele_type, ele_id)}')
        print(self.element_dict)

    def print_per_dict(self):
        print('per_dict = :{(ele_type, ele_id)--->(user_id, role)}')
        print(self.person_dict)


class Controller:
    """
    Controller基类负责实现控制器所共有的接口
    """
    right_graph = RightsGraph()

    def __init__(self, my_program, my_view, my_model, my_role):
        """
        """
        self.__view = my_view
        self.__model = my_model
        self.__role = my_role
        self.__program = my_program
        self.__view.set_controller(self)
        self.__model.set_controller(self)

    def action_start_transaction(self):
        self.get_model().model_start_transaction()

    def action_roll_back(self):
        self.get_model().model_roll_back()
        self.tools_update_graph()

    def action_submit(self):
        self.get_model().model_commit()
        self.tools_update_graph()

    def action_is_in_transaction(self):
        return self.get_model().is_in_transaction()

    def get_program(self):
        return self.__program

    def get_view(self):
        return self.__view

    def get_model(self):
        return self.__model

    def get_role(self):
        return self.__role

    def run_view(self):
        self.__view.run_view()

    @staticmethod
    def tools_tuple_to_list(list_tuple):
        """
        单元素返回结果，拼装成列表
        """
        if not list_tuple:
            return []

        ret = []
        for item in list_tuple:
            ret.append(list(item)[0])
        return ret

    @staticmethod
    def tools_tuple_to_matrix(list_tuple):
        """
        多元素返回结果，拼装成矩阵, 这个函数有过度设计的嫌疑。。。
        """
        if not list_tuple:
            return []

        ret = []
        for item in list_tuple:
            ret.append(list(item))
        return ret

    @staticmethod
    def tools_delete_first_column(mat):
        for item in mat:
            item.pop(0)
        return mat

    def tools_update_graph(self):
        mat = Controller.tools_tuple_to_matrix(self.get_model().model_get_all_rights())
        self.right_graph.update_graph(Controller.tools_delete_first_column(mat))


class LoginController(Controller):
    def __init__(self, my_program, db_object, my_role):
        super(LoginController, self).__init__(my_program=my_program,
                                              my_view=view.LoginView(),
                                              my_model=model.LoginModel(db_object=db_object),
                                              my_role=my_role)

    def action_login(self):
        temp_username = self.get_view().get_username()
        temp_password = self.get_view().get_password()
        user_info = self.get_model().model_login(temp_username, temp_password)
        if not user_info:
            self.get_view().login_fail()
        else:
            self.get_view().login_success()
            self.get_role().set_user_info(user_info=user_info)
            self.tools_update_graph()
            self.get_program().run_menu(self.get_role())


class MenuController(Controller):
    def __init__(self, my_program, db_object, my_role):
        super(MenuController, self).__init__(my_program=my_program,
                                             my_view=view.MenuView(),
                                             my_model=model.MenuModel(db_object=db_object),
                                             my_role=my_role)

    def action_open_management(self):
        self.get_view().close_window()
        self.get_program().run_management()

    def action_open_items_to_be_tested(self):
        self.get_view().close_window()
        self.get_program().run_items_to_be_tested()


class ManagementController(Controller):
    def __init__(self, my_program, db_object, role):
        super(ManagementController, self).__init__(my_program=my_program,
                                                   my_view=view.ManagementView(),
                                                   my_model=model.ManagementModel(db_object=db_object),
                                                   my_role=role)

    def action_fill_organisation(self):
        sql_result = self.get_model().model_get_orga()
        return self.tools_tuple_to_list(sql_result)

    def action_fill_user_list(self, orga):
        lis = self.get_model().model_get_list_of_users_by_organisation(orga)
        return Controller.tools_tuple_to_list(lis)

    def action_fill_user_table(self):
        """元组列表不需要转换成矩阵。。。"""
        user_list = self.get_model().model_get_list_of_users()
        # ret_table = []
        # for item in user_list:
        #     row = []
        #     for col in item:
        #         row.append(col)
        #     ret_table.append(row)
        return user_list

    def action_fill_user_right_table(self, txt):
        sql_ret = self.get_model().model_get_user_id(uname=txt)
        if not sql_ret:
            return []
        test_role = self.get_model().model_user_have_role(uid=sql_ret[0][0])
        if test_role[0] == (6,):
            return []
        uid = sql_ret[0][0]
        print('uid = ' + str(uid))
        if uid == 1 or uid == 2:
            return []
        list_of_tup = Controller.right_graph.get_user_right(uid=uid)
        # tup --- (role_id, ele_type, ele_id)
        mat = []
        for item in list_of_tup:
            item = list(item)
            mat.append(self.get_model().tools_get_elements_info(item))
        return mat

    def action_fill_fname_lname(self, uname):
        fname = self.get_model().model_get_fname(uname)
        if fname:
            fname = self.tools_tuple_to_list(fname)

        lname = self.get_model().model_get_lname(uname)
        if lname:
            lname = self.tools_tuple_to_list(lname)

        print(fname)
        print(lname)

        return fname, lname

    def action_fill_administrator_table(self):
        mat = []
        for tup in Controller.right_graph.sparse_mat:
            if tup[1] == 2:
                info = Controller.right_graph.get_total_info_of_node(self.get_model(), tup)
                if info is not None:
                    uname = info[3]
                    ele_info = info[0:2]
                    mat.append(ele_info + [uname])
        if not mat:
            return None
        else:
            return mat

    def action_validate_user(self, lis):
        """
        关于接口的调整，不需要下面这行代码，虽然这行代码很酷炫
        """
        # lis = [i if i != '' else None for i in lis]
        if not self.get_model().model_get_uid_by_uname(lis[0]):
            #     系统中不存在该用户
            self.get_model().model_create_new_user(uname=lis[0], orga=lis[1], fname=lis[2], lname=lis[3], tel=lis[4],
                                                   email=lis[5], password=lis[6])
            self.get_view().add_table_user_modify([lis[0], 'CREATE'])
        else:
            self.get_model().model_update_user(uname=lis[0], new_username=lis[0], organisation=lis[1],
                                               last_name=lis[3], tel=lis[4], first_name=lis[2],
                                               email=lis[5], password=lis[6])
            self.get_view().add_table_user_modify([lis[0], 'UPDATE'])
        self.tools_update_graph()
        self.get_view().refresh()

    def action_delete_user(self, uname):
        uid = self.get_model().model_get_uid_by_uname(uname)
        if uid:
            self.get_model().model_delete_user(uname)
            self.tools_update_graph()
            self.get_view().add_table_user_modify([uname, 'DELETE'])
            self.get_view().refresh()

    def action_fill_coating(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_coatings())

    def action_fill_detergent(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_detergent())

    def action_fill_insect(self):
        return ['YES', 'NO']

    def action_fill_means(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_means())

    def action_fill_tank(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_tank())

    def action_fill_sensor(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_sensor())

    def action_fill_acqui(self):
        return ['YES', 'NO']

    def action_fill_ejector(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_ejector())

    def action_fill_camera(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_camera())

    def action_fill_teams(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_teams())

    def action_test_points(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_points())

    def action_fill_intrinsic(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_intrinsic())

    def action_fill_rights(self):
        return Controller.tools_tuple_to_list(self.get_model().model_get_rights())

    def action_fill_combobox_test_mean(self, txt):
        data = self.get_model().model_get_means_name_by_means_type(txt)
        return self.tools_tuple_to_list(data)

    def action_fill_serial(self, mean_type, mean_name):
        data = self.get_model().model_get_means_number_by_means_name(mean_type, mean_name)
        return self.tools_tuple_to_list(data)

    def action_fill_user_right_list(self, table_number, ref_tup):
        """
        table_number取决于调用本函数的槽函数，对应于model类中定义的表字典
        ref_tup有可能是三元组，也有可能是单元组
        """
        lis = []
        mat = []
        if not self.get_model().model_get_ele_id_by_ref(table_number, ref_tup):
            # 不存在这种element, 返回全体成员
            print('不存在这种元素')
            others_set = self.right_graph.user_set
            for item in iter(others_set):
                lis.append(self.get_model().model_get_username_by_uid(item)[0][0])
            return None, lis
        else:
            print('存在这种元素')
            element_id = self.get_model().model_get_ele_id_by_ref(table_number, ref_tup)[0][0]
            print('元素id = ' + str(element_id))

            others_set = set()
            # 判断是否有人拥有这种元素
            print((table_number, element_id))
            print(self.right_graph.person_dict.keys())
            if (table_number, element_id) in self.right_graph.person_dict.keys():
                print("有人拥有这种元素")
                list_of_owners = self.right_graph.person_dict[(table_number, element_id)]
                others_set = self.right_graph.get_certian_element_others_set((table_number, element_id))

                for item in list_of_owners:
                    # 遍历每一个拥有者节点，获得权限信息和用户名信息
                    role_str = self.get_model().model_get_role_ref(item[1])[0][0]
                    username = self.get_model().model_get_username_by_uid(item[0])[0][0]
                    mat.append([username, role_str])
            else:
                print("没有人拥有这种元素")
                mat = None
                others_set = self.right_graph.user_set

            for item in iter(others_set):
                lis.append(self.get_model().model_get_username_by_uid(item)[0][0])

            print(mat)
            print(lis)
            return mat, lis

    def action_change_role(self, element_type, ref_tup, person_name, role_str, state):
        print('element_type: ' + str(element_type))
        print('element_info: ' + str(ref_tup))
        print('person_name: ')
        print(person_name)
        print('role_str: ' + role_str)
        print('state = ' + str(state))

        if not self.get_model().model_get_ele_id_by_ref(element_type, ref_tup):
            # 不存在这种element
            # 创建新元素，判断元素信息是否合法
            if element_type == 0:
                for item in ref_tup:
                    if item == '':
                        print("输入不合法")
                        return
            else:
                if ref_tup[0] == '':
                    print("输入不合法")
                    return
            self.get_model().model_create_new_element(element_type, ref_tup)
            print("成功创建新元素")

        uid = self.get_model().model_get_uid_by_uname(uname=person_name)[0][0]
        role_id = self.get_model().model_get_role_id(role_ref=role_str)[0][0]
        element_id = self.get_model().model_get_ele_id_by_ref(table_number=element_type, ref_tup=ref_tup)[0][0]

        if state == 0 and role_str == 'none':
            print("删除userright中的一行")
            self.get_model().model_delete_user_right(uid=uid, element_type=element_type, element_id=element_id)

        if state == 0 and role_str != 'none':
            print("update userright中的一行")
            self.get_model().model_update_user_right(uid=uid, element_type=element_type, element_id=element_id,
                                                     role_id=role_id)

        if state == 1 and role_str != 'none':
            print("insert userright中的一行")
            self.get_model().model_insert_user_right(uid=uid, element_type=element_type, element_id=element_id,
                                                     role_id=role_id)

        self.tools_update_graph()


class ItemsToBeTestedController(Controller):
    def __init__(self, my_program, db_object, role):
        super(ItemsToBeTestedController, self).__init__(my_program=my_program,
                                                        my_view=view.ItemsToBeTestedView(),
                                                        my_model=model.ItemsToBeTestedModel(db_object=db_object),
                                                        my_role=role)
        # self.get_model().model_start_transaction()

    def action_get_coatings(self):
        """
        根据当前登录用户的身份查找属于他的coating元素，并展示在combobox中
        """
        uid = self.get_role().get_uid()
        if uid in self.right_graph.admin_set:
            # 如果是管理员，则显示全部coating类别
            return self.tools_tuple_to_list(self.get_model().model_get_coatings())
        if (uid,) not in self.right_graph.element_dict.keys():
            # 用户什么权限也没有，什么都不返回（在user_right中只有一行权限为6的记录，这时候用户是不会被添加到字典中的，只会存在在稀疏矩阵中）
            return []
        else:
            # 用户有对某一个设备的权限，其身份不为管理员，此时需要筛选出其对coating设备的记录
            lis = []
            for item in self.right_graph.element_dict[(uid,)]:
                if item[1] == 1 and item[0] < 6:
                    # 如果item[0]这一项小于六，意味着至少有只读权限，所以添加到lis中
                    lis.append(item[2])
            if not lis:
                # 用户没有对任何coating的权限
                return lis
            else:
                ret = []
                for item in lis:
                    ret.append(self.get_model().model_get_simple_ele(table_name='type_coating', ele_id=item)[0][0])
                return ret

    def action_get_coating_position(self, coating_type):
        """
        选择好coating之后，首先从coating表中查找
        首先判断是否存在这种coating
        """
        coating_id = self.get_model().model_get_ele_id_by_ref(1, (coating_type,))
        if not coating_id:
            # 不存在这种coating type
            return []
        else:
            # 存在这种type
            # 权限查询
            data = self.get_model().model_get_coating_number(coating_type=coating_type)
            if not data:
                return []
            else:
                return self.tools_tuple_to_list(data)

    def action_get_coating_table(self, element_type, number_name):
        mat = self.get_model().model_get_coating_attributes(element_type, number_name)
        if not mat:
            mat = None
        return mat

    def action_configue_by_type_number(self, element_type, number_name):
        # coating_type没填，直接返回
        if element_type == '':
            self.get_view().disable_modify_coating()
            return None, None, None

        coating_id = self.get_model().model_get_simple_id(table_name='type_coating', ele_ref=element_type)
        coating_id = coating_id[0][0]

        # 权限图中必定存在一条边描述该用户和该设备的关系，找出权限
        uid = self.get_role().get_uid()
        token = None
        if uid in self.right_graph.admin_set:
            token = 1
        else:
            ele_lis = self.right_graph.element_dict[(uid,)]
            for item in ele_lis:
                if item[1] == 1 and item[2] == coating_id:
                    token = item[0]

        if token == 6:
            self.get_view().disable_modify_coating()
            return None, None, None

        # 填充list
        mat = self.get_model().model_get_coating_attributes(element_type, number_name)
        if not mat:
            mat = None

        # 填充chara和unity
        chara, unity = [], []
        if token < 6:
            # 用type coating查找
            chara = self.get_model().model_get_coating_char(element_type)
            if chara:
                chara = self.tools_tuple_to_list(chara)

            unity = self.tools_tuple_to_list(self.get_model().model_get_unity())

        # 判断number是否存在
        # 如果数据被validate了，擦去db transfer， search， create
        is_validate = self.get_model().model_is_validate_coating(element_type, number_name)
        if is_validate:
            # 存在这种元素
            is_validate = is_validate[0][0]
            if is_validate:
                # validated
                self.get_view().disable_modify_coating()
            else:
                # not validated
                if token == 5:
                    # 只读用户
                    self.get_view().disable_modify_coating()
                #     这里可以加一条将三元组设置成不可编辑
                elif token == 4:
                    # 只有创建权限的用户
                    self.get_view().one_click_coating()
                    self.get_view().enable_modify_coating()
                else:
                    # valid或者admin或者manager
                    self.get_view().question_for_validate_coating()
                    self.get_view().enable_modify_coating()
        else:
            self.get_view().enable_modify_coating()
            print("\n不存在这种元素\n")
        return chara, unity, mat

    def action_create_coating(self, coating_name, coating_number, attribute_name, unity, value):
        """
        如果用户点击了，肯定是有权限创建的，所以权限检查不需要做

        其次，将create的粒度降低，如果当前没有position，就算attribute，unity和value被填充了，也不会创建对应的attribute
        必须先点击一次create将position创建好了，再点击一次create才可以insert attribute
        """
        if not coating_name:
            return

        if not coating_number:
            return

        coating_id = self.get_model().model_get_simple_id(table_name='type_coating', ele_ref=coating_name)[0][0]
        print(coating_id)
        coating_exist = self.get_model().model_is_exist_coating(coating_name, coating_number)
        print(coating_exist)

        if not coating_exist:
            # 先判断number是否存在，如果不存在，创建number随后直接返回
            self.get_model().model_create_new_coating(coating_id, coating_number)
            print("新number"+coating_number+"已创建")
        else:
            if not attribute_name:
                # 如果输入不合法，没有attribute_name直接返回
                return
            print("number"+coating_number+"已经存在")
            unity_id = self.get_model().model_is_unity_exist(unity)
            if not unity_id:
                # 如果不存在单位，先创建单位
                unity_id = self.get_model().model_create_new_unity(unity)[0][0]
                print("新单位"+unity+"已创建")
            else:
                unity_id = unity_id[0][0]
            print("unity_id="+str(unity_id))

            # 如果不存在attribute三元组，创建三元组
            attr_id = self.get_model().model_is_exist_attr(attribute_name, unity_id, value)
            if not attr_id:
                attr_id = self.get_model().model_create_new_attr(attribute_name, unity_id, value)[0][0]
                print("新attr"+attribute_name+str(value)+"已创建")
            else:
                attr_id = attr_id[0][0]
            print("attribute_id="+str(attr_id))

            is_connected = self.get_model().model_is_connected_coating_and_attribute(coating_id, attr_id)
            if not is_connected:
                self.get_model().create_connexion_between_coating_and_attribute(coating_id, attr_id)
                print("新关系"+str(coating_id)+str(attr_id)+"已创建")

    def action_delete_coating_attribute(self, coating_name, coating_number, attribute_name, value, unity):
        pass


if __name__ == '__main__':
    unittest_db = database.PostgreDB(host='localhost', database='testdb', user='dbuser', pd=123456, port='5432')
    unittest_db.connect()
    print(Controller.tools_tuple_to_list([]))
