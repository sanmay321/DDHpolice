import app
import uvicorn

from config import *
from controller.helloWorldc import *


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
