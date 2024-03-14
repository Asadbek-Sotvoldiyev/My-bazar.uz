from myapp.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = request.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = str(quantity)
        else:
            self.cart[product_id] = str(int(self.cart[product_id]) + quantity)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)

    def get_products(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quantity(self):
        return self.cart

    def update(self, product, quantity):
        product_id = str(product)
        quantity = str(quantity)

        self.cart[product_id] = quantity

        self.session.modified = True
        return self.cart

    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
