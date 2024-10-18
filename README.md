# My-advanced-programming-course
## 安裝一些必要工具和套件
```python
!pip install -q -U google-generativeai
!pip install discord
!pip install nest_asyncio
!pip install pytesseract pillow discord
!apt-get install tesseract-ocr
!apt-get install tesseract-ocr-chi-sim tesseract-ocr-chi-tra  # 安裝中文語言包
```
## 匯入模組和文字識別引擎
```python
import discord
import os
from PIL import Image
import pytesseract
import asyncio
import nest_asyncio # import nest_asyncio to allow nested event loops
import google.generativeai as genai
%env API_KEY=AIzaSyAzMb2NwDnvMkZGQBF_GFBzUarkmdj_BVY
```

