from pydantic import BaseModel, Field

class genericerror(BaseModel):
    error_code: int = Field(..., description='Status code')
    error_message: str = Field('', description='Reported issue description', example='JavaException detected')
    details: str = Field('',  description='User friendly description', example='An error occurred while processing your request due to a Java exception.')

