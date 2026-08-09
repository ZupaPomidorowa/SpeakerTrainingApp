# Speaker Training App

A web app with exercises to practise and improve public-speaking skills.

<img width="2327" height="1290" alt="image" src="https://github.com/user-attachments/assets/6e53fb30-ea15-4dc8-8cd8-be3033dfb879" />


## Exercises

- **Tongue Twisters** 
- **Reading & Over-Articulation** - pick text, read it aloud and over articulate every word.
- **Read as a Character** - read the provided text out loud exactly as the scenario describe.
- **Roleplay Game** - step into the given role and improvise a short speech or performance as that character in that situation.
- **Presentation Karaoke** - improvise a talk over random slides on a countdown timer.
- **Random Words** — get three random words and 30 seconds to give a speech.

<img width="2327" height="1379" alt="image" src="https://github.com/user-attachments/assets/12224c02-6ee2-4eef-a782-48e7d9e57510" />

<img width="2327" height="1379" alt="image" src="https://github.com/user-attachments/assets/f978e87f-9871-4eba-95e2-bd0e9c9e110d" />

## Tech stack

- **Backend:** FastAPI
- **Templates:** Jinja2
- **Styling:** Bootstrap 5 + custom CSS
- **Interactivity:** vanilla JavaScript (timers, slide advancing)
- **Container:** Docker

## How to run?

```bash
docker compose up
```

## Adding content

- **New text:** add a `.txt` file in `content/texts/`
- **New slides:** add a slide image to `content/slides/`.
- **New tongue twister / word:** edit the relevant list in `content/`

