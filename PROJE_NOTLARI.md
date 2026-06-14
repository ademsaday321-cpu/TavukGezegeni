# Tavuk Gezegeni — Dijital QR Menü

## Canlı Site
https://ademsaday321-cpu.github.io/TavukGezegeni/

## Teknik Detaylar
- Tek dosya: `index.html` + `logo.png`
- Veri kaynağı: Google Sheets CSV (client-side fetch, veritabanı yok)
- CSV kolonları: `Ürün Adı`, `Kategorisi`, `Fiyatı`
- Fiyat formatı: `279 TRY` → `279 ₺`

## Tasarım
- Renkler: siyah `#0e0e0e`, altın `#F5C518`, kırmızı `#D62B2B`
- Fontlar: Inter (genel) + Bebas Neue (başlıklar)
- Mobil öncelikli

## Özellikler
- Yükleme animasyonu: yürüyen tavuk SVG
- Sticky arama + kaydırılabilir kategori butonları
- Ürün kartları: sol resim + sağda isim/açıklama/fiyat
- Tavuklar kategorisine otomatik açıklama: "Makarna ve Salata ile servis edilir."
- Karta tıklayınca modal açılır, arka plan blur

## Kategoriler & Ürünler
**Tavuklar:** Chilli Soslu, Çökertme, Acılım, Dağ Kekiklim, Acılı Corolina, Ali Nazik, Soya Soslu, Beğendi, Barbekü, Cevizlim, Mix, Körilim, Kremalı Mantarlı

**Yan Ürünler:** Salata, Makarna, Patates Kızartması, Soğan Halkası

**İçecekler:** Fanta Cam/Kutu, Kola Kutu/Cam/1LT, Fanta 1LT, Cappy Atom/Şeftali, Fuse Tea çeşitleri, Sprite, Soda Meyveli, Sade Soda, Su Büyük/Küçük

## Yapılacaklar
- [ ] Her ürün için resim eklenecek
- [ ] Resimler hazır olunca CSV'ye `Resim` kolonu açılıp URL'ler girilecek, kod otomatik gösterecek
