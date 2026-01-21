# Password Generator API

Bu proje, güçlü ve özelleştirilebilir şifreler oluşturmak için geliştirilmiş, FastAPI tabanlı basit bir REST API'dir.

## Özellikler

- Belirtilen uzunlukta şifre oluşturma
- Küçük harf (`lower`), büyük harf (`upper`), rakam (`digits`) ve özel karakter (`special`) seçenekleri
- Hızlı ve hafif yapı

## Kurulum

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/firatmio/password-generator-api
   cd password-generator-api
   ```

2. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

## Kullanım

Uygulamayı başlatmak için aşağıdaki komutu kullanın:

```bash
uvicorn src.password_generator_api.main:app --reload
```
veya terminalde proje kök dizinindeyken:
```bash
python -m src.password_generator_api.main
```

Not: `main.py` içinde `uvicorn.run()` çağrısı olmadığı için `uvicorn` komutunu terminalden kullanmanız önerilir.

## API Dokümantasyonu

API çalıştığında `http://127.0.0.1:8000/docs` adresine giderek Swagger UI üzerinden interaktif dokümantasyonu inceleyebilirsiniz.

### Endpoints

#### `GET /`

API'nin çalıştığını kontrol etmek için kök dizin.

**Yanıt:**
```json
{
  "message": "Hello, FastAPI!"
}
```

#### `GET /password`

Şifre oluşturma endpoint'i.

**Parametreler:**

- `length` (int, zorunlu): Şifre uzunluğu (pozitif tam sayı olmalı).
- `lower` (bool, opsiyonel): Küçük harfler kullanılsın mı? (Varsayılan: `false`)
- `upper` (bool, opsiyonel): Büyük harfler kullanılsın mı? (Varsayılan: `false`)
- `digits` (bool, opsiyonel): Rakamlar kullanılsın mı? (Varsayılan: `false`)
- `special` (bool, opsiyonel): Özel karakterler kullanılsın mı? (Varsayılan: `false`)

**Örnek İstek:**

`GET /create?length=12&lower=true&upper=true&digits=true`

**Örnek Yanıt:**

```json
{
  "password": "aB3dE9..."
}
```

**Hata Durumları:**

- `length` 0 veya daha küçükse hata döner.
- Hiçbir karakter seti seçilmezse hata döner.

## Lisans

Bu proje [MIT](LICENSE) lisansı ile lisanslanmıştır.