import os
from datetime import datetime

date = datetime.now()


class Common:

    def __init__(self):
        self.arg1 = ''
        self.all_words = {
            'user': {
                'product': 'В этой категории нет продуктов !!!',
                'signin_or_login': '1- Вход\n2- Регистрация\n3- Каталог\n4- Продукты',
                'login': 'Авторизация\n'
                         '1- Логин\n'
                         '2- Email\n'
                         '3- Пароль',
                'sign_in': '1- Имя\n'
                           '2- Фамилия\n'
                           '3- Email\n'
                           '4- Логин\n'
                           '5- Проль',
                'admin': '\nДобро пожаловать в админ панель\n\n',
                'sign_is_valid': 'Вы успешно зарегистрировались, пожалуйста теперь авторизуйтесь',
                'products_error': 'В этом категории нет продукта с таким именем\n',
                'login_not_is_valid': 'Такого пользователя не существует,\n'
                                      'пожалуеста убедитесть ваш (username, email и password) введет правильно',
                'quantity_error': '\nНе хватает продуктов\n\n',
                'signin_or_login_error': 'Вы ввели не существующие функции',
                'output_order': '\nУвас нет заказов\n\n',
                'log_in_error': '\nВы ввеле не корректные данные пожалуйста попробуйте еще раз\n\n',
                'sign_in_error': '1 и 2 Пункт заполнения должен содержать только буквы\n[A-Z; a-z; А-я; а-я]',
                'first_stage_error': 'Вы истратили все попытки, пожалуйста вернитесь позже',
                'products_db_error': '\nСожалению к данному времени нет не одной категории\n\n',
                'order_db_error': 'Нет заказов',
                'no_pay': '\nУ вас нет открытых заказов\n\n',
                'product_error': '\nТакая категория не существует\nПожалуйста убедитесь что есть такая категория'
                                 ' в каталоге\n\n',
                'menu': '1- Просмотр каталога товаров\n'
                        '2- Просмотр продуктов\n'
                        '3- Создание заказа\n'
                        '4- Редактировать заказ\n'
                        '5- Просмотр списка заказов\n'
                        '6- Оплатить заказов в корзине\n'
                        '0- Выйти',
                'orders': '1- Категория продукта которого вы хотите купить\n'
                          '2- Введите имя продукта\n'
                          '3- Количество продукта\n'
                          '4- Введите: 1 - для оплаты и заказа; 2- для добавления в корзинку\n'
                          '5- Номер телефона',
                'check_quantity_error': 'Пожалуйста введите имя продукта и категорию0 так как'
                                        ' они написаны в каталоге\n',
                'orders_error': 'Такой категории не существует, пожалуйста провепьте какие категории сществуют или'
                                ' пишите имя категории как и написано в каталоге',
                'pay_error': 'Не хватает продуктов, пожалуеста уменьшите количество заказов',
                'pay': '\nОплата прошло успешно\n\n'
            },
            'admin': {
                'welcome': '\nДобро пожаловать\n\n',
                'menu': '1- Просмотр каталогов\n'
                        '2- Просмотр продуктов\n'
                        '3- Добавление новой категории\n'
                        '4- Добавлени нового продукта\n'
                        '5- Изменение цены товара или количества товара\n'
                # '6- Изменеие количества товара\n'
                        '6- Просмотр заказов\n'
                        '7- Изменение статуса заказа\n'
                        '0- Выйти\n',
                'change_price': '\nИзменеие прошло успешно\n\n',
                'output_order': '\nЗаказов нет\n\n',
                'product_add': '1- Имя продукта\n'
                               '2- Категория продукта\n'
                               '3- Цена продукта\n'
                               '4- Количество продукта\n'
                               '0- Выход\nТак же совет - в категорию продукта пишите уже существующий'
                               ' в каталоге категорию иначе пользователь не сможет видеть этоу продукцию!!!',
                'edit_order': '1- Имя пользователя\n'
                              '2- Email пользователя\n'
                              '3- Пароль пользователя\n'
                              '4- Новый статус\n'
                              '0- Выйти\n',
                'product_add_valid': 'Добавления продукта прошло успешно',
                # 'catalog_add': 'Добавления нового каталога прошло успешно',
                'products_db_add': '\nДобавление категории прошло успешно',
                'products_error': '\nСожалению к данному времени нет не одной категории\n\n',
                'products_db_error': '\nКаталог пуст, пожалуеста сначало добавьте продукты\n\n',
                'product_error': '\nТакая категория не существует\nПожалуйста убедитесь что есть такая категория'
                                 ' в каталоге\n\n',
                'menu_error': '\nВы ввели не существующие функции\n\n',
                'edit_order_error': '\nНет пользователя с такими данными\n\n',
                'error': '\nВы ввеле не корректные данные пожалуйста попробуйте еще раз\n\n',

            },
        }

    def output(self, arg):
        # 0000000000000000
        """
        функция принимает только 1 значение при вызови,
        задача у этого функции принтануть с помомщью словаря
        """
        outputs = self.all_words[self.arg1][arg]
        return print(outputs)


