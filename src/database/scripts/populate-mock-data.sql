INSERT INTO committees (committee_id, committee_name, committee_abbreviation, committee_description, committee_status) VALUES (1, 'General Assembly 1', 'GA1', 'The 1st General Assembly', 'IN_SESSION') ON CONFLICT DO NOTHING;
INSERT INTO committees (committee_id, committee_name, committee_abbreviation, committee_description, committee_status) VALUES (2, 'The Jedi Council', 'TJC', 'We love democracy', 'SUSPENDED_SESSION') ON CONFLICT DO NOTHING;
INSERT INTO committees (committee_id, committee_name, committee_abbreviation, committee_description, committee_status) VALUES (3, 'The Fellowship of the Ring', 'FOR', 'After all why not, why shouldnt I keep it', 'OUT_OF_SESSION') ON CONFLICT DO NOTHING;
INSERT INTO committees (committee_id, committee_name, committee_abbreviation, committee_description, committee_status) VALUES (4, 'Human Rights Council', 'HRC', 'Teaching everyone the golden rule', 'MOD') ON CONFLICT DO NOTHING;

INSERT INTO delegations (delegation_id, delegation_name) VALUES (1, 'United States of America') ON CONFLICT DO NOTHING;
INSERT INTO delegations (delegation_id, delegation_name) VALUES (2, 'Iran') ON CONFLICT DO NOTHING;
INSERT INTO delegations (delegation_id, delegation_name) VALUES (3, 'Canada') ON CONFLICT DO NOTHING;
INSERT INTO delegations (delegation_id, delegation_name) VALUES (4, 'Ukraine') ON CONFLICT DO NOTHING;
INSERT INTO delegations (delegation_id, delegation_name) VALUES (5, 'Germany') ON CONFLICT DO NOTHING;