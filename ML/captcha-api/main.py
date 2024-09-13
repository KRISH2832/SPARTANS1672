from uvicorn import run

if __name__ == "__main__":
    run("app:app", host="localhost", port=6969, reload=True)