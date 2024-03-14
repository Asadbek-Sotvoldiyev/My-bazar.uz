from myapp.models import Product
class Favorite:
    def __init__(self, request):
        self.session = request.session
        favorite = request.session.get('favorite')

        if 'favorite' not in request.session:
            favorite = self.session['favorite'] = {}
        self.favorite = favorite

    def add(self,product_id):
        product_id = str(product_id)
        if product_id not in self.favorite:
            self.favorite[product_id] = product_id

        self.session.modified = True

    def __len__(self):
        return len(self.favorite)

    def dell(self,product_id):
        product_id = str(product_id)
        if product_id in self.favorite:
            self.favorite.pop(product_id)

        self.session.modified = True

    def favorites(self):
        return self.favorite.keys()

    def get_favorites(self):
        product_ids = self.favorite.keys()
        products = Product.objects.filter(id__in=product_ids)
        return products
