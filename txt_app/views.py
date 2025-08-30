from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.conf import settings
from gtts import gTTS
from gtts.lang import tts_langs
from deep_translator import GoogleTranslator
import uuid 
from pathlib import Path
SUPPORTED_TTS = tts_langs()

def index(reuest):
    return render(request,"index.html",{"translate_first":True})

def convert_text(request):
    if request.mwthod !="POST":
        return HttpResponseBadRequest("Invalid request method")
    text=(request.POST.get("text")or "").strip()
    lang=(request.POST.get("lang")or "en").strip()
    translate_first=(request.POST.get(translate_first)=="on") 
    slow=(request.POST.get(slow)==("on"))

if not text:
   return render(request,"index.html",{"error":"Please enter some text.","translate_first":translate_first})
if lang not in SUPPORTED_TTS:
     return render(request,"index.html","error":f"Language {lang} not supported by gTTS.","Translate_first":translate_first})