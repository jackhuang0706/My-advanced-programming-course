# My-advanced-programming-course
## 安裝一些必要工具和套件
```python
!pip install -q -U google-generativeai #使用Google的AI模型Gemini，要安裝&更新
!pip install discord #安裝Discord機器人的Python庫
!pip install nest_asyncio #允許事件循環的嵌套
!pip install pytesseract pillow discord #圖片轉文字及圖像處理
!apt-get install tesseract-ocr #圖像辨識引擎
!apt-get install tesseract-ocr-chi-sim tesseract-ocr-chi-tra  # 安裝中文語言包
```
## 匯入模組和文字識別引擎
```python
import discord #匯入discord機器人
import os #負責與作業系統互動
from PIL import Image #打開、處理圖像
import pytesseract #搭配Tesseract-OCR引擎來實現圖片轉文字
import asyncio # 管理事件循環模組
import nest_asyncio 
import google.generativeai as genai #匯入AI聊天
%env API_KEY=YOUR-API #替換成自己的API 
```

