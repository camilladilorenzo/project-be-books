import logging
from book_api.models.book_request import newBookReview, bookReview
from book_api.models.book_response import bookResObj
from book_api.utils.helpers import get_process_id, create_connection
from fastapi import HTTPException


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class bookService:

    @classmethod
    async def getReviewByKeyword(cls, keyword: str):
        try:
            conn = create_connection()
            cursor = conn.cursor()          
            query = "SELECT * FROM reviews WHERE review LIKE %s"
            logger.info(f"Executing query: {query} with keyword: {keyword}")
            cursor.execute(query, (f"%{keyword}%",))           
            results = cursor.fetchall()
            content = {
                "reviews": [dict(zip([desc[0] for desc in cursor.description], row)) for row in results]
            }
            if results:
                return bookResObj(message='success', status_code=200, pid=get_process_id(), content=content)
            else:
                logger.warning(f"No reviews found for keyword: {keyword}")
                raise HTTPException(status_code=404, detail=f"{keyword} not found")   
        except Exception as e:
            logger.error(f"Error retrieving reviews by keyword: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error during the retrieval of reviews: {str(e)}")
        finally:
            conn.close()


    @classmethod
    async def createReview(cls, request: newBookReview):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            request_dict = request.dict()
            query = "INSERT INTO reviews (id, review, score) VALUES (%s, %s, %s)"
            logger.info(f"Executing query: {query} with values: {request_dict}")
            cursor.execute(query, (request_dict.get('bookId', ''), request_dict.get('review', ''), request_dict.get('score', 0)))
            conn.commit()
            return bookResObj(message='success', status_code=200, pid=get_process_id(), content={})
        except Exception as e:
            logger.error(f"Error during the insertion of the review: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error during the insertion of the request: {str(e)}")
        finally:
            conn.close()


    @classmethod
    async def getReviewById(cls, bookId: str):
        try:
            conn = create_connection()
            cursor = conn.cursor()          
            query = "SELECT * FROM reviews WHERE id = %s"
            logger.info(f"Executing query: {query} with bookId: {bookId}")
            cursor.execute(query, (bookId,))           
            results = cursor.fetchall()
            content = {
                "reviews": [dict(zip([desc[0] for desc in cursor.description], row)) for row in results]
            }
            if results:
                return bookResObj(message='success', status_code=200, pid=get_process_id(), content=content)
            else:
                logger.warning(f"No review found for bookId: {bookId}")
                raise HTTPException(status_code=404, detail=f"{bookId} not found")   
        except Exception as e:
            logger.error(f"Error retrieving review by ID: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error during the retrieval of the review: {str(e)}")
        finally:
            conn.close()


    @classmethod
    async def updateReviewById(cls, bookId: str, request: bookReview):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            request_dict = request.dict()
            set_condition = []
            for k, v in request_dict.items():
                if v is not None:  
                    if isinstance(v, (int, float)):
                        set_condition.append(f"{k} = {v}")
                    else:
                        set_condition.append(f"{k} = '{v}'") 
            if not set_condition:
                logger.warning("No fields provided for update.")
                raise HTTPException(status_code=400, detail="Nessun campo da aggiornare fornito.")
            query = f"UPDATE reviews SET {', '.join(set_condition)} WHERE id = %s"
            logger.info(f"Executing query: {query} with bookId: {bookId}")

            cursor.execute(query, [bookId])
            conn.commit()
            conn.close()
            return bookResObj(message='success', status_code=200, pid=get_process_id(), content={})   
        except Exception as e:
            logger.error(f"Error during the update of the review: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error during the update of the request: {str(e)}")
        finally:
            conn.close()


    @classmethod
    async def deleteReviewById(cls, bookId: str):
        try:
            conn = create_connection() 
            cursor = conn.cursor()
            query = "DELETE FROM reviews WHERE id = %s"
            logger.info(f"Executing query: {query} with bookId: {bookId}")

            cursor.execute(query, (bookId,))
            conn.commit()

            if cursor.rowcount == 0:
                logger.warning(f"No review found to delete for bookId: {bookId}")
                raise HTTPException(status_code=404, detail="Review not found.")
            
            return bookResObj(message='success', status_code=200, pid=get_process_id(), content={})
        
        except Exception as e:
            logger.error(f"Error during the deletion of the review: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error during the deletion of the review: {str(e)}")
        finally:
            conn.close()


if __name__ == "__main__":
    cls = bookService()