class Database:
    def __init__(self):
        self.user_is_valid = False

    def registration(self, name, surname, email, username, password):
        """
        Функция для пользовательской части и задача этой функции добавить пользователей в db
        принимает 5 значений, и добавляется в userdb файл
        """
        # 0000000000000000
        users = {
            'name': name,
            'surname': surname,
            'username': username,
            'email': email,
            'password': password,
            'status': None
        }
        with open('userdb.txt', 'a+', encoding='utf-8') as user:
            for key, val in users.items():
                user.write('{}:{}\n'.format(key, val))
            user.write('{}:{}\n'.format('стоп', 'стоп'))

    def log_in(self, user, _email, _password):
        # 0000000000000000
        """
        Функция принимает 3 параметра, и ищет по этим данным в файле
        userdb, и проверит есть ли такой пользователь в базе данных
        и self.user_is_valid будет True,
        """
        # level1, level2 и level3 по умолчанию False и если имя пользователя
        # совпадает с именем в базе данных то
        # level1 перезапишется в True и такая же логика работает с _email и _password
        # level1 = False
        # level2 = False
        # level3 = False
        self.user_is_valid = False
        nev = {}
        with open('userdb.txt', encoding='utf-8') as login:
            for i in login.readlines():
                key, val = i.strip().split(':')
                nev[key] = val
                if key == 'стоп' and val == 'стоп':
                    if nev['username'] == user and nev['email'] == _email and nev['password'] == _password:
                        self.name = user
                        self.email = _email
                        self.password = _password
                        self.user_is_valid = True
                        return self.user_is_valid
                    #     Common().output(arg='login_not_is_valid')
                    #     level1 = True
                    # if nev['email'] == _email:
                    #     level2 = True
                    # if nev['password'] == _password:
                    #     level3 = True
                    # if level1 and level2 and level3:
                    #     self.user_is_valid = True
                    # else:
                    #     Common().output(arg='login_not_is_valid')


