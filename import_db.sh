cd db_dump
mongoimport --db ihack --collection tenders --drop --file tenders.json
mongoimport --db ihack --collection dept --drop --file dept.json
mongoimport --db ihack --collection sellers --drop --file sellers.json
mongoimport --db ihack --collection tender --drop --file tender.json
cd ..
