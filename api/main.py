from typing import List, Dict
from fastapi import FastAPI, HTTPException, status
from contextlib import asynccontextmanager
from transformers import pipeline

from models import ReviewRequest, SentimentResponse


def predict_sentiment(text: str) -> List[Dict[str, float]]:
    """
    Predict sentiment of a given text
    
    Args:
    text (str): Text to predict sentiment
    
    Returns:
    List[Dict[str, float]]: Predicted sentiment
    """
    classifier = pipeline(model="aakinlalu/finetune-bert-sentiment-analysis")
    return classifier(text)


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    ml_models['predict_sentiment'] = predict_sentiment
    yield
    ml_models.clear()


app = FastAPI(lifespan=lifespan, docs_url="/api/v1/docs", redoc_url="/api/v1/redocs")


@app.post("/api/v1/sentiment", status_code=200)
async def get_sentiment(review: ReviewRequest) -> Dict:
    """
    API to predict sentiment of a given text
    
    Args:  
    text (str): Text to predict sentiment
    
    Returns:
    SentimentArrayResponse: Predicted sentiment
    """

    sentiment = None
    score = None
    try:
        text = review.review
        predictions = ml_models['predict_sentiment'](text)
        prediction = predictions[0]
        sentiment = prediction['label']
        score = round(prediction['score'], 2)
        return {
            "sentiment": sentiment,
            "score": score
        }
        
    except KeyError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Model not loaded")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    