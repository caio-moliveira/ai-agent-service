from pydantic import BaseModel, Field
from typing import Optional, List


class LeadPersonalInfo(BaseModel):
    name: str = Field(..., description=" The full name of the lead.")
    job_title: str = Field(..., description="The job title of the lead.")
    role_relevance: int = Field(
        ..., ge=0, le=10, description="A score representing how relevant the lead's is."
    )
    professional_background: Optional[str] = Field(
        ..., description=" A brief description of the lead's profession."
    )


class CompanyInfo(BaseModel):
    company_name: str = Field(..., description="The name of the company.")
    industry: str = Field(..., description="The industry in which the company is.")
    company_size: int = Field(..., description="The size of the company in employees.")
    revenue: Optional[float] = Field(None, description="The annual revenue.")
    market_presence: int = Field(
        ...,
        ge=0,
        le=10,
        description="A score representing the company's market presence.",
    )


class LeadScore(BaseModel):
    score: int = Field(
        ..., ge=0, le=100, description="The final score assigned to the lead (0-100)."
    )
    scoring_criteria: List[str] = Field(
        ..., description="The criteria used to determine the lead's score."
    )
    validation_notes: Optional[str] = Field(
        None, description="Any notes regarding to the validation of the lead score"
    )


class LeadScoringResult(BaseModel):
    personal_info: LeadPersonalInfo = Field(
        ..., description="Personal information about the lead."
    )
    company_info: CompanyInfo = Field(
        ..., description="Information about the lead's company."
    )
    lead_score: LeadScore = Field(
        ..., description="The calculated score and related information for the lead."
    )
