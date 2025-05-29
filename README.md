# Bank API Assignment

## Endpoints

- `GET /banks/` - List all banks
- `GET /branches/?ifsc=XYZ` - Get branch by IFSC
- `GET /branches/?branch=XYZ` - Get branches by name

## Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Test

```bash
pytest
```

## Time Taken

~2.5 hours