class Catalog:
    def __init__(self):
        self.user_is_valid = False

    def catalog_db(self):
        """
         Функция для пользовательской и админской части и задача этой функци
         вывести все категории(каталог), в консоль
        """
        catalog_dict = {}
        self.catalog = False
        try:
            with open('catalogdb.txt', encoding='utf-8') as catalog:
                for products in catalog.readlines():
                    self.error = False
                    key, val = products.strip().split(':')
                    catalog_dict[key] = val
                    if key == 'стоп' and val == 'стоп':
                        name = catalog_dict['name']
                        _id = catalog_dict['id']
                        print('\n', _id + '- ', name, '\n')
                if self.error:
                    self.error = True
        except Exception:
            self.error = True

    def product_db(self, category):
        """
        Функция для админской и пользовательской части, принимает 1 параметр
        и по этого параметра откроет файл и выведит все данные в консоль
        """
        file_name = str(category).lower()
        product = {}
        self.product_error = False
        try:
            with open(file_name + '.txt', encoding='utf-8') as catalog:
                self.product_bool = True
                for products in catalog.readlines():
                    key, val = products.strip().split(':')
                    product[key] = val
                    if key == 'стоп' and val == 'стоп':
                        title = product['title']
                        price = product['price']
                        quantity = product['quantity']
                        print('\nTitle: ' + title, '\nЦена: ' + price, '\nКоличество кг(шт): ' + quantity + '\n')
        except Exception:
            self.product_error = True

    def output_order(self, status, name_, email__, password_):
        """
         Функция для админской и пользовательской части, принимает 1 параметр
         status и по этого параметра определяет что вывести в консоль
        """
        i = 0
        order_dict = {}
        self.output_error_ = False
        with open('order.txt', encoding='utf-8') as orders:
            for oreder in orders.readlines():
                key, val = oreder.strip().split(':')
                order_dict[key] = val
                if key == 'стоп' and val == 'стоп':
                    if status == 'user':
                        title = order_dict['title']
                        price = order_dict['price']
                        quantity = order_dict['quantity']
                        sum_ = order_dict['sum']
                        date_ = order_dict['created_add_date']
                        order_status = order_dict['status']
                        name = order_dict['name']
                        email = order_dict['email']
                        password = order_dict['password']
                        if name == name_ and email == email__ and password == password_:
                            i += 1
                            print(i, '\n', '1- Имя продукта: ' + title + '\n',
                                  '2- Цена: ' + price + '\n',
                                  '3- Количество: ' + quantity + '\n',
                                  '4- Сумма: ' + sum_ + '\n',
                                  '5- Дата создания заказа: ' + date_ + '\n',
                                  'Статус: ' + order_status + '\n'
                                  )
                        self.output_error_ = True
                    elif status == 'admin':
                        id_ = order_dict['id']
                        status_ = order_dict['status']
                        catalog = order_dict['catalog']
                        title = order_dict['title']
                        price = order_dict['price']
                        date_ = order_dict['created_add_date']
                        quantity = order_dict['quantity']
                        sum_ = order_dict['sum']
                        name = order_dict['name']
                        email = order_dict['email']
                        password = order_dict['password']
                        self.output_error_ = True
                        print('№ ' + id_ + '\n', '1- Каталог: ' + catalog + '\n',
                              '2- Статус: ' + status_ + '\n',
                              '3- Имя продукта: ' + title + '\n',
                              '4- Цена: ' + price + '\n',
                              '5- Дата создания заказа: ' + date_ + '\n',
                              '6- Количество: ' + quantity + '\n',
                              '7- Сумма: ' + sum_ + '\n',
                              '8- Имя заказчика: ' + name + '\n',
                              '9- Email: ' + email + '\n',
                              '10- Пароль: ' + password + '\n',
                              )
            else:
                self.output_error = False


# def output_order(self, status):
#     """
#      Функция для админской и пользовательской части, принимает 1 параметр
#      status и по этого параметра определяет что вывести в консоль
#     """
#     i = 1
#     order_dict = {}
#     with open('order.txt', encoding='utf-8') as orders:
#         for oreder in orders.readlines():
#             key, val = oreder.strip().split(':')
#             order_dict[key] = val
#             if key == 'стоп' and val == 'стоп':
#                 if status == 'user':
#                     title = order_dict['title']
#                     price = order_dict['price']
#                     quantity = order_dict['quantity']
#                     sum_ = order_dict['sum']
#                     order_status = order_dict['status']
#                     print(i, '\n', '1- Имя продукта ' + title + '\n',
#                           '2- Цена ' + price + '\n',
#                           '3- Количество ' + quantity + '\n',
#                           '4- Сумма ' + sum_ + '\n',
#                           'Статус ' + order_status + '\n'
#                           )
#                     i += 1
#                 elif status == 'admin':
#                     id_ = order_dict['id']
#                     status_ = order_dict['status']
#                     catalog = order_dict['catalog']
#                     title = order_dict['title']
#                     price = order_dict['price']
#                     quantity = order_dict['quantity']
#                     sum_ = order_dict['sum']
#                     name = order_dict['name']
#                     email = order_dict['email']
#                     password = order_dict['password']
#                     print('№ ' + id_ + '\n', '1- Статус ' + status_ + '\n',
#                           '2- Каталог ' + catalog + '\n',
#                           '3- Имя продукта ' + title + '\n',
#                           '4- Статус ' + status_ + '\n',
#                           '5- Цена ' + price + '\n',
#                           '6- Количество ' + quantity + '\n',
#                           '7- Сумма ' + sum_ + '\n',
#                           '8- Имя заказчика ' + name + '\n',
#                           '9- Email ' + email + '\n',
#                           '10- Пароль ' + password + '\n',
#                           )

