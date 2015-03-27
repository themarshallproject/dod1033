csv: virtualenvs
	source ~/.virtualenvs/current1033/bin/activate; python dodcombine.py

virtualenvs: mkvirtualenvs
	source ~/.virtualenvs/current1033/bin/activate; pip install -r requirements.txt

mkvirtualenvs:
	virtualenv ~/.virtualenvs/current1033

download:
	mkdir -p data/current
	curl 'http://www.dispositionservices.dla.mil/EFOIA-Privacy/Documents/LESO%20Data/Alaska_Louisiana.xls' -o Alaska_Louisiana.xls
	curl 'http://www.dispositionservices.dla.mil/EFOIA-Privacy/Documents/LESO%20Data/Massachussetts_Wyoming_Territories.xls' -o Massachussetts_Wyoming_Territories.xls
	mv Alaska_Louisiana.xls data/current/
	mv Massachussetts_Wyoming_Territories.xls data/current/
	touch data/current/Alaska_Louisiana.xls
	touch data/current/Massachussetts_Wyoming_Territories.xls
