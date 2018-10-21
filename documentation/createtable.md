# CREATE TABLE -lauseet

### Käyttäjä
'''
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
'''

### Kategoria
'''
CREATE TABLE category (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
'''

'''
### Tehtävä 
CREATE TABLE task (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	priority INTEGER NOT NULL, 
	done BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (done IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
'''

'''
### Tehtävät ja kategoriat
CREATE TABLE tasks_and_categories (
	task_id INTEGER NOT NULL, 
	category_id INTEGER NOT NULL, 
	PRIMARY KEY (task_id, category_id), 
	FOREIGN KEY(task_id) REFERENCES task (id), 
	FOREIGN KEY(category_id) REFERENCES category (id)
'''
