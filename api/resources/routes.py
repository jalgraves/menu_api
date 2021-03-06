from .food import FoodAPI, FoodItemsAPI, FoodItemsByCategoyryAPI
from .categories import CategoryAPI, CategoriesAPI


def init_routes(api):
    api.add_resource(FoodItemsAPI, '/v1/menu/items')
    api.add_resource(FoodItemsByCategoyryAPI, '/v1/menu/section/<category>')
    api.add_resource(FoodAPI, '/v1/menu/item')
    api.add_resource(CategoryAPI, '/v1/categories/<category>')
    api.add_resource(CategoriesAPI, '/v1/categories')
