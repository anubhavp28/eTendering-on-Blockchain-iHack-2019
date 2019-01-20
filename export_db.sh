cd db_dump
mongoexport --db ihack --collection tenders --out tenders.json
mongoexport --db ihack --collection dept --out dept.json
mongoexport --db ihack --collection sellers --out sellers.json
mongoexport --db ihack --collection tender --out tender.json
cd ..

