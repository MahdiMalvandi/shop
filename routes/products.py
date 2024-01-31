from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from schemas import products as schema
from models import products as model

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
    post = db.query(model.Product).filter(model.Product.slug == slug).first()
    if post is None:
        raise HTTPException(detail='Product not found', status_code=404)
    return post

# endregion

# region get products by category
# endregion

# region create a new product
# endregion
