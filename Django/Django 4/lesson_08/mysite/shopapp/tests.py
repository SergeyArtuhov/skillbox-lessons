from django.test import TestCase
from .utils import two_numbers
from django.urls import reverse
from string import ascii_letters
from random import choices
from .models import Product
from django.contrib.auth.models import User
from django.conf import settings


class TwoNumbersTestCase(TestCase):
    def test_two_numbers(self):
        result = two_numbers(2, 3)
        self.assertEqual(result, 5)


class ProductCreateViewTestCase(TestCase):
    def setUp(self):
        self.product_name = "".join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()

    def test_create_product(self):
        response = self.client.post(
            reverse("shopapp:product_create"),
            {
                "name": self.product_name,
                "price": "123.45",
                "description": "A good table",
                "discount": "5"
            },
            HTTP_USER_AGENT="Mozilla/5.0"
        )
        self.assertRedirects(response, reverse("shopapp:products_list"))
        self.assertTrue(
            Product.objects.filter(name=self.product_name).exists()
        )


class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = Product.objects.create(name="".join(choices(ascii_letters, k=10)))

    # def setUp(self):
    #     self.product = Product.objects.create(name="".join(choices(ascii_letters, k=10)))

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()

    # def tearDown(self):
    #     self.product.delete()

    def test_get_product(self):
        response = self.client.get(
            reverse("shopapp:product_details", kwargs={"pk": self.product.pk}),
            HTTP_USER_AGENT="Mozilla/5.0"
        )
        self.assertEqual(response.status_code, 200)

    def test_get_product_and_check_content(self):
        response = self.client.get(
            reverse("shopapp:product_details", kwargs={"pk": self.product.pk}),
            HTTP_USER_AGENT="Mozilla/5.0"
        )
        self.assertContains(response, self.product.name)


class ProductsListViewTestCase(TestCase):
    fixtures = [
        "products-fixture.json",
    ]

    def test_products(self):
        response = self.client.get(reverse("shopapp:products_list"),
                                   HTTP_USER_AGENT="Mozilla/5.0")
        products = Product.objects.filter(archived=False).all()
        products_ = response.context["products_list"]
        self.assertQuerySetEqual(
            qs=Product.objects.filter(archived=False).all(),
            values=[p.pk for p in products_],
            transform=lambda p: p.pk,
        )
        self.assertTemplateUsed(response, "shopapp/products_list.html")
        # for p, p_ in zip(products, products_):
        #     self.assertEqual(p.pk, p_.pk)
        # for product in Product.objects.filter(archived=False).all():
        #     self.assertContains(response, product.name)


class OrdersListViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        # 1 cls.credentials = dict(username="bob_test", password="qwerty")
        # 1 cls.user = User.objects.create_user(**cls.credentials)
        cls.user = User.objects.create_user(username="bob_test", password="qwerty")

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self):
        # 1 self.client.login(**self.credentials)
        self.client.force_login(self.user)

    def test_orders_view(self):
        response = self.client.get(
            reverse("shopapp:orders_list"),
            HTTP_USER_AGENT="Mozills/5.0"
        )
        self.assertContains(response, "Orders")

    def test_orders_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(
            reverse("shopapp:orders_list"),
            HTTP_USER_AGENT="Mozills/5.0"
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)
        # self.assertRedirects(response, str(settings.LOGIN_URL))  Так не работает так как есть ?next=


class ProductsExportViewTestCase(TestCase):
    fixtures = [
        "products-fixture.json",
    ]

    def test_get_products_view(self):
        response = self.client.get(
            reverse("shopapp:products-export"),
            HTTP_USER_AGENT="Mozilla/5.0"
        )
        self.assertEqual(response.status_code, 200)
        products = Product.objects.order_by("pk").all()
        expected_data = [
            {
                "pk": product.pk,
                "name": product.name,
                "price": str(product.price),
                "archived": product.archived,
            }
            for product in products
        ]
        products_data = response.json()
        self.assertEqual(
            products_data["products"],
            expected_data,
        )