# for products in catalog.readlines():
#     key, val = products.strip().split(':')
#     product[key] = val
#     if key == 'стоп' and val == 'стоп':
#         id_ = product['id']
#         title = product['title']
#         price = product['price']
#         quantity = product['quantity']
#         print(id_, '\n', title, price, quantity)


class Orders:

    def __init__(self):
        self.check_quantity_ = False
        self.products_error = True
        self.check_quantity_error = False
        file_name = {
            'hello': 'hello'
        }
        with open('file.txt', 'a+', encoding='utf-8') as files:
            for key, val in file_name.items():
                files.write('{}:{}\n'.format(key, val))
            files.write('{}:{}\n'.format('стоп', 'стоп'))

        self.num_ = 1
        self._id = 1
        self.orders_id = 1

    def catalog_db_add(self, name, num):
        """
        Функци для админской части, задача функции добавить новый каталог(категория)
        в db каталогов
        """
        name_ = str(name).lower()
        catalog_add = {
            'name': name_,
            'id': num
        }
        with open('catalogdb.txt', 'a+', encoding='utf-8') as catalogs:
            for key, val in catalog_add.items():
                catalogs.write('{}:{}\n'.format(key, val))
            catalogs.write('{}:{}\n'.format('стоп', 'стоп'))

    def products_db_add(self, title, category, price, quantity):
        """
        Функция для админской части и задача этой функции добавления продуктов,
        и он берет следующие параметры title, category, price, quantity
        и добавится в указанный файл в db
        """
        product_db_add = {
            'title': title,
            'price': price,
            'quantity': quantity
        }
        file_name = str(category).lower()
        with open(file_name + '.txt', 'a+', encoding='utf-8') as user:
            for key, val in product_db_add.items():
                user.write('{}:{}\n'.format(key, val))
            user.write('{}:{}\n'.format('стоп', 'стоп'))

    def order(self, catalog, status, phone, title, id_, quantity, name, email__, password_):
        """
        Эта функция для админской и пользовательской части и задача фукции
        добавить в файл то что покупал пользовател, администратор может посмотреть смисок
        и изменить статус
        :param phone: int() параметр для пользовательской части
        :param catalog: str() параметр вводится пользователем, для того чтоб админ смог видеть в каком категории
         находится товар и для поиска в db количство товаров
        :param status: str() если пользователь оплачет покупку то стату будет 'Оплачен', если просто добавит,
         то по умолчанию будет 'Создан'
        :param title: str() имя продукта вводится пользователем
        # :param price: int() цена продукты передается по умолчанию
        :param quantity: int() кол-во продукта
        :param name: int() имя пользователя, передается по умолчанию
        :param email__: str() email пользователя, передается по умолчанию
        :param password_: input() password пользователя, передается по умолчанию
        :return: self.check_quantity_ если будет True то сохранится в виде Оплачен, иначе сохранится как Создан
        """
        self.check_quantity(category_=catalog, title_=title, quantity_=quantity)
        if status == 'Оплачен' and self.check_quantity_:
            sum_ = int(self.price) * int(quantity)
            orders = {
                'id': id_,
                'status': status,
                'catalog': catalog,
                'title': title,
                'price': self.price,
                'quantity': quantity,
                'phone': phone,
                'created_add_date': date.strftime('%x'),
                'sum': sum_,
                'name': name,
                'email': email__,
                'password': password_
            }
            with open('order.txt', 'a+', encoding='utf-8') as order:
                for key, val in orders.items():
                    order.write('{}:{}\n'.format(key, val))
                order.write('{}:{}\n'.format('стоп', 'стоп'))
                self.rewriting(file=catalog, status='user', choice=status, num=title, status_user=quantity,
                               user='', email_='', password_='')
        elif status == 'Создан' and self.check_quantity_:
            sum_ = int(self.price) * int(quantity)
            orders = {
                'id': id_,
                'status': status,
                'catalog': catalog,
                'title': title,
                'price': self.price,
                'quantity': quantity,
                'created_add_date': date.strftime('%x'),
                'sum': sum_,
                'name': name,
                'email': email__,
                'password': password_
            }
            with open('order.txt', 'a+', encoding='utf-8') as order:
                for key, val in orders.items():
                    order.write('{}:{}\n'.format(key, val))
                order.write('{}:{}\n'.format('стоп', 'стоп'))

            return self.check_quantity_

    def check_quantity(self, category_, title_, quantity_):
        """
        функция проверит наличие товаров, достаточно ли товары в db чтобы пользователь смог заказать
        :param category_: имя категории передается от пользователя
        :param title_: имя продукта передается от пользователя
        :param quantity_: количество товаров передается от пользователя
        :return: self.check_quantity_
        """
        self.check_quantity_ = False
        self.quantity_error = False
        file = str(category_).lower()
        catalog_dict = {}
        title_ = str(title_).lower()
        title = title_.replace(' ', '')
        try:
            with open(file + '.txt', encoding='utf-8') as quantity:
                for products in quantity.readlines():
                    key, val = products.strip().split(':')
                    catalog_dict[key] = val
                    if key == 'стоп' and val == 'стоп':
                        if str(catalog_dict['title']).lower() == title and \
                                int(catalog_dict['quantity']) >= int(quantity_):
                            self.price = int(catalog_dict['price'])
                            self.check_quantity_ = True
                            self.products_error = True
                            return self.check_quantity_
                        elif str(catalog_dict['title']).lower() == title and \
                                int(catalog_dict['quantity']) < int(quantity_):
                            self.quantity_error = True
                        elif str(catalog_dict['title']).lower() != title and not self.check_quantity_:
                            self.products_error = True
        except Exception:
            self.check_quantity_error = True

    # def order(self, catalog, status, title, price, quantity, name, email__, password_):
    #     """
    #     Эта функция для админской и пользовательской части и задача фукции
    #     добавить в файл то что покупал пользовател, администратор может посмотреть смисок
    #     и изменить статус
    #     :param catalog: str() параметр вводится пользователем, для того чтоб админ смог видеть в каком категории
    #      находится товар и для поиска в db количство товаров
    #     :param status: str() если пользователь оплачет покупку то стату будет 'Оплачен', если просто добавит,
    #      то по умолчанию будет 'Создан'
    #     :param title: str() имя продукта вводится пользователем
    #     :param price: int() цена продукты передается по умолчанию
    #     :param quantity: int() кол-во продукта
    #     :param name: int() имя пользователя, передается по умолчанию
    #     :param email__: str() email пользователя, передается по умолчанию
    #     :param password_: input() password пользователя, передается по умолчанию
    #     :return: self.check_quantity_ если будет True то сохранится в виде Оплачен, иначе сохранится как Создан
    #     """
    #     if status == 'Оплачен':
    #         self.check_quantity(category_=catalog, title_=title, quantity_=quantity)
    #         if self.check_quantity_:
    #             sum_ = int(price) * int(quantity)
    #             orders = {
    #                 'id': self.orders_id,
    #                 'status': status,
    #                 'catalog': catalog,
    #                 'title': title,
    #                 'price': price,
    #                 'quantity': quantity,
    #                 'sum': sum_,
    #                 'name': name,
    #                 'email': email__,
    #                 'password': password_
    #             }
    #             self.orders_id += 1
    #             with open('order.txt', 'a+', encoding='utf-8') as order:
    #                 for key, val in orders.items():
    #                     order.write('{}:{}\n'.format(key, val))
    #                 order.write('{}:{}\n'.format('стоп', 'стоп'))
    #     elif status == 'Создан':
    #         sum_ = int(price) * int(quantity)
    #         orders = {
    #             'id': self.orders_id,
    #             'status': status,
    #             'catalog': catalog,
    #             'title': title,
    #             'price': price,
    #             'quantity': quantity,
    #             'sum': sum_,
    #             'name': name,
    #             'email': email__,
    #             'password': password_
    #         }
    #         self.orders_id += 1
    #         with open('order.txt', 'a+', encoding='utf-8') as order:
    #             for key, val in orders.items():
    #                 order.write('{}:{}\n'.format(key, val))
    #             order.write('{}:{}\n'.format('стоп', 'стоп'))
    #
    #     return self.check_quantity_
    #
    # def check_quantity(self, category_, title_, quantity_):
    #     """
    #     функция проверит наличие товаров, достаточно ли товары в db чтобы пользователь смог заказать
    #     :param category_: имя категоии передается от пользователя
    #     :param title_: имя продукта передается от пользователя
    #     :param quantity_: количество товаров передается от пользователя
    #     :return: self.check_quantity_
    #     """
    #     file = str(category_).lower()
    #     catalog_dict = {}
    #     with open(file + '.txt', 'a+', encoding='utf-8') as quantity:
    #         for products in quantity.readlines():
    #             key, val = products.strip().split(':')
    #             catalog_dict[key] = val
    #             if key == 'стоп' and val == 'стоп':
    #                 if catalog_dict['title'] == title_:
    #                     if catalog_dict['quantity'] == quantity_:
    #                         self.check_quantity_ = True
    #                         return self.check_quantity_

    def rewriting(self, file, status, choice, num, status_user, user, email_, password_):
        """
        функция определит что хочет пользователь или изменить и запишет в переменный текстовый файл
        :param file: str() имя категории который вводит админ , если пользователь вводит, то этот файл будет введен по
         умолчанию
        :param status: str() статус это для обе части, параметр тоже вводится по умолчанию
        :param choice: int() выбор для админа и для пользователя пользователя сам а-н либо п-тель  введет, параметр
         для админской части измеинт цену или количество товара, а для пользователя для изменеия кол-во товара или
         удаление заказа
        :param num: int() параметр для пользовательской и админской части, админ вводит для изменения в количестве
         товара или цену товара, пользователь может изменить только количество заказа
        :param status_user: параметр для админа, этот параметр изменит статус заказа, для пользователя по умочанию
         вводится: ''
        :param user: str() прарметр для п-ой и а-ой части, админ вводит конкретные имена пользователя чтобы измеить
         статус, пользователью это передается по умолчанию
        :param email_: str()прарметр для п-ой и а-ой части, админ вводит конкретные email пользователя чтобы измеить
         статус, ользователью это передается по умолчанию
        :param password_: str()прарметр для п-ой и а-ой части, админ вводит пароль имена пользователя чтобы измеить
         статус, ользователью это передается по умолчанию
        :return: функция для перезаписи
        """
        rewriting_dict = {}
        file_name = str(file).lower()
        self.view = False
        file_names = open('file.txt', 'a+', encoding='utf-8')
        with open(file_name + '.txt', encoding='utf-8') as product:
            for rewritings in product.readlines():
                key, val = rewritings.strip().split(':')
                rewriting_dict[key] = val
                if key == 'стоп' and val == 'стоп':
                    if status == 'admin':
                        if choice == 1 and str(rewriting_dict['title']).lower() == str(status_user).lower():
                            rewriting_dict['price'] = num
                        elif choice == 2 and str(rewriting_dict['title']).lower() == str(status_user).lower():
                            rewriting_dict['quantity'] = num
                        elif choice == '0' and status_user != '':
                            if str(rewriting_dict['name']).lower() == str(user).lower() and \
                                    str(rewriting_dict['email']).lower() == str(email_).lower() and \
                                    str(rewriting_dict['password']).lower() == str(password_).lower() and \
                                    str(rewriting_dict['status']).lower() == 'оплачен' or \
                                    str(rewriting_dict['status']).lower() == 'отправлен':
                                rewriting_dict['status'] = status_user
                                self.view = True
                                # СЮДА ПИШЕТСЯ ТО ЧТО ЕСЛИ ПОЛЬЗОВАТЕЛЬ НЕ СМОЖЕТ ПОЛЬЗОВАТЕль ЗАЙТИ В АКК
                    elif status == 'user':
                        if str(rewriting_dict['title']).lower() == str(num).lower() and choice == 'Оплачен':
                            new_quantity = int(rewriting_dict['quantity'])
                            (rewriting_dict['quantity']) = new_quantity - int(status_user)
                        # elif str(rewriting_dict['title']).lower() == str(num).lower() and \
                        #          choice == 'Создан' and \
                        #          int(user) == 3:
                        #     new_quantity = int(rewriting_dict['quantity'])
                        #     (rewriting_dict['quantity']) = new_quantity - int(status_user)
                        elif str(rewriting_dict['name']).lower() == str(user).lower() and \
                                str(rewriting_dict['email']).lower() == str(email_).lower() and \
                                str(rewriting_dict['password']).lower() == str(password_).lower() and \
                                rewriting_dict['title'] == status_user:
                            if int(choice) == 1 and rewriting_dict['status'] == 'Создан':
                                rewriting_dict['quantity'] = num
                            elif int(choice) == 2 and rewriting_dict['status'] == 'Создан':
                                rewriting_dict['status'] = 'заказ отменен'
                            elif int(choice) == 3 and rewriting_dict['status'] == 'Создан':
                                self.check_quantity(category_=rewriting_dict['catalog'],
                                                    title_=rewriting_dict['title'],
                                                    quantity_=rewriting_dict['quantity'])
                                self.quantity = rewriting_dict['quantity']
                                # self.rewrit(file=rewriting_dict['catalog'],
                                #                status='user', choice='Создан', num=rewriting_dict['title'],
                                #                status_user=rewriting_dict['quantity'],
                                #                user=3, email_='', password_='')
                                if self.check_quantity_:
                                    sum_ = int(self.price) * int(rewriting_dict['quantity'])
                                    rewriting_dict['sum'] = sum_
                                    rewriting_dict['status'] = 'Оплачен'
                                    self.view = True
                    for key, val in rewriting_dict.items():
                        file_names.write('{}:{}\n'.format(key, val))
        file_names.close()
        os.remove(file_name + '.txt')
        self.rewritings(file_name_1=file)

    def rewritings(self, file_name_1):
        """
        функция для перезаписи в обычный текстовый файл который удалился ранее и откроется новый файл со старым именем
        и запишется новые данные, затем удалится переменный файл
        :param file_name_1: этот параметр получается по умолчанию
        :return: None
        """
        file = str(file_name_1).lower()
        rewriting_dict_1 = {}
        filess = open('file.txt', encoding='utf-8')
        with open(file + '.txt', 'a+', encoding='utf-8') as files:
            for rewritings in filess.readlines():
                key, val = rewritings.strip().split(':')
                rewriting_dict_1[key] = val
                if key == 'стоп' and val == 'стоп':
                    for key, val in rewriting_dict_1.items():
                        files.write('{}:{}\n'.format(key, val))

        filess.close()
        os.remove('file.txt')

    def rewrit(self, file, status, choice, num, status_user, user, email_, password_):
        rewriting_dict = {}
        file_name = str(file).lower()
        file_names = open('file.txt', 'a+', encoding='utf-8')
        with open(file_name + '.txt', encoding='utf-8') as product:
            for rewritings in product.readlines():
                key, val = rewritings.strip().split(':')
                rewriting_dict[key] = val
                if key == 'стоп' and val == 'стоп':
                    if status == 'user':
                        if str(rewriting_dict['title']).lower() == str(num).lower() and \
                                choice == 'Создан' and \
                                int(user) == 3:
                            new_quantity = int(rewriting_dict['quantity'])
                            (rewriting_dict['quantity']) = new_quantity - int(status_user)
                        for key, val in rewriting_dict.items():
                            file_names.write('{}:{}\n'.format(key, val))
        file_names.close()
        os.remove(file_name + '.txt')
        self.rewritis(file_name_1=file)

    def rewritis(self, file_name_1):
        """
        функция для перезаписи в обычный текстовый файл который удалился ранее и откроется новый файл со старым именем
        и запишется новые данные, затем удалится переменный файл
        :param file_name_1: этот параметр получается по умолчанию
        :return: None
        """
        file = str(file_name_1).lower()
        rewriting_dict_1 = {}
        filess = open('file.txt', encoding='utf-8')
        with open(file + '.txt', 'a+', encoding='utf-8') as files:
            for rewritings in filess.readlines():
                key, val = rewritings.strip().split(':')
                rewriting_dict_1[key] = val
                if key == 'стоп' and val == 'стоп':
                    for key, val in rewriting_dict_1.items():
                        files.write('{}:{}\n'.format(key, val))
        filess.close()
        os.remove('file.txt')
