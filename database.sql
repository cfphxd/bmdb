/*
    Parent table for hmhmhm
*/

DROP TABLE IF EXISTS bdb_ob;
CREATE TABLE bdb_ob(
    oid SERIAL4 PRIMARY KEY,
    fid INTEGER,
    name VARCHAR(255) NOT NULL DEFAULT 'unknown',
    alias VARCHAR(255),
    descr VARCHAR(255)
);

/*
    Table for food
*/

DROP TABLE IF EXISTS bdb_food;
CREATE TABLE bdb_food(
     
    PRIMARY KEY(oid)
) INHERITS(bdb_ob);


/*
    Table for symptoms
*/

DROP TABLE IF EXISTS bdb_symptom;
CREATE TABLE bdb_symtpom(
    
    PRIMARY KEY(oid)
) INHERITS(bdb_ob);

/*
    Table for diseases
*/

DROP TABLE IF EXISTS bdb_disease;
CREATE TABLE bdb_disease(
    
    PRIMARY KEY(oid)
) INHERITS(bdb_ob);


/*
    Table for system configurations
*/

DROP TABLE IF EXISTS bdb_config;
CREATE TABLE bdb_config(
    PRIMARY KEY(oid)
) INHERITS(bdb_ob);

/*
    Table of a list of attributes
*/

DROP TABLE IF EXISTS bdb_attrib_key;
CREATE TABLE bdb_attrib_key(
    PRIMARY KEY(oid)
) INHERITS(bdb_ob);

/*
    Table for hmhmhm attributes
*/

DROP TABLE IF EXISTS bdb_attrib;
CREATE TABLE bdb_attrib(
    oid SERIAL4 PRIMARY KEY NOT NULL,
    kid INTEGER NOT NULL,
    value TEXT
);

/*
    Attributes relate to attribute keys
*/
ALTER TABLE bdb_attrib ADD CONSTRAINT fk_bdb_attrib_kid FOREIGN KEY (kid) REFERENCES bdb_attrib_key(oid); 

/*
    Search field index. The search engine will search in this field
*/
CREATE INDEX idx_bdb_attrib ON bdb_attrib(value);


