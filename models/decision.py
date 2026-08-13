from pydantic import BaseModel, Field
from typing import List


class DecisionResult(BaseModel):
    decision: str = Field(
        description="HIGH_POTENTIAL, MEDIUM_POTENTIAL, or LOW_POTENTIAL"
    )

    confidence: int = Field(
        ge=0,
        le=100,
        description="Confidence score from 0 to 100"
    )

    best_opportunity: str

    reasons: List[str]

    risks: List[str]

    evidence: List[str]

    assumptions: List[str]

    missing_information: List[str]