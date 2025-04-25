from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pyback.db import get_db
from .model_loader import get_model

router = APIRouter(prefix="/api/document", tags=["Document"])

@router.get("/{doctype}/{doc_id}")
def get_doc(doctype: str, doc_id: int, db: Session = Depends(get_db)):
    model = get_model(doctype)
    document = db.query(model).filter(model.id == doc_id).first()
    if document:
        return document
    raise HTTPException(status_code=404, detail="Document not found")

@router.post("/{doctype}")
def create_doc(doctype: str, doc: dict, db: Session = Depends(get_db)):
    model = get_model(doctype)
    db_doc = model(**doc)
    db.add(db_doc)
    db.commit()
    db.refresh(db_doc)
    return db_doc