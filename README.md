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

## ساختار صفحه‌ها و SEO

- کتاب فقط به فارسی منتشر می‌شود؛ زبان سند `fa` و جهت نوشتار راست‌به‌چپ از تنظیمات پوسته می‌آید. برای صفحه‌ها نسخهٔ زبانی معادل دیگری تعریف نشده، بنابراین `hreflang` اضافه نشده است.
- `docs/index.md` صفحهٔ آغاز کتاب است، `docs/about.md` دربارهٔ پروژه است و فصل‌ها زیر `docs/00-introduction/` قرار دارند. ترتیب و گروه‌بندی ناوبری در `mkdocs.yml` تعریف شده است.
- `site_url` در `mkdocs.yml` برابر `https://soroush-zendedel.github.io/silk-road/` است. MkDocs canonical مطلق هر صفحه و `sitemap.xml` خروجی را بر اساس همین مسیر انتشار می‌سازد. خروجی sitemap در `site/sitemap.xml` است؛ robots.txt در این مخزن وجود ندارد و فایل سطح دامنه یا پروژه‌های دیگر بخشی از این مخزن نیست.
- `hooks/seo.py` از ناوبری MkDocs یک مسیر مشترک برای Breadcrumb دیداری و JSON-LD نوع `BreadcrumbList` می‌سازد. مسیرها از خانهٔ اصلی `https://soroush-zendedel.github.io` به صفحهٔ کتاب و سپس گروه و صفحه می‌روند. صفحهٔ آغاز کتاب Breadcrumb ندارد. ریشه به‌عنوان خانه نمایش داده می‌شود و نشانی آن دقیقاً URL دامنهٔ اصلی است.
- دادهٔ ساخت‌یافتهٔ دیگری مانند `Article` یا `SoftwareApplication` افزوده نشده؛ محتوای فعلی کتاب و وب‌سایت با Breadcrumb قابل توصیف است و نوع‌های دیگر بازتاب قابل اتکایی از اطلاعات صفحه نیستند.

برای بررسی پس از انتشار، چند URL داخلی را در [Rich Results Test](https://search.google.com/test/rich-results) و [URL Inspection در Search Console](https://search.google.com/search-console) وارسی کنید. وجود JSON-LD واجد شرایط بودن را تضمین می‌کند، نه نمایش نتیجهٔ غنی در جست‌وجو.

## مجوز و انتساب

محتوای این پروژه تحت [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) است؛ متن کامل شرایط در فایل [LICENSE](LICENSE) آمده است. بازنشر و اقتباس، از جمله استفاده‌ی تجاری، مجاز است به شرط انتساب مناسب، پیوند دادن به مجوز، و اعلام تغییراتی که انجام داده‌اید. این مجوز درباره‌ی کد پوسته یا وابستگی‌های ثالث نیست؛ مجوزهای خود آن‌ها برقرار است.
