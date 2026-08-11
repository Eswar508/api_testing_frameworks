
def to_dict(self):
    return {
        "product_id": self.product_id,
        "name": self.name,
        "price": self.price,
        "stock": self.stock,
        "category_id": self.category_id,
        "status": self.status,
        "description": self.description
    }
    
def user_dict(self):
    return {
        "user_id":self.user_id,
        "name":self.name,
        "email":self.email,
        "role":self.role,
        "gender":self.gender
    }