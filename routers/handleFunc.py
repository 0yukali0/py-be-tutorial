from fastapi import APIRouter, Depends
from manager.bookManager import BookManager, book_manager_instance


router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Hello World"}

def get_book_manager():
    return book_manager_instance

@router.get("/books")
async def get_books(book_manager: BookManager = Depends(get_book_manager)):
    return book_manager.get_books()