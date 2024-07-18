# 0g faucet

แบ่งเป็น 2 ส่วน ส่วนที่รันบน Desktop อีกส่วนรันบน VPS 0g node

-------------------
ส่วนของ Desktop
-------------------

ต้องมีรัน 0g node ที่ sync เรียบร้อยแล้ว

1. ติดตั้ง python, git, ต้องมี chrome ในเครื่องลงไว้

2. เปิด Powershell, หรือ Terminal

3. รัน
```
git clone https://github.com/dekkeng/0gfaucet.git && cd 0gfaucet
cp proxy.txt.sample proxy.txt
cp config.txt.sample config.txt
pip install -r requirements.txt
```

4. แก้ไขไฟล์ config.txt
```
NOPECHA_API_KEY ให้ใส่ api key ของ nopecha
GEN_AMOUNT คือจำนวนกระเป๋าที่ต้องการสร้างต่อครั้งที่รัน gen
```

5. แก้ไขไฟล์ proxy.txt เป็นรายการ proxy ของคุณบรรทัดละ 1 ตัว เช่น
```
socks5://user:pass@111.11.11.11:1111
socks5://user2:pass2@111.11.11.12:1112
```

6. รันเพื่อสร้างกระเป๋าใหม่เพิ่ม (หากต้องการเคลียร์กระเป๋าเก่า ให้ลบไฟล์ keys.txt addrs.txt seeds.txt ออกก่อน)
```
python gen.py
```

7. รันเพื่อขอ faucet
```
python faucet.py
```

-------------------
ส่วนของ VPS
-------------------

จะเป็นส่วนของการ delegate แต่ละกระเป๋าไปที่ node หลัก

1. รัน
```
apt install -y git
git clone https://github.com/dekkeng/0gfaucet.git
cd 0gfaucet
```

2. รัน
```
printf "ketchup answer sudden fruit head edge vocal slight control salmon bonus journey\n" | 0gchaind keys add wallet1 --eth --recover
```

3. Copy ข้อมูลจาก `seeds.txt` บน desktop ที่รันไปด้านบน มาใส่ใน VPS folder เดียวกัน
```
nano seeds.txt
```
วางข้อมูล
แล้ว Ctrl + X , Y , enter

4. รัน โดยเปลี่ยน <VALIDATOR_ADDRESS> เป็นเลข validator หลักที่ต้องการ delegate
```
sudo chmod +x delegate.sh
./delegate.sh <VALIDATOR_ADDRESS>
```