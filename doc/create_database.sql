/*
    Parent table for hmhmhm
*/

DROP TABLE IF EXISTS bdb_ob CASCADE;
CREATE TABLE bdb_ob(
    oid SERIAL4 PRIMARY KEY,
    fid INTEGER,
    name VARCHAR(255) NOT NULL DEFAULT 'unknown',
    alias VARCHAR(255),
    descr VARCHAR(255),
    date_created DATE DEFAULT now(),
    date_last    DATE DEFAULT now()
);

CREATE FUNCTION bdb_ob_stamp() RETURNS trigger AS $bdb_ob_stamp$
    BEGIN
        -- Remember who changed the payroll when
        NEW.date_last := now();
        --NEW.last_user := current_user;
        RETURN NEW;
    END;
$bdb_ob_stamp$ LANGUAGE plpgsql;


CREATE TRIGGER bdb_trg_date_changed 
    BEFORE UPDATE OR INSERT 
    ON bdb_ob
    FOR EACH ROW EXECUTE PROCEDURE bdb_ob_stamp();

/*
    Table for biomarker
*/

DROP TABLE IF EXISTS bdb_biomarker CASCADE;
CREATE TABLE bdb_biomarker(
    PRIMARY KEY(oid)
) INHERITS(bdb_ob);


/*
    Table for food
*/

DROP TABLE IF EXISTS bdb_food CASCADE;
CREATE TABLE bdb_food(
     
    PRIMARY KEY(oid)
) INHERITS(bdb_ob);


/*
    Table for symptoms
*/

DROP TABLE IF EXISTS bdb_symptom CASCADE;
CREATE TABLE bdb_symptom(
    
    PRIMARY KEY(oid)
) INHERITS(bdb_ob);

/*
    Table for diseases
*/

DROP TABLE IF EXISTS bdb_disease CASCADE;
CREATE TABLE bdb_disease(
    
    PRIMARY KEY(oid)
) INHERITS(bdb_ob);


/*
    Table for system configurations
*/

DROP TABLE IF EXISTS bdb_config CASCADE;
CREATE TABLE bdb_config(
    PRIMARY KEY(oid)
) INHERITS(bdb_ob);

/*
    Table of a list of attributes
*/

DROP TABLE IF EXISTS bdb_attrib_key CASCADE;
CREATE TABLE bdb_attrib_key(
    PRIMARY KEY(oid)
) INHERITS(bdb_ob);


/*
    Table for hmhmhm attributes
*/

DROP TABLE IF EXISTS bdb_attrib CASCADE;
CREATE TABLE bdb_attrib(
    oid SERIAL4 PRIMARY KEY NOT NULL,
    kid INTEGER NOT NULL REFERENCES bdb_attrib_key(oid),
    value TEXT
);


/*
    Table for hmhmhm attributes
*/

DROP TABLE IF EXISTS bdb_biomarker_assn CASCADE;
CREATE TABLE bdb_biomarker_assn(
    oid SERIAL4 PRIMARY KEY NOT NULL,
    biom_id INTEGER NOT NULL,
    attr_id INTEGER NOT NULL 
);

DROP TABLE IF EXISTS bdb_food_assn CASCADE;
CREATE TABLE bdb_food_assn(
    oid SERIAL4 PRIMARY KEY NOT NULL,
    food_id INTEGER NOT NULL,
    attr_id INTEGER NOT NULL
);

DROP TABLE IF EXISTS bdb_symptom_assn CASCADE;
CREATE TABLE bdb_symptom_assn(
    oid SERIAL4 PRIMARY KEY NOT NULL,
    symp_id INTEGER NOT NULL,
    attr_id INTEGER NOT NULL
);

DROP TABLE IF EXISTS bdb_disease_assn CASCADE;
CREATE TABLE bdb_disease_assn(
    oid SERIAL4 PRIMARY KEY NOT NULL,
    dise_id INTEGER NOT NULL,
    attr_id INTEGER NOT NULL
);




ALTER TABLE bdb_biomarker_assn ADD CONSTRAINT fk_bdb_biomarker_assn_biom_id FOREIGN KEY (biom_id) REFERENCES bdb_biomarker(oid);
ALTER TABLE bdb_biomarker_assn ADD CONSTRAINT fk_bdb_biomarker_assn_attr_id FOREIGN KEY (attr_id) REFERENCES bdb_attrib(oid);
ALTER TABLE bdb_food_assn      ADD CONSTRAINT fk_bdb_food_assn_food_id FOREIGN KEY (food_id) REFERENCES bdb_food(oid);
ALTER TABLE bdb_food_assn      ADD CONSTRAINT fk_bdb_food_assn_attr_id FOREIGN KEY (attr_id) REFERENCES bdb_attrib(oid);
ALTER TABLE bdb_symptom_assn   ADD CONSTRAINT fk_bdb_symp_assn_symp_id FOREIGN KEY (symp_id) REFERENCES bdb_symptom(oid);
ALTER TABLE bdb_symptom_assn   ADD CONSTRAINT fk_bdb_symp_assn_attr_id FOREIGN KEY (attr_id) REFERENCES bdb_attrib(oid);
ALTER TABLE bdb_disease_assn   ADD CONSTRAINT fk_bdb_symp_assn_dise_id FOREIGN KEY (dise_id) REFERENCES bdb_disease(oid);
ALTER TABLE bdb_disease_assn   ADD CONSTRAINT fk_bdb_symp_assn_attr_id FOREIGN KEY (attr_id) REFERENCES bdb_attrib(oid);



/*
    Search field index. The search engine will search in this field
*/
CREATE INDEX idx_bdb_attrib ON bdb_attrib(value);


