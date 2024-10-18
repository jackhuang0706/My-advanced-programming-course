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
import os
from PIL import Image
import pytesseract #
import asyncio
import nest_asyncio # import nest_asyncio to allow nested event loops
import google.generativeai as genai
%env API_KEY=YOUR-API #替換成自己的API 
```

