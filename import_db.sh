cd db_dump
mongoimport --db test --collection tenders --drop --file tenders.json
mongoimport --db test --collection tenders --drop --file dept.json
mongoimport --db test --collection tenders --drop --file sellers.json
mongoimport --db test --collection tenders --drop --file tender.json
cd ..
