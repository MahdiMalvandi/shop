from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from models.users import User
from schemas import products as schema
from models import products as model
from tools.authentication.token import get_current_user
from tools.crud import add_to_db

router = APIRouter()


# region all products
@router.get('/', response_model=list[schema.Product])
def get_all_products(db: Session = Depends(get_db)):
    all_products = db.query(model.Product).all()
    return all_products


# endregion

# region get a product


@router.get('/{slug}', response_model=schema.Product)
def get_product(slug: str, db: Session = Depends(get_db)):
    product = db.query(model.Product).filter(model.Product.slug == slug).first()
    if product is None:
        raise HTTPException(detail='Product not found', status_code=404)
    return product


# endregion

# region get products by category
@router.get('/category/{category_id}', response_model=schema.Product)
def get_product_by_category(category_id: str, db: Session = Depends(get_db)):
    category = db.query(model.Category).filter(model.Category.id == category_id).first()
    if category is None:
        raise HTTPException(detail='Category not found', status_code=404)

    products = db.query(model.Product).filter(model.Product.category_id == category_id)
    return products


# endregion

# region create a new product
@router.post('/', response_model=schema.Product)
def create_product(data: schema.ProductCreate, db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    if not current_user.is_seller:
        raise HTTPException(detail='You must be a seller', status_code=400)
    slug = data.title.replace('', '-')
    product = model.Product(
        title=data.title,
        price=data.price,
        discount=data.discount if 'discount' in data else None,
        slug=slug,
        count=data.count,
        seller_id=current_user.id,
        category_id=data.category_id
    )
    add_to_db(db, product)
    if 'product_colors' in data:
        for color in data['product_colors']:
            if db.query(model.Color).filter(color=color).first():
                color = db.query(model.Color).filter(color=color).first()
            else:
                color = model.Color(color=color)
                add_to_db(db, color)
            relation = model.ProductColor(product_slug=slug, color_id=color.id)
            add_to_db(db, relation)
    if 'product_attributes' in data:
        for attribute in data['product_attributes']:
            attribute_item = model.ProductAttribute(
                key=attribute.key,
                value=attribute.value,
                product_slug=slug
                )
            add_to_db(db, attribute_item)
    if 'product_images' in data:
        for image in data['product_images']:
            # add and upload images
            ...
    return product
# endregion
