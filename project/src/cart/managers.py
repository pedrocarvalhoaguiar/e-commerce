from safedelete.managers import SafeDeleteManager

class CartManager(SafeDeleteManager):

    def update_item(self, product, action):
        if action == 'add':
            product.quantity += 1
        elif action == 'remove':
            product.quantity -= 1
        product.save()
        