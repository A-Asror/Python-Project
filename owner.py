from common import *


class Admin(Common, Database, Catalog, Orders):
    def main(self):
        """
        ф-я заработает тогда когда админ заходит в админвскую панель управления
        :return: menu()
        """
        self.arg1 = 'admin'
        self.id = 1
        self.id_product = 1
        self.menu()

    def redirect(self):
        """
        ф-я для перенаправления пользователя, перенаправит исходя от того, ккакую ф-ю выберит админ
        """
        if self.num == '1':
            self.catalogs()
        elif self.num == '2':
            self.product()
        elif self.num == '3':
            self.catalog_add()
        elif self.num == '4':
            self.product_add()
        elif self.num == '5':
            self.change_price()
        elif self.num == '6':
            self.view_orders()
        elif self.num == '7':
            self.edit_order()

    def menu(self):
        """
        ф-я для определение, какую ф-ю хочет испоьзовать админ, получает 1 значение от админа
        :return: redirect()
        """
        self.output(arg='menu')
        try:
            self.num = input('- ')
            if self.num == '0':
                import client
                self.output(arg='welcome')
                client.Client().signin_or_login()
            self.redirect()
        except Exception:
            self.output(arg='menu_error')
            # self.compiler()

    def catalogs(self):
        """
        ф-я для просмотра всех категориев в db, от пользователя ничего не берет
        :return: menu()
        """
        self.catalog_db()
        if self.error:
            self.error = False
            self.output(arg='products_db_error')
            self.menu()
        else:
            self.menu()
            # self.catalog_add()

    def catalog_add(self):
        """
        ф-я для добавления нового каталога в db, берет от пользователя 1 параметр для названия этой категории
        :return: menu()
        """
        try:
            new_catalog = str(input('Введите "0" чтобы выйти\nВведите имя новой категории: '))
            if new_catalog == '0':
                return self.menu()
            self.catalog_db_add(name=new_catalog, num=self.id)
            self.id += 1
            self.output(arg='products_db_add')
            self.menu()

        except Exception:
            self.output(arg='error')
            return self.redirect()

    def product_add(self):
        """
        ф-я для добавления нового продукта в db, и получит от пользователя 4 параметра один из них
        catalog - категория этого продукта, нужно ввести так как и в katalogdb иначе порльзователя
        не сможет найти этот каталог
        :return: menu()
        """
        self.output(arg='product_add')
        try:
            title_ = str(input('1- '))
            if title_ == '0':
                self.menu()
            catalog = str(input('2- '))
            price_ = int(input('3- '))
            quantity_ = int(input('4- '))
            self.products_db_add(title=title_, category=catalog, price=price_, quantity=quantity_)
            # self.id_product += 1
            #     self.output(arg='products_error')
            #     self.menu()
            self.output(arg='products_db_add')
            self.menu()
        except Exception:
            self.output(arg='error')
            self.product_add()

    def product(self):
        """
        ф-я для вывода протдуктов в конкретно одном категории
        от админа получается 1 параметр для поиска категориев,
        и выведит в консоль все продукты в этом катеории
        :return: menu()
        """
        try:
            catalog = str(input('Введите категорию- '))
            if catalog == '0':
                self.menu()
            self.product_db(category=catalog)
            # if self.error:
            if self.product_error:
                self.product_error = False
                self.output(arg='product_error')
                self.menu()
            else:
                self.menu()
        except Exception:
            self.output(arg='error')
            self.product()

    def change_price(self):
        """
        ф-я для изменение количества или цены продукта, для этого от польлзователя берется 2 параметра
        категория и имя продукта который хочет изменить админ
        :return: menu()
        """
        try:
            category = str(input('Категория продукта: '))
            title = input('Имя продукта: ')
            if category == '0':
                self.menu()
            choice_ = int(input('Введите: 1 для изменеия цены, Введите: 2 для изменение количество шт(кг): '))
            if choice_ == 1:
                num_ = int(input('новая цена: '))
            else:
                num_ = int(input('количество товаров: '))
            self.rewriting(file=category, status='admin', choice=choice_, num=num_,
                           status_user=title, user='', email_='', password_='')
            self.output(arg='change_price')
            self.menu()
        except Exception:
            self.output(arg='error')
            self.change_price()

    def view_orders(self):
        """
        ф-я для просмотра заказов
        :return: menu()
        """
        self.output_order(status='admin', name_='', email__='', password_='')
        if not self.output_error_:
            self.output(arg='output_order')
            self.menu()
        else:
            self.menu()

    def edit_order(self):
        """
        ф-я для изменение статуса пользователя, админ вводит
        имя пользователя,
        email
        пароль пользвателя
        по этим данным изменится статус у конкретнеого пользователя
        и статус на которы он хочет изменить
        :return: menu()
        """
        self.output(arg='edit_order')
        try:
            name = input('1- ')
            if name == '0':
                self.menu()
            email = input('2- ')
            password = input('3- ')
            status = input('4- ')
            self.rewriting(file='order', status='admin', choice='0', num='', status_user=status,
                           user=name, email_=email, password_=password)
            if not self.view:
                self.output(arg='edit_order_error')
                self.edit_order()
            else:
                self.menu()
        except Exception:
            self.output(arg='error')
            self.edit_order()

# b = Admin()
# b.main()