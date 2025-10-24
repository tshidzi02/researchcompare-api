import os
API_KEY = os.getenv("API_KEY", "set-a-strong-key")

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Read API key from environment if present
import os
API_KEY = os.getenv("API_KEY", "set-a-strong-key")

class Options(BaseModel):
    doHarvardAudit: bool = True
    doEquationCheck: bool = True
    returnAlignments: bool = True
    similarityMethod: str = "cosine-embeddings"
    paraphraseThreshold: float = 0.78

class CompareBody(BaseModel):
    sectionName: Optional[str] = None
    original: str
    humanized: str
    options: Options = Options()

@app.post("/compare")
def compare(body: CompareBody, x_api_key: str = Header(default="")):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    # Minimal dummy response so deploy works; we’ll improve later
    return {"score": 100, "subscores": {}, "alignments": [], "omissions": [], "introduced": [],
            "termsChanged": [], "equationCheck": {"status":"not_found","differences":[]},
            "harvardAudit": {"inTextPairs":[],"missingInReferences":[],"unmatchedInText":[],"formatIssues":[]}}
