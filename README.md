## Dataset / Document Corpus

This project uses a bounded subset of the official FastAPI Tutorial/User Guide as the document corpus.

The corpus consists of seven documentation topics:

1. [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)
2. [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)
3. [Request Body](https://fastapi.tiangolo.com/tutorial/body/)
4. [Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
5. [Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/)
6. [Security - First Steps](https://fastapi.tiangolo.com/tutorial/security/first-steps/)
7. [Testing](https://fastapi.tiangolo.com/tutorial/testing/)

Each page will initially be treated as one source document before applying the different chunking strategies.

To make the experiment reproducible, a fixed snapshot of the source documentation will be stored locally in the repository rather than relying on the live documentation during experiments.
