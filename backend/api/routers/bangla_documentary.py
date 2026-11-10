"""
Bangla Documentary API Endpoint (POST /v1/audio/bangla-documentary)
===================================================================
Automated API endpoint designed for external video generators (such as Remotion):
- Accepts raw or pre-formatted Bengali text.
- Normalizes script (digits, acronyms, typography).
- Synthesizes micro-chunks with optimal documentary settings.
- Stitches with cosine crossfades and sentence/paragraph pauses.
- Applies studio broadcast mastering filtergraph.
- Returns audio path/URL and exact word-level @remotion/captions timestamps.
"""

from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field

from api.dependencies import require_consumer_reads_admin_writes
from services.bangla_documentary_engine import generate_bangla_documentary

router = APIRouter(prefix="/v1/audio", tags=["Bangla Documentary"])


class BanglaDocumentaryRequest(BaseModel):
    input: str = Field(..., description="Bengali text/script to synthesize")
    voice: Optional[str] = Field("bangla-documentary-master", description="Voice profile ID")
    speed: Optional[float] = Field(0.94, ge=0.5, le=2.0, description="Narration speed (default: 0.94 for documentary)")
    num_step: Optional[int] = Field(40, ge=10, le=100, description="Diffusion steps (default: 40)")
    guidance_scale: Optional[float] = Field(2.2, ge=1.0, le=5.0, description="Classifier-free guidance scale (default: 2.2)")
    response_format: Optional[str] = Field("mp3", description="Audio format (mp3 or wav)")
    output_path: Optional[str] = Field(None, description="Optional custom destination file path")
    return_timestamps: Optional[bool] = Field(True, description="Whether to include @remotion/captions word timestamps")


class RemotionCaption(BaseModel):
    text: str
    startMs: int
    endMs: int
    timestampMs: int


class WordItem(BaseModel):
    word: str
    start: float
    end: float


class SegmentItem(BaseModel):
    id: int
    start: float
    end: float
    text: str
    words: List[WordItem] = []


class BanglaDocumentaryResponse(BaseModel):
    status: str
    file_path: str
    audio_url: str
    duration_seconds: float
    remotion_captions: List[RemotionCaption]
    segments: List[SegmentItem]
    render_time_seconds: float


@router.post("/bangla-documentary", response_model=BanglaDocumentaryResponse)
async def create_bangla_documentary_speech(req: BanglaDocumentaryRequest):
    """
    Generate broadcast studio-quality Bengali documentary narration with word-level Remotion captions.
    """
    if not req.input or not req.input.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")

    try:
        result = await generate_bangla_documentary(
            text=req.input,
            output_path=req.output_path,
            response_format=req.response_format,
            speed=req.speed,
            num_step=req.num_step,
            guidance_scale=req.guidance_scale,
            return_timestamps=req.return_timestamps
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Bangla documentary generation failed: {str(e)}")

