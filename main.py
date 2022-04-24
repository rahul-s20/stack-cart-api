"""
Stack cart by Rahul Sarkar by stark and co.
"""

import uvicorn
from app import create_app

app = create_app()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.main()
