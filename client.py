from common import *


class Client(Common, Database, Orders,  Catalog):

    def __init__(self):
        super().__init__()
        # self.user_is_valid = False
        self.id = 1
    #     self.name = ''
    #     self.email = ''
    #     self.password = ''    #     self.name = ''
    #     self.email = ''
    #     self.password = ''

    def compiler(self):
        """
        Компитятор для всех функций, заработает тогда когда пользователь вводит не корректные данные
        :return: redirect или full_temp
        """
        while self.i >= 1:
            self.i -= 1
            if self.num == '15':
                self.menu()
            self.redirect()
        if self.i == 0:
            self.full_temp()

    def full_temp(self):
        """
        заработает если пользователь вводит не корректные данные 3 раза
        :return: исхогдя от того в каком функции находится перенаправится пользователь
        """
        if self.num == '1':
            self.i = 2
            self.output(arg='first_stage_error')
            self.signin_or_login()
        elif self.num == '3' or self.num == '9' or self.num == '6' or self.num == '12' or self.num == '15'\
                or self.num == '18':
            self.menu()

    def redirect(self):
        """
        перенаправление порльзователей в определенные функции исходя выбора функции самого пользователя
        """
        if self.num == '1':
            self.login()
        elif self.num == '2':
            self.user_is_valid = False
            self.sign_in()
        elif self.num == '3':
            self.catalogs()
        elif self.num == '6' or self.num == '4':
            self.product()
        elif self.num == '9':
            self.orders()
        elif self.num == '12':
            self.edit_order()
        elif self.num == '15':
            self.view_orders()
        elif self.num == '18':
            self.pay_order()
        elif self.num == '99':
            self.catalogs()
        else:
            self.signin_or_login()

    def catalogs(self):
        """
        функция ничего не принимает, выводит фсе категорнии в консоль
        если они есть в файле catalogdb
        :return: None
        """
        self.i = 2
        self.catalog_db()
        if self.num == '99':
            if self.error:
                self.output(arg='products_db_error')
                self.signin_or_login()
            else:
                self.signin_or_login()
        elif self.error:
            self.user_is_valid = True
            self.error = False
            self.output(arg='products_db_error')
            self.menu()
        else:
            self.menu()

    def product(self):
        """
        функция получает 1 значение от пользователя для нахождени в категории
        :return:
        """
        try:
            catalog = str(input('Введите категорию\n 0- Выйти\n- '))
            if catalog == '0':
                if self.num == '4':
                    self.signin_or_login()
                    self.i = 2
                else:
                    self.i = 2
                    self.menu()
            self.product_db(category=catalog)
            if self.num == '4':
                if self.product_error:
                    self.product_error = False
                    self.output(arg='product_error')
                return self.signin_or_login()
            elif self.product_error:
                self.product_error = False
                self.output(arg='product_error')
                self.compiler()
            else:
                self.i = 2
                self.menu()
        except Exception:
            self.output(arg='log_in_error')
            self.product()

    def signin_or_login(self):
        """
        берет тоько 1 параметр для выбора входа тлт регистрации
        :return: self.redirect или compiler()
        """
        self.arg1 = 'user'
        self.output(arg='signin_or_login')  # вызов функции для принта
        try:
            self.num = int(input('- '))
            if self.num == 3:
                self.num = 99
            self.num = str(self.num)
            self.i = 2
            # self.num *= 1  # Умножение для определение в какую функцию надо отправить пользователя
            return self.redirect()
        except Exception:
            self.output(arg='signin_or_login_error')
            return self.signin_or_login()

    def admins(self, name_, username_, password_):
        """
        ф-я для входа в админскую часть, проверяет,
        если все даныые будут admin то откроется админ панель
        :param name_: получается от функции login()
        :param username_: получается от функции login()
        :param password_: получается от функции login()
        :return: админ панель
        """
        if name_ == 'admin' and username_ == 'admin' and password_ == 'admin':
            import owner
            self.i = 2
            self.output(arg='admin')
            owner.Admin().main()
        else:

            self.menu()

    def sign_in(self):
        """
        Функция для регистраци и добавлении в базу данных
        от пользователя берется его данные сохраняет в db
        :return: login()
        """
        self.output(arg='sign_in')
        try:
            name = str(input('1- '))
            if name == '0':
                self.signin_or_login()
            surname = str(input('2- '))
            email = input('3- ')
            username = input('4- ')
            password = input('5- ')
            self.registration(name=name, surname=surname, email=email, username=username, password=password)
            self.i = 2
            self.login()
        except Exception:
            self.output(arg='sign_in_error')
            self.compiler()

    def login(self):
        """
        ф-я для входа в акк и берет от пользователя 3 параметра
        для проверки
        :return: menu()
        """
        self.output(arg='login')
        try:
            username = input('1- ')
            if username == '0':
                self.signin_or_login()
            email = input('2- ')
            password = input('3- ')
            if username == 'admin' and email == 'admin' and password == 'admin':
                self.admins(name_=username, username_=username, password_=password)
            self.log_in(user=username, _email=email, _password=password)
            if self.user_is_valid:
                self.menu()
            if not self.user_is_valid:
                self.output(arg='login_not_is_valid')
                self.compiler()
        except Exception:
            self.output(arg='log_in_error')
            self.compiler()

    def menu(self):
        """
        ф-я для выбора функций, берет у пользователя 1 значение
        :return: redirect()
        """
        self.output(arg='menu')
        try:
            self.num = int(input('- '))
            if self.num == 0:
                self.user_is_valid = False
                self.signin_or_login()
            self.num *= 3
            self.num = str(self.num)
            self.redirect()
        except Exception:
            self.output(arg='log_in_error')
            self.menu()

    def orders(self):
        """
        функция для заказа, берет у пользователя 5 значений из них title_ и category
        для поиска в db этого продукта и для выврода суммы заказа
        :return:
        """
        global status_
        self.output(arg='orders')
        try:
            category = str(input('1- '))
            if category == '0':
                return self.menu()
            title_ = str(input('2- '))
            quantity_ = int(input('3- '))
            status = int(input('4- '))
            phone_ = int(input('5- '))
            if status == 1:
                status_ = 'Оплачен'
            elif status == 2:
                status_ = 'Создан'
            zakaz = input('Введите: 1- Подтвердить; 0- Отменить: ')
            if zakaz == '1':
                self.order(catalog=category, status=status_, phone=phone_, title=title_, id_=self.id,
                           quantity=quantity_, name=self.name, email__=self.email, password_=self.password)
                self.id += 1
                self.i = 2
                self.menu()
                if not self.check_quantity_:
                    self.output(arg='orders_error')
                    self.compiler()
                elif self.products_error:
                    self.output(arg='products_error')
                    self.compiler()
                elif self.check_quantity_error and not self.products_error:
                    self.compiler()
                    self.output(arg='check_quantity_error')
            elif zakaz == '2':
                self.id += 1
                self.i = 2
                self.order(catalog=category, status=status_, phone=phone_, title=title_, id_=self.id,
                           quantity=quantity_, name=self.name, email__=self.email, password_=self.password)
            elif zakaz == '0':
                self.menu()
        except Exception:
            if self.quantity_error == True:
                self.output(arg='quantity_error')
            else:
                self.output(arg='log_in_error')
            self.compiler()

    # def order_db(self):
    #     """
    #     ф-я для просмотра истории заказов, ниченго не берет от пользователя
    #     :return:
    #     """
    #     self.output_order(status='user', name_=self.name, email__=self.email, password_=self.password)
    #     self.i = 2
    #     if not self.output_error:
    #         self.output(arg='order_db_error')
    #     elif self.output_error:
    #         self.output_error = False

    def edit_order(self):
        """
        ф-я для изменения количества или удаление из корзины продуктов которых он
        заказл но не оплатил
        :return:
        """
        global new_quantity, title
        try:
            num_ = int(input('1- Для изменение количество продукта заказа\n'
                             '2- Для удаление заказа\n'
                             '0- Выйти\n- '))
            if 0 <= num_ <= 2:
                if num_ == 1:
                    title = input('Имя продукта: ')
                    new_quantity = int(input('количество продукта: '))
                elif num_ == 2:
                    title = input('Имя продукта: ')
                elif num_ == 0:
                    self.menu()
                self.rewriting(file='order', status='user', num=new_quantity, choice=num_, status_user=title,
                               user=self.name, email_=self.email, password_=self.password)
                self.i = 2
                self.menu()
            else:
                self.output(arg='signin_or_login_error')
                self.compiler()
        except Exception:
            self.output('log_in_error')
            self.compiler()

    def view_orders(self):
        """
        ф-я для просмотра истории заказов, ниченго не берет от пользователя
        :return:
        """
        self.output_order(status='user', name_=self.name, email__=self.email, password_=self.password)
        if not self.output_error_:
            self.output(arg='output_order')
            self.compiler()
        else:
            self.menu()

    def pay_order(self):
        """
        ф-я для оплаты продукта в котором он ранее добавил в корзину, для этого получает от пользователя
        2 параметра категорию и имя продукта, и исходя из этих данных ищет в db
        :return:
        """
        global title
        try:
            catalog = input('Категория продукта: ')
            if catalog == '0':
                return self.menu()
            title = input('имя продута: ')
            self.rewriting(file='order', status='user', num='', choice=3, status_user=title,
                           user=self.name, email_=self.email, password_=self.password)
            if self.quantity_error:
                self.output(arg='quantity_error')
            if self.check_quantity_:
                self.rewrit(file=catalog,
                        status='user', choice='Создан', num=title,
                        status_user=self.quantity,
                        user=3, email_='', password_='')
            if not self.view and not self.quantity_error:
                self.output(arg='no_pay')
                self.compiler()
            elif self.view and not self.check_quantity_:
                if self.check_quantity_:
                    self.output(arg='pay_error')
                    self.compiler()
            else:
                if not self.quantity_error:
                    self.output(arg='pay')
                    self.menu()
                else:
                    self.compiler()
        except Exception:
            self.output('log_in_error')
            self.compiler()


c = Client()
c.signin_or_login()

# self.rewrit(file=rewriting_dict['catalog'],
#             status='user', choice='Создан', num=rewriting_dict['title'],
#             status_user=rewriting_dict['quantity'],
#             user=3, email_='', password_='')