from fastapi import APIRouter, Query, Path
from book_api.models.health_response import HealthCheckResponse
from book_api.models.book_response import bookResObj
from book_api.models.book_request import newBookReview, bookReview
from book_api.services.book_service import bookService
from book_api.models.errors_models import genericerror


router = APIRouter()

@router.get("/health", response_model=HealthCheckResponse, status_code=200, include_in_schema=False)
async def health_check():
    """
    Health check endpoint to verify if the service is running.
    """
    return {"status": "healthy"}


@router.get("/search", response_model=bookResObj, responses={
        400: {"model": genericerror, "description": "Bad Request"},
        500: {"model": genericerror, "description": "Internal Server Error"},
    })
async def searchReview(keyword: str = Query(..., example='Keyword', description='Keyword to be searched in the review')):
    """
    API endpoint to retrieve retrieve a book review searching for keyword.
    """
    return await bookService.getReviewByKeyword(keyword)


@router.post("/review", response_model=bookResObj, responses={
        400: {"model": genericerror, "description": "Bad Request"},
        500: {"model": genericerror, "description": "Internal Server Error"},
    })
async def reviewBook(request: newBookReview):
    """
    API endpoint to create a new review.
    """
    return await bookService.createReview(request)


@router.get("/review/{bookId}", response_model=bookResObj, responses={
        400: {"model": genericerror, "description": "Bad Request"},
        500: {"model": genericerror, "description": "Internal Server Error"},
    })
async def searchReviewById(bookId: str = Path(..., example='BO343', description='Identification number of the book (UUID)')):
    """
    API endpoint to search a review using the ID.
    """
    return await bookService.getReviewById(bookId)


@router.put("/review/{bookId}", response_model=bookResObj, responses={
        400: {"model": genericerror, "description": "Bad Request"},
        500: {"model": genericerror, "description": "Internal Server Error"},
    })
async def updateReviewById(request: bookReview, bookId: str = Path(..., example='BO343', description='Identification number of the book (UUID)')):
    """
    API endpoint to modify a review by inserting ID.
    """
    return await bookService.updateReviewById(bookId, request)


@router.delete("/review/{bookId}", response_model=bookResObj, responses={
        400: {"model": genericerror, "description": "Bad Request"},
        500: {"model": genericerror, "description": "Internal Server Error"},
    })
async def deleteReviewById(bookId: str = Path(..., example='BO343', description='Identification number of the book (UUID)')):
    """
    API endpoint to delete a review.
    """
    return await bookService.deleteReviewById(bookId)
