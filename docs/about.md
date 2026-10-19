# درباره‌ی پروژه

**جاده‌ی ابریشم — آنچه باید بدانیم** کتابی فارسی درباره‌ی تاریخ، شبکه‌های ارتباطی و میراث فرهنگی جاده‌ی ابریشم است. این اثر با ترجمه و بازنویسی پژوهش‌های تاریخی، از جمله *The Silk Road: A Very Short Introduction* نوشته‌ی James A. Millward، و با توضیحات و یادداشت‌های تحلیلی برای خوانندگان فارسی‌زبان تدوین می‌شود.

این کتاب با MkDocs و پوسته‌ی Material for MkDocs ساخته شده است. کد و متن منبع در [مخزن GitHub](https://github.com/soroush-zendedel/silk-road) و نسخه‌ی منتشرشده در [سایت پروژه](https://soroush-zendedel.github.io/silk-road/) قرار دارد.

## اجرای محلی

پس از نصب Python 3.9 یا جدیدتر و Git، در Windows و PowerShell اجرا کنید:

```powershell
git clone https://github.com/soroush-zendedel/silk-road.git
Set-Location silk-road
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m mkdocs serve
```

در macOS و Linux:

```sh
git clone https://github.com/soroush-zendedel/silk-road.git
cd silk-road
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs serve
```

سپس `http://127.0.0.1:8000/` را باز کنید. برای ساخت فایل‌های سایت در `site/`:

```sh
python -m mkdocs build --strict
```

## مشارکت و انتشار

برای مشارکت، مخزن را fork کنید، تغییرات را در شاخه‌ای جداگانه بفرستید و Pull Request باز کنید. ادغام Pull Request در `main` به‌تنهایی سایت را به‌روز نمی‌کند: GitHub Pages از شاخه‌ی `gh-pages` منتشر می‌شود و مخزن گردش‌کار سفارشی برای ساخت از `main` یا Pull Request ندارد. پس از ادغام، نگه‌دارنده‌ی دارای دسترسی نوشتن باید از نسخه‌ی به‌روز `main` دستور `python -m mkdocs gh-deploy` را اجرا کند تا خروجی ساخته و به `gh-pages` فرستاده شود؛ سپس GitHub Pages آن شاخه را منتشر می‌کند.

## مجوز

محتوا تحت [مجوز Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) است؛ متن کامل در فایل [LICENSE مخزن](https://github.com/soroush-zendedel/silk-road/blob/main/LICENSE) آمده است. بازنشر و اقتباس، حتی برای استفاده‌ی تجاری، با انتساب مناسب، پیوند به مجوز و اعلام تغییرات انجام‌شده مجاز است. مجوز محتوای پروژه، مجوز کد و وابستگی‌های ثالث را تغییر نمی‌دهد.
