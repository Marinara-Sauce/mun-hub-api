-- SQLite
INSERT INTO committees (committee_name, committee_abbreviation, committee_description, committee_status) VALUES ('General Assembly 1', 'GA1', 'The 1st General Assembly', 'IN_SESSION');
INSERT INTO committees (committee_name, committee_abbreviation, committee_description, committee_status) VALUES ('The Jedi Council', 'TJC', 'We love democracy', 'SUSPENDED_SESSION');
INSERT INTO committees (committee_name, committee_abbreviation, committee_description, committee_status) VALUES ('The Fellowship of the Ring', 'FOR', 'After all why not, why shouldnt I keep it', 'OUT_OF_SESSION');
INSERT INTO committees (committee_name, committee_abbreviation, committee_description, committee_status) VALUES ('Human Rights Council', 'HRC', 'Teaching everyone the golden rule', 'MOD');

INSERT INTO delegations (delegation_name) VALUES ('United States of America');
INSERT INTO delegations (delegation_name) VALUES ('Iran');
INSERT INTO delegations (delegation_name) VALUES ('Canada');
INSERT INTO delegations (delegation_name) VALUES ('Ukraine');
INSERT INTO delegations (delegation_name) VALUES ('Germany');

SELECT * FROM committees;
SELECT * FROM delegations;