"""
1. Data Validation
2. Exception Handling
3. Status Codes
4. Swagger configurations
5. Request Objects
"""


"""
HTTP Request Methods: Comparision between CRUD and HTTP Request Methods
1. GET: To request data from the server. This is similar to the Read operation in CRUD.
2. POST: To submit data to the server. This is similar to the Create operation in CRUD.
3. PUT: To update data on the server. This is similar to the Update operation in CRUD.
4. DELETE: To delete data from the server. This is similar to the Delete operation in CRUD.
"""

from fastapi import FastAPI, Body, HTTPException
from typing import Optional, List