# make capture2dataset capture=capture.pcapng labels=labels.csv output=output.csv
capture2csv:
	python3 ./convert/capture2dataset.py $(capture) $(labels) $(output)

# make dissections2labels dissections=dissections.csv output=output.csv
dissections2labels:
	python3 ./convert/dissections2labels.py $(dissections) $(output)

# make train_models
train_models:
	cd ./model; python3 ./train_models.py
