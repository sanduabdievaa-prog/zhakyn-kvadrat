# Жақын квадрат әдісін тексеру

Streamlit арқылы жасалған шағын қазақша веб-қосымша. `a` санын, жуық мәнді және дәлдікті енгізгенде, ең жақын толық квадратты табады, `√a ≈ (a+b)/(2√b)` формуласын есептейді және нәтижені нақты квадрат түбірмен салыстырады.

## Компьютерде іске қосу

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Интернетке орналастыру

Streamlit Community Cloud-та жариялау үшін GitHub репозиторийіне `app.py` және `requirements.txt` файлдарын жүктеңіз. `share.streamlit.io` сайтына GitHub арқылы кіріп, **Create app** батырмасын басыңыз; репозиторий мен `app.py` файлының жолын көрсетіп, Deploy басыңыз. Қолданба сәтті орналастырылғаннан кейін берілген `*.streamlit.app` сілтемесін телефоннан да, компьютерден де аша аласыз.

Ресми заавар: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy
