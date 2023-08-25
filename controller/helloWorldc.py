from config import *
from service.helloworlds import *

@app.get('/{email}')
def getPhone(email: str):
    return helloo(email)