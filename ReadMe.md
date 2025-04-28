Project: AI-Powered Code Generator (!!! türkçesi alttadır)

-This repo uses a local LLM (Ollama) to generate Python code.

-Homebrew, Ollama, and Python must be installed.
(If you don't know how to install them, check the "Notes" section.)

-Activate Ollama using:

bash/ ollama serve

-Then open another terminal and run:

bash/ ollama run mistral
(to run the open-source LLM model Mistral. We want Ollama to keep running in the background.)

bash/ cd Myproject.py

bash/ pip install -r requirements.txt
(install necessary Python packages)

python3 app.py
(Run the Flask application)

http://localhost:5055
-The server will be running at this address.
If this port is already in use, you can clean it with:

lsof -i :5055 and kill -9 PID

-Or use a different port.

-After Flask is running, visit http://localhost:5055 from your browser to access the Python code generator interface.

Run on Minikube

-Install Minikube (brew install minikube)

-Start Minikube:

bash/ minikube start

-Set Docker environment to Minikube:

bash/ eval $(minikube docker-env)

-Build your Docker image:

bash/ docker build -t my-flask-app .

-Prepare and apply Deployment and Service YAML files
(e.g., codemaker-deployment.yaml and codemaker-service.yaml)

bash/ kubectl apply -f codemaker-deployment.yaml
bash/ kubectl apply -f codemaker-service.yaml

-Access the service via:

bash/ minikube service ai-codemaker-service

-The application interface should open, allowing you to generate Python code.

Possible Issues

-Port already in use:
Use lsof -i :5055 and kill -9 PID to free the port, or switch to a different port.

-Cannot connect to Ollama API:
Ensure that Ollama is running in a separate terminal with bash/ ollama serve.

-Minicube pod not running:
Make sure imagePullPolicy: Never is set in your deployment yaml, and docker image is built inside Minikube's docker-env.

-Requests module not found:
bash/ pip3 install requests

!!! If pip3 or python3 commands don't work on your system, try pip and python instead.
This project was developed on MacOS.
-----------------------------------------------------------------------------------------------------------------

Yapay Zeka Destekli Kod Üretici

-Bu repo yerel llm olan Ollama’yı kullanarak Python kodu üretiyor

-Homebrew, Ollama ve Python programları kurulu olmalı
(Nasıl kurulacağı bilinmiyorsa Notlarım kısmında açıklaması var)

“bash/ ollama serve” komutu kullanılarak ollama aktif edilmeli

-ardından farklı bir terminal açıp “bash/ ollama run mistral” mistral indirilip çalıştırılmalı
(Ollamanın arka planda çalışmasını istiyoruz)

bash/ cd Myproject.py

bash/ pip install -r requirements.txt
gerekli kütüphaneler yüklenmeli

python3 app.py
-Flask kütüphanesi çalıştırılmalı

http://localhost:5055
-sunucu bu adreste çalışacak eğer bu adresiniz dolu ise
lsof -i :5055 ve kill -9 PID (PID : process ıd ) ile port temizlenmeli veya başka bir port kullanılmalı

-Flask kütüphanesi çalıştırıldıktan sonra http://localhost:5055 adresine tarayıcı üzerinden giderek Python kodu üreten arayüze ulaşabilirsiniz

Minikube Üzerinde Çalıştırmak

-Minikube kurulumu yapılmalı (brew install minikube)

-Minikube başlatılmalı:

bash/ minikube start

-Minikube docker ortamı aktif edilmeli:

bash/ eval $(minikube docker-env)

-Docker image oluşturulmalı:

bash/ docker build -t my-flask-app .

-Deployment ve Service YAML dosyaları hazırlanmalı
(codemaker-deployment.yaml ve codemaker-service.yaml gibi)

-YAML dosyaları apply edilerek deployment ve service oluşturulmalı:

bash/ kubectl apply -f codemaker-deployment.yaml
bash/ kubectl apply -f codemaker-service.yaml

-Servisi tarayıcıdan açmak için:

bash/ minikube service ai-codemaker-service

-Uygulama açıldığında Python kod üreten arayüz çalışacaktır.

Olası Problemler

-Port adresi dolu hatası:
lsof -i :5055 ve kill -9 PID komutları ile port temizlenmeli veya başka bir port kullanılmalı

-Ollama API’ye bağlanamıyorsa:
Ollama arka planda çalışıyor mu kontrol edilmeli

yeni bir terminal açıp bash/ ollama serve komutu tekrar çalıştırılmalı

-Minikube podları çalışmıyorsa:
Deployment dosyasında imagePullPolicy: Never eklenmeli
ve docker build işlemi minikube docker ortamında yapılmalı

-Request modülü bulunamadı hatası:
bash/ pip3 install requests

!!! eğer pip3 veya python3 gibi bash kodları sizde çalışmıyorsa pip, python gibi kodlar deneyebilirsiniz.
Bu proje MacOS üzerinde yazılmıştır.

