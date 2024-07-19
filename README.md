# 0g faucet

-------------------
ส่วนของ Desktop Gen Wallet
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

-------------------
วิธีขอ Key Nopecha
-------------------

เข้าดิส https://nopecha.com/discord
รอ 5 นาที
ไปห้อง ⁠NopeSupport⁠free-key-discord แล้วพิมพ์ !nopecha
อย่าลืมเปิด DM ด้วย บอทจะส่ง key มาใน DM

โค้ดใช้ได้วันเดียว 100 ครั้ง 24 ชม. ต้องมาขอใหม่ไปใช้ทุกวัน

-------------------
ส่วนของ Desktop ขอ Faucet
-------------------

1. ใช้ Tor Browser ที่ติดตั้ง Extension Nopecha และใส่ API key บน Extension เปลี่ยนใหม่ทุกวัน

2. เข้า https://faucet.0g.ai/

3. รัน torauto.py

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
bash ./delegate.sh <VALIDATOR_ADDRESS>
```