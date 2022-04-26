"""
DB Collection varibles for Stack Cart by Rahul Sarkar
"""

ROLES_COLLECTION = 'roles'
USERS_COLLECTION = 'users'
PRODUCT_COLLECTION = 'products'
ORDER_COLLECTION = 'orders'
ADDRESS_COLLECTION = 'address'
BRAND_COLLECTION = 'brands'
CART_COLLECTION = 'cart'
CATEGORY_COLLECTION = 'category'
CONTACT_COLLECTION = 'contacts'
MERCHANT_COLLECTION = 'marchants'
REVIEW_COLLECTION = 'review'
WISHLIST_COLLECTION = 'wishlist'

"""
Routes varibles for Stack Cart by Rahul Sarkar
"""

ADD_ROLES = "/api/v1/add_role"
GET_ROLES = "/api/v1/get_all_roles"

CREATE_MERCHANT = "/api/v1/add_merchant"
UPDATE_MERCHANT = "/api/v1/update_merchant/{_id}"
DELETE_MERCHANT = "/api/v1/delete_merchant/{_id}"

"""
Merchant status: 'Waiting Approval', 'Rejected', 'Approved'
"""

MERCHANT_STATUS = {
    "WA": "Waiting Approval",
    "R": "Rejected",
    "A": "Approved"
}
