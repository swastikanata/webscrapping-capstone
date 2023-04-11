# Web-Scrapping using Beautifulsoup

Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy Data Analytics Specialization. Deliverables yang diharapkan dari projek ini adalah melakukan simple webscrapping untuk mendapatkan informasi. Kita juga akan memanfaatkan flask dashboard sederhana untuk menampilkan hasil scrap dan visualisasi kita.

## Dependencies

- beautifulSoup4
- pandas
- flask
- matplotlib

Atau cukup menginstall requirements.txt dengan cara berikut

```python
pip install -r requirements.txt
```

## Rubrics

- Environment preparation (2 points)
- Finding the right key to scrap the data  & Extracting the right information (5 points)
- Creating data frame & Data wrangling (5 points)
- Creating a tidy python notebook as a report. (2 points)
- Implement it on flask dashboard (2 points)

### The Final Mission

Pada captsone kali ini, Bapak Ibu bisa memilih salah satu soal ini untuk dikerjakan.

1. (Easy) Data Volume Penjualan Ethereum dari `https://www.coingecko.com/en/coins/ethereum/historical_data?start_date=2022-01-01&end_date=2023-03-30#panel`

   * Dari halaman tersebut carilah `Date`, dan `Volume`.
   * Buat lah plot pergerakan volume perdagangan dari Ethereum. 

2. (Medium) Data kurs US Dollar ke rupiah dari `https://www.exchange-rates.org/history/IDR/USD/T`

    * Dari halaman tersebut carilah `harga harian`, dan `tanggal`
    * Bualah plot pergerakan kurs USD 
    
3. (Hard) Data pekerjaan data di indonesia pada  `https://www.kalibrr.id/job-board/te/data/1`

    * Dari Halaman tersebut carilah `title pekerjaan` , `lokasi pekerjaan` , `tanggal pekerjaan di post dan dealine submit permohonan`, dan `perusahaan`
    * tariklah 15 halaman
    * Buatlah plot dari jumlah pekerjaan berdasarkan lokasi.


Happy learning! 
