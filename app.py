from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pathlib import Path
import random
import json

from content.toungetwisters import TWISTERS
from content.overarticulation import TEXT
from content.scenarios import SCENARIOS
from content.roleplay_scenarios import ROLEPLAY_SCENARIOS

TEXT_DIR = Path("content/texts")
TEXT2_DIR = Path("content/texts2")
SLIDES_DIR = Path("static/slides")
WORD_LIST = Path("content/word_list.json")

EXERCISES = [
    {"title": "Tongue Twisters", "url": "/toungetwisters"},
    {"title": "Reading and Over Articulation", "url": "/over-articulation"},
    {"title": "Read as a Character", "url": "/read-as-character"},
    {"title": "Roleplay Game", "url": "/roleplay-game"},
    {"title": "Presentation Karaoke", "url": "/presentation-karaoke"},
    {"title": "Random Words", "url": "/random-words"}
]

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"exercises": EXERCISES})

@app.get("/toungetwisters", response_class=HTMLResponse)
async def tounge_twisters(request: Request):
    return templates.TemplateResponse(request=request, name="tounge_twisters.html", context={"twisters": TWISTERS})

@app.get("/over-articulation", response_class=HTMLResponse)
async def over_articulation(request: Request):
    return templates.TemplateResponse(request=request, name="over_articulation.html", context={"books": TEXT})

@app.get("/over-articulation/{book_id}", response_class=HTMLResponse)
async def over_articulation(request: Request, book_id: str):
    book = next((b for b in TEXT if b["id"] == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail="Book id not found")

    file_path = TEXT_DIR / f"{book_id}.txt"
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Text file not found")
    
    text = file_path.read_text()
    paragraphs = text.split("\n\n")
    
    return templates.TemplateResponse(request=request, name="over_articulation_text.html", context={"book": book, "text": paragraphs})

@app.get("/read-as-character", response_class=HTMLResponse)
async def reading_acting(request: Request):
    scenario = random.choice(SCENARIOS)
    scenario = scenario["text"]

    text_path_list = [str(x) for x in TEXT2_DIR.iterdir() if x.is_file()]
    text_path = random.choice(text_path_list)
    text_path = Path(text_path)
    if not text_path.exists():
        raise HTTPException(status_code=404, detail="Text file not found")

    text = text_path.read_text()
    paragraphs = text.split("\n\n")

    return templates.TemplateResponse(request=request, name="read_character.html", context={"scenario": scenario, "text": paragraphs})

@app.get("/roleplay-game", response_class=HTMLResponse)
async def roleplay_game(request: Request):
    return templates.TemplateResponse(request=request, name="roleplay_game.html", context={"scenarios": ROLEPLAY_SCENARIOS})

@app.get("/presentation-karaoke", response_class=HTMLResponse)
async def presentation_karaoke(request: Request):
    slides_path_list = [str(x) for x in SLIDES_DIR.iterdir() if x.is_file()]
    slides = random.sample(slides_path_list, len(slides_path_list))

    return templates.TemplateResponse(request=request, name="presentation_karaoke.html", context={"slides": slides})

@app.get("/random-words", response_class=HTMLResponse)
async def random_words(request: Request):
    with open(WORD_LIST, 'r') as f:
        word_list = json.load(f)
    words = random.sample(word_list, 3)
    return templates.TemplateResponse(request=request, name="random_words.html", context={"words": words})

