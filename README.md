# جاده‌ی ابریشم — آنچه باید بدانیم

این پروژه کتابی فارسی درباره‌ی تاریخ و میراث جاده‌ی ابریشم است. مخزن منبع در [GitHub](https://github.com/soroush-zendedel/silk-road) قرار دارد و سایت در [soroush-zendedel.github.io/silk-road](https://soroush-zendedel.github.io/silk-road/) منتشر می‌شود.

کتاب با MkDocs و پوسته‌ی Material for MkDocs ساخته شده است. صفحات Markdown در `docs/` و تنظیمات ساخت در `mkdocs.yml` قرار دارند.

## اجرای محلی

Python 3.9 یا جدیدتر و Git نصب کنید. در Windows، PowerShell:

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

سایت محلی در `http://127.0.0.1:8000/` در دسترس است. ساخت خروجی بدون اجرا:

```sh
python -m mkdocs build --strict
```

## انتشار

GitHub Pages از شاخه‌ی `gh-pages` منتشر می‌کند. مخزن گردش‌کار سفارشی برای ساخت از `main` یا Pull Request ندارد؛ ادغام Pull Request در `main` به‌تنهایی سایت را به‌روز نمی‌کند. پس از ادغام تغییرات، فردی با دسترسی نوشتن باید از checkout به‌روز `main` دستور زیر را اجرا کند. MkDocs خروجی را می‌سازد و به `gh-pages` می‌فرستد و GitHub Pages سپس آن شاخه را منتشر می‌کند:

```sh
python -m mkdocs gh-deploy
```

URL سایت: <https://soroush-zendedel.github.io/silk-road/>.

## مجوز و انتساب

محتوای این پروژه تحت [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) است؛ متن کامل شرایط در فایل [LICENSE](LICENSE) آمده است. بازنشر و اقتباس، از جمله استفاده‌ی تجاری، مجاز است به شرط انتساب مناسب، پیوند دادن به مجوز، و اعلام تغییراتی که انجام داده‌اید. این مجوز درباره‌ی کد پوسته یا وابستگی‌های ثالث نیست؛ مجوزهای خود آن‌ها برقرار است.
