--
-- Reset sequences after data MASS loading
--
DO $$
DECLARE
    mymax INTEGER;
    mysql TEXT;
BEGIN
    select max(id) into mymax from wards;
    mysql := 'ALTER SEQUENCE wards_id_seq RESTART WITH '||mymax+1;
    RAISE NOTICE 'Calling %', mysql;
    EXECUTE mysql;
    select max(id) into mymax from cities;
    mysql := 'ALTER SEQUENCE cities_id_seq RESTART WITH '||mymax+1;
    RAISE NOTICE 'Calling %', mysql;
    EXECUTE mysql; 
    select max(id) into mymax from province;
    mysql := 'ALTER SEQUENCE province_id_seq RESTART WITH '||mymax+1;
    RAISE NOTICE 'Calling %', mysql;
    EXECUTE mysql;  
    select max(id) into mymax from councillors;
    mysql := 'ALTER SEQUENCE councillors_id_seq RESTART WITH '||mymax+1;
    RAISE NOTICE 'Calling %', mysql;
    EXECUTE mysql;   
    select max(id) into mymax from faq_entries;
    mysql := 'ALTER SEQUENCE faq_entries_id_seq RESTART WITH '||mymax+1;
    RAISE NOTICE 'Calling %', mysql;
    EXECUTE mysql;     
END $$
