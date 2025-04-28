
-Bu repo yerel llm olan Ollama’yı kullanarak Python kodu üretiyor

-Homebre,Ollama,ve Python programları kurulu olmalı
(Nasıl kurulacağı bilinmiyorsa Notlarım kısmında açıklaması var)

“bash/ ollama serve” komutu kullanılarak ollama aktif edilmeli

-ardından farklı bir terminal açıp “bash/ ollama run mistral” mistral indirilip çalıştırılmalı(Ollamanın arka planda çalışmasını istiyoruz)

 bash/ cd Myproject.py
-bash/ pip install -r requirements.txt
gerekli kütüphaneler yüklenmeli

python3 app.py
-Flask kütüphanesi çalıştırılmalı

http://localhost:5055
-sunucu bu adreste çalışacak eğer bu adresiniz dolu ise 
lsof -i :5055 ve kill -9 PID (PID : process ıd ) ile port temizlenmeli veya başka bir port kullanılmalı 

-Flask kütüphanesi çalıştırıldıktan sonra http://localhost:5055 adresine tarayıcı üzerinden giderek Python kodu üreten arayüze ulaşabilirsiniz


Olası problemler 
-Port adresi dolu hatası: eğer adresiniz dolu ise 
lsof -i :5055 ve kill -9 PID (PID : process ıd ) ile port temizlenmeli veya başka bir port kullanılmalı 

-Ollama API’ye bağlanamıyorsa: Ollama arka planda çalışıyor mu kontorl edilmeli +yeni bir terminal aç ve bash/ ollama serve

-request modulü bulunamadı : pip3 install request 

!!! eğer pip3 python3 gibi bash kodları sizde çalışmıyorsa pip,python gibi kodlar deneyebilirsiniz bu proje mac üzerinden yazılmıştır 

———————————————————————————————————————————————————————————————————
This repo generates Python code using a local LLM called Ollama

-Homebrew, Ollama, and Python programs must be installed (If you don't know how to install them, there is an explanation in the Notes section)

“bash/ ollama serve” command must be used to activate ollama

-then open a different terminal and “bash/ ollama run mistral”
mistral should be downloaded and run (we want ollama to run in the background)

bash/ cd Myproject.py -bash/ pip install -r requirements.txt necessary libraries must be installed

python3 app.py -Flask library must be started http://localhost:5055
 -the server will run at this address. If your address is already occupied, you should clean the port with lsof -i :5055 and kill -9 PID (PID: process id) or use a different port

-After running the Flask library, you can reach the Python code generator interface by going to http://localhost:5055 through your browser

Possible problems: -Port address occupied error: if your address is occupied, it should be cleaned with lsof -i :5055 and kill -9 PID (PID: process id) or a different port should be used
-Cannot connect to Ollama API: Check if ollama is running in the background + open a new terminal and bash/ ollama serve
-request module not found: pip3 install requests

!!! if bash codes like pip3, python3 do not work for you, you can try codes like pip, python instead this project was written on mac