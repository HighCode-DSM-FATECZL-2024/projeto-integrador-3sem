from . import create_app
import uvicorn

app = create_app(
    "PI 3º Sem. | FATEC-ZL",
    "1.0.0"
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3